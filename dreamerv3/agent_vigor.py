"""Dreamer+VIGOR: DreamerV3 with VIGOR's AW, DC, and ES objectives.

  1. Asymmetric weak-to-strong augmentation (AW): each replayed image batch is
     encoded as a weak-only view and a weak-to-strong view, and the world model
     input mixes them per sequence (half weak-only, half weak-to-strong). See
     `vigor_aug.py`.

  2. Dynamics-level consistency (DC): the RSSM is trained on the mixed input,
     but its dynamics and representation KLs target a stop-gradient weak-only
     posterior:
        dyn = KL( sg(post_weak) || prior_mixed )
        rep = KL( post_mixed    || sg(post_weak) )

  3. Encoder-level stabilization (ES): an l2-normalized MSE that aligns the
     strong embedding to the stop-gradient weak embedding.

Only `loss()` is overridden and no parameters are added, so checkpoints are
architecture-compatible with the base DreamerV3 agent.
"""

import jax
import jax.numpy as jnp
import ninjax as nj

from . import agent as A
from . import vigor_aug

f32 = jnp.float32
sg = A.sg


class Agent(A.Agent):

  def __init__(self, obs_space, act_space, config):
    super().__init__(obs_space, act_space, config)
    v = config.vigor
    # Register the scale of the new ES loss.
    self.scales = dict(self.scales)
    self.scales['es'] = float(v.es_scale)
    # Infer the image resolution from the first image obs key.
    imgsize = v.image_size
    for k in self.enc.imgkeys:
      imgsize = obs_space[k].shape[0]
      break
    self.aug = vigor_aug.VigorAug(
        places_dir=v.places_dir, partition=v.partition, num_bg=int(v.num_bg),
        image_size=int(imgsize), alpha=float(v.alpha), pad=int(v.pad),
        weak_ratio=float(v.weak_ratio), seed=int(v.seed))

  def loss(self, carry, obs, prevact, training):
    enc_carry, dyn_carry, dec_carry = carry
    reset = obs['is_first']
    B, T = reset.shape
    losses = {}
    metrics = {}

    # AW: encode weak-only and weak-to-strong views, mix them per sequence
    obs_weak, obs_strong, is_weak = self.aug.make_views(
        obs, self.enc.imgkeys, nj.seed())
    enc_carry, enc_entries, tokens_weak = self.enc(
        enc_carry, obs_weak, reset, training)
    _, _, tokens_strong = self.enc(enc_carry, obs_strong, reset, training)
    mask = is_weak[:, None, None]
    tokens_mixed = jnp.where(mask, tokens_weak, tokens_strong)

    # ES: squared distance of l2-normalized embeddings, 2(1 - cos) in [0, 4]
    zw = f32(tokens_weak)
    zs = f32(tokens_strong)
    zw = zw / (jnp.linalg.norm(zw, axis=-1, keepdims=True) + 1e-8)
    zs = zs / (jnp.linalg.norm(zs, axis=-1, keepdims=True) + 1e-8)
    losses['es'] = ((zs - sg(zw)) ** 2).sum(-1)

    # DC: weak-only posterior as a stop-gradient target
    _, _, feat_weak = self.dyn.observe(
        dyn_carry, sg(tokens_weak), prevact, reset, training)
    post_weak = sg(feat_weak['logit'])

    # World model on the mixed input
    dyn_carry, dyn_entries, repfeat = self.dyn.observe(
        dyn_carry, tokens_mixed, prevact, reset, training)
    prior_mixed = self.dyn._prior(repfeat['deter'])
    post_mixed = repfeat['logit']
    dyn = self.dyn._dist(post_weak).kl(self.dyn._dist(prior_mixed))
    rep = self.dyn._dist(post_mixed).kl(self.dyn._dist(post_weak))
    if self.dyn.free_nats:
      dyn = jnp.maximum(dyn, self.dyn.free_nats)
      rep = jnp.maximum(rep, self.dyn.free_nats)
    losses['dyn'] = dyn
    losses['rep'] = rep
    metrics['dyn_ent'] = self.dyn._dist(prior_mixed).entropy().mean()
    metrics['rep_ent'] = self.dyn._dist(post_mixed).entropy().mean()

    # Heads on the mixed latent; images are reconstructed as the weak view
    dec_carry, dec_entries, recons = self.dec(
        dec_carry, repfeat, reset, training)
    inp = sg(self.feat2tensor(repfeat), skip=self.config.reward_grad)
    losses['rew'] = self.rew(inp, 2).loss(obs['reward'])
    con = f32(~obs['is_terminal'])
    if self.config.contdisc:
      con *= 1 - 1 / self.config.horizon
    losses['con'] = self.con(self.feat2tensor(repfeat), 2).loss(con)
    for key, recon in recons.items():
      space = self.obs_space[key]
      value = obs_weak[key] if A.isimage(space) else obs[key]
      target = f32(value) / 255 if A.isimage(space) else value
      losses[key] = recon.loss(sg(target))

    shapes = {k: v.shape for k, v in losses.items()}
    assert all(x == (B, T) for x in shapes.values()), ((B, T), shapes)

    # Imagination
    K = min(self.config.imag_last or T, T)
    H = self.config.imag_length
    starts = self.dyn.starts(dyn_entries, dyn_carry, K)
    policyfn = lambda feat: A.sample(self.pol(self.feat2tensor(feat), 1))
    _, imgfeat, imgprevact = self.dyn.imagine(starts, policyfn, H, training)
    first = jax.tree.map(
        lambda x: x[:, -K:].reshape((B * K, 1, *x.shape[2:])), repfeat)
    imgfeat = A.concat([sg(first, skip=self.config.ac_grads), sg(imgfeat)], 1)
    lastact = policyfn(jax.tree.map(lambda x: x[:, -1], imgfeat))
    lastact = jax.tree.map(lambda x: x[:, None], lastact)
    imgact = A.concat([imgprevact, lastact], 1)
    assert all(x.shape[:2] == (B * K, H + 1) for x in jax.tree.leaves(imgfeat))
    assert all(x.shape[:2] == (B * K, H + 1) for x in jax.tree.leaves(imgact))
    inp = self.feat2tensor(imgfeat)
    los, imgloss_out, mets = A.imag_loss(
        imgact,
        self.rew(inp, 2).pred(),
        self.con(inp, 2).prob(1),
        self.pol(inp, 2),
        self.val(inp, 2),
        self.slowval(inp, 2),
        self.retnorm, self.valnorm, self.advnorm,
        update=training,
        contdisc=self.config.contdisc,
        horizon=self.config.horizon,
        **self.config.imag_loss)
    losses.update({k: v.mean(1).reshape((B, K)) for k, v in los.items()})
    metrics.update(mets)

    # Replay
    if self.config.repval_loss:
      feat = sg(repfeat, skip=self.config.repval_grad)
      last, term, rew = [obs[k] for k in ('is_last', 'is_terminal', 'reward')]
      boot = imgloss_out['ret'][:, 0].reshape(B, K)
      feat, last, term, rew, boot = jax.tree.map(
          lambda x: x[:, -K:], (feat, last, term, rew, boot))
      inp = self.feat2tensor(feat)
      los, reploss_out, mets = A.repl_loss(
          last, term, rew, boot,
          self.val(inp, 2),
          self.slowval(inp, 2),
          self.valnorm,
          update=training,
          horizon=self.config.horizon,
          **self.config.repl_loss)
      losses.update(los)
      metrics.update(A.prefix(mets, 'reploss'))

    assert set(losses.keys()) == set(self.scales.keys()), (
        sorted(losses.keys()), sorted(self.scales.keys()))
    metrics.update({f'loss/{k}': v.mean() for k, v in losses.items()})
    loss = sum([v.mean() * self.scales[k] for k, v in losses.items()])

    carry = (enc_carry, dyn_carry, dec_carry)
    entries = (enc_entries, dyn_entries, dec_entries)
    outs = {'tokens': tokens_mixed, 'repfeat': repfeat, 'losses': losses}
    return loss, (carry, entries, outs, metrics)
