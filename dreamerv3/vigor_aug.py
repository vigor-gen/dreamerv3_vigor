"""Asymmetric weak-to-strong image augmentation (AW) for Dreamer+VIGOR.

Augmentation is applied only to the replayed training batch inside the world
model loss, never to the observations used for acting or evaluation.

  - weak:   random shift (DrQ-style pad and crop).
  - strong: alpha-blend of a Places365 image over the weak view.

A fixed bank of backgrounds is loaded once at construction, so all ops are
jittable.
"""

from pathlib import Path

import jax
import jax.numpy as jnp
import numpy as np

f32 = jnp.float32


def _load_backgrounds(places_dir, partition, num_bg, image_size, seed):
  """Load `num_bg` Places365 images, resized to (image_size, image_size, 3).

  Returns a float32 numpy array in [0, 1]. Sampling is spread across category
  folders and stops early so we never enumerate the full 1.8M-image tree.
  """
  from PIL import Image, ImageFile
  ImageFile.LOAD_TRUNCATED_IMAGES = True

  if not places_dir:
    raise ValueError(
        'agent.vigor.places_dir is empty. Download Places365 and pass '
        '--agent.vigor.places_dir /path/to/places365_standard.')
  root = Path(places_dir) / partition
  if not root.exists():
    raise FileNotFoundError(
        f'Places365 directory not found: {root} '
        f'(expected <places_dir>/<partition> with category subfolders).')

  rng = np.random.RandomState(seed)
  dirs = [d for d in root.iterdir() if d.is_dir()]
  if not dirs:
    dirs = [root]
  rng.shuffle(dirs)
  per_dir = max(1, num_bg // max(1, len(dirs)) + 1)

  files = []
  for d in dirs:
    fs = []
    for pat in ('*.jpg', '*.jpeg', '*.png'):
      fs.extend(sorted(d.glob(pat)))
      if len(fs) >= per_dir:
        break
    files.extend(fs[:per_dir])
    if len(files) >= num_bg:
      break
  files = files[:num_bg]
  if not files:
    raise FileNotFoundError(f'No image files found under {root}.')

  imgs = np.zeros((len(files), image_size, image_size, 3), np.float32)
  for i, fp in enumerate(files):
    im = Image.open(fp).convert('RGB').resize((image_size, image_size))
    imgs[i] = np.asarray(im, np.float32) / 255.0
  return imgs


class VigorAug:
  """Holds preloaded backgrounds and provides jittable augmentation ops.

  All image ops expect uint8 tensors shaped (B, T, H, W, C) and return uint8, so
  they can be fed straight back into the DreamerV3 encoder (which asserts uint8).
  Weak/strong offsets and background choices are drawn per batch element and kept
  constant across the time dimension.
  """

  def __init__(
      self, places_dir, partition='train', num_bg=2048, image_size=64,
      alpha=0.5, pad=4, weak_ratio=0.5, seed=0):
    self.alpha = float(alpha)
    self.pad = int(pad)
    self.weak_ratio = float(weak_ratio)
    self.image_size = int(image_size)
    bg = _load_backgrounds(places_dir, partition, int(num_bg), self.image_size, int(seed))
    # Kept on the host: a closed-over device array would need a device-to-host
    # copy when traced, which the transfer guard in embodied.jax forbids.
    self.bg = (bg * 255).astype(np.uint8)  # (num_bg, H, W, 3)

  def random_shift(self, imgs, key):
    """DrQ-style random shift: replicate-pad by `pad`, random integer crop back."""
    assert imgs.ndim == 5, imgs.shape
    B, T, H, W, C = imgs.shape
    pad = self.pad
    padded = jnp.pad(
        imgs, ((0, 0), (0, 0), (pad, pad), (pad, pad), (0, 0)), mode='edge')
    offs = jax.random.randint(key, (B, 2), 0, 2 * pad + 1)

    def crop_one(p, off):  # p: (T, H+2pad, W+2pad, C)
      return jax.lax.dynamic_slice(p, (0, off[0], off[1], 0), (T, H, W, C))

    return jax.vmap(crop_one)(padded, offs)

  def random_overlay(self, imgs, key):
    """Alpha-blend a random Places365 background per batch element."""
    assert imgs.ndim == 5, imgs.shape
    B, T, H, W, C = imgs.shape
    assert H == self.image_size and W == self.image_size, (imgs.shape, self.image_size)
    idx = jax.random.randint(key, (B,), 0, self.bg.shape[0])
    bg = jnp.asarray(self.bg)[idx].astype(f32) / 255.0  # (B, H, W, 3) in [0, 1]
    reps = (C + 2) // 3
    bg = jnp.tile(bg, (1, 1, 1, reps))[..., :C]  # (B, H, W, C)
    bg = bg[:, None]  # (B, 1, H, W, C), broadcast over time
    x = imgs.astype(f32) / 255.0
    out = (1.0 - self.alpha) * x + self.alpha * bg
    return jnp.clip(out * 255.0, 0, 255).astype(jnp.uint8)

  def make_views(self, obs, imgkeys, key):
    """Build weak-only and weak-to-strong obs dicts plus a half/half batch mask.

    Strong is `random_overlay(random_shift(x))` so the weak and strong views of a
    sample share the same spatial shift (only the overlay differs).
    Returns (obs_weak, obs_strong, is_weak) where is_weak is a (B,) bool mask
    selecting which batch elements stay weak-only in the mixed representation.
    """
    B = obs['is_first'].shape[0]
    keys = jax.random.split(key, 2 * len(imgkeys) + 1)
    obs_weak = dict(obs)
    obs_strong = dict(obs)
    for i, ik in enumerate(imgkeys):
      weak = self.random_shift(obs[ik], keys[2 * i])
      strong = self.random_overlay(weak, keys[2 * i + 1])
      obs_weak[ik] = weak
      obs_strong[ik] = strong
    perm = jax.random.permutation(keys[-1], B)
    n_weak = int(round(B * self.weak_ratio))
    is_weak = jnp.zeros((B,), bool).at[perm[:n_weak]].set(True)
    return obs_weak, obs_strong, is_weak
