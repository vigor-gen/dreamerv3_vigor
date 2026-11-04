"""DMC visual generalization benchmark (VGB) wrapper.

Parts are adapted from DMControl-GB
(https://github.com/nicklashansen/dmcontrol-generalization-benchmark),
including its copy of the Distracting Control Suite camera code.
"""

import copy
import functools
import os
from collections import deque

import cv2
import elements
import embodied
import numpy as np
import xmltodict
from dm_control.suite import common
from dm_control.utils import io as resources

_SUITE_DIR = os.path.dirname(os.path.dirname(common.__file__))
_FILENAMES = [
    "./common/materials.xml",
    "./common/skybox.xml",
    "./common/visual.xml",
]
CAMERA_MODES = ['fixed', 'track', 'trackcom', 'targetbody', 'targetbodycom']


class DMCVGBWrapper(embodied.Wrapper):
  """Applies a visual perturbation to a DMC task and renders the image.

  gen_type: original, background_color, background_video, cam_pos, cam_ori,
  cam_dyn, normal_blur, gaussian_noise, light_position, light_color,
  moving_light, objects_color. gen_diff: easy, hard.
  """

  def __init__(
      self, env, task, gen_type='original', gen_diff='easy', seed=0,
      image_size=64, frame_stack=1):
    super().__init__(env)
    domain = task.split('_', 1)[0]
    self._gen_type = gen_type
    self._gen_diff = gen_diff
    self._random_state = np.random.RandomState(seed)
    self._image_size = image_size
    self._domain = domain
    self._frame_stack = frame_stack
    self._frames = deque([], maxlen=frame_stack)
    if self._gen_type == 'original':
      pass
    elif self._gen_type == 'background_color':
      self._load_colors()
    elif self._gen_type == 'background_video':
      self._video_index = 0
      self._video_paths = []
      self._load_video_paths()
      self._num_videos = len(self._video_paths)
      self._bg_frames = deque([], maxlen=self._frame_stack)
    elif self._gen_type == 'cam_pos':
      self._camera_id = 0
      offset_range = 0.08 if self._gen_diff == 'easy' else 0.15
      self._cam_xpos_offset = self._random_state.uniform(-offset_range, offset_range, size=self.env.physics.named.data.cam_xpos[self._camera_id].shape)
    elif self._gen_type in ['cam_ori', 'cam_dyn']:
      # https://github.com/nicklashansen/dmcontrol-generalization-benchmark/blob/main/src/env/distracting_control/camera.py#L160
      # cam_ori: Fixed camera with random orientation
      # cam_dyn: Dynamically distracting camera
      assert domain in ['reacher', 'cartpole', 'finger', 'cheetah', 'ball_in_cup', 'walker']
      scale = 0.3 if self._gen_diff == 'easy' else 0.8 # Manually defined difficulty
      dynamic = True if self._gen_type == 'cam_dyn' else False
      self._camera_id = 0
      self._vertical_delta=np.pi / 2 * scale
      self._horizontal_delta=np.pi / 2 * scale
      # Limit camera to -90 / 90 degree rolls.
      self._roll_delta=np.pi / 2. * scale
      self._vel_std=.1 * scale if dynamic else 0.
      self._max_vel=.4 * scale if dynamic else 0.
      self._roll_vel_std=np.pi / 300 * scale if dynamic else 0.
      self._max_roll_vel=np.pi / 50 * scale if dynamic else 0.
      self._max_zoom_in_percent=.5 * scale
      self._max_zoom_out_percent=1.5 * scale
      self._limit_to_upper_quadrant='reacher' not in domain
      # These camera state parameters will be set on the first reset call.
      self._camera_type = None
      self._camera_vel = None
      self._max_h_angle = None
      self._max_v_angle = None
      self._min_h_angle = None
      self._min_v_angle = None
      self._radius = None
      self._roll_vel = None
      self._vel_scaling = None
      self._frame_count = 0
    elif self._gen_type ==  'normal_blur':
      self._denominator = 20 if self._gen_diff == 'easy' else 10
    elif self._gen_type == 'gaussian_noise':
      self._noise_mean = 0 # white noise
      self._noise_std = 0.3 if self._gen_diff == 'easy' else 1
    elif self._gen_type in ('light_position', 'moving_light'):
      light = self.env.physics.model.light(0)
      pos = light.poscom0 if light.mode.any() else light.pos
      self._light_sphere_radius = np.linalg.norm(pos)
      if self._gen_type == 'moving_light':
        self._phi_step = np.pi/200 if self._gen_diff == 'easy' else np.pi/100
    elif self._gen_type == 'light_color':
      self._origin_light_diffuse = self.env.physics.model.light(0).diffuse.copy()
    elif self._gen_type == 'objects_color':
      self._load_colors()
    else:
      raise ValueError(f'{self._gen_type} is not supported for generalization.')

  @functools.cached_property
  def obs_space(self):
    spaces = self.env.obs_space.copy()
    spaces['image'] = elements.Space(np.uint8, (self._image_size, self._image_size, 3*self._frame_stack), 0, 255)
    return spaces

  @functools.cached_property
  def act_space(self):
    return self.env.act_space

  def _load_video_paths(self):
    video_dir = os.path.join(f'{os.path.dirname(__file__)}/../data/', f'video_{self._gen_diff}')
    num_videos = 10 if self._gen_diff == 'easy' else 100
    self._video_paths = [os.path.join(video_dir, f'video{i}.mp4') for i in range(num_videos)]

  def _load_video(self, video):
    """Load video from provided filepath and return as numpy array"""
    cap = cv2.VideoCapture(video)
    assert cap.get(cv2.CAP_PROP_FRAME_WIDTH) >= 100, 'width must be at least 100 pixels'
    assert cap.get(cv2.CAP_PROP_FRAME_HEIGHT) >= 100, 'height must be at least 100 pixels'
    n = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    buf = np.empty((n, int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)), int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), 3), np.dtype('uint8'))
    i, ret = 0, True
    while (i < n  and ret):
      ret, frame = cap.read()
      frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
      buf[i] = frame
      i += 1
    cap.release()
    return buf

  def _load_colors(self):
    self._colors_easy = np.load(f'{os.path.dirname(__file__)}/../data/color_easy.npy', allow_pickle=True)
    self._colors_hard = np.load(f'{os.path.dirname(__file__)}/../data/color_hard.npy', allow_pickle=True)

  def _reset_video(self):
    self._video_index = (self._video_index + 1) % self._num_videos
    self._video_frame = self._load_video(self._video_paths[self._video_index])

  def _setup_camera(self):
    """Set up camera motion ranges and state."""
    # Define boundaries on the range of the camera motion.
    mode = self.env.physics.model.cam_mode[0]

    camera_type = CAMERA_MODES[mode]
    assert camera_type in ['fixed', 'trackcom']

    self._camera_type = camera_type
    self._cam_initial_lookat_point = get_lookat_point(self.env.physics,
                                                    self._camera_id)

    start_pos = copy.deepcopy(
        self.env.physics.named.data.cam_xpos[self._camera_id])

    if self._camera_type != 'fixed':
      # Center the camera relative to the agent's center of mass.
      start_pos -= self.env.physics.named.data.subtree_com[1]

    start_r, start_h_angle, start_v_angle = cart2sphere(start_pos)
    # Scale the velocity by the starting radius. Most environments have radius 4,
    # but this downscales the velocity for the envs with radius < 4.
    self._vel_scaling = start_r / 4.
    self._max_h_angle = start_h_angle + self._horizontal_delta
    self._min_h_angle = start_h_angle - self._horizontal_delta
    self._max_v_angle = start_v_angle + self._vertical_delta
    self._min_v_angle = start_v_angle - self._vertical_delta

    if self._limit_to_upper_quadrant:
      # A centered cam is at np.pi / 2.
      self._max_v_angle = min(self._max_v_angle, np.pi / 2.)
      self._min_v_angle = max(self._min_v_angle, 0.)
      # A centered cam is at -np.pi / 2.
      self._max_h_angle = min(self._max_h_angle, 0.)
      self._min_h_angle = max(self._min_h_angle, -np.pi)

    self._max_roll = self._roll_delta
    self._min_roll = -self._roll_delta
    self._min_radius = max(start_r - start_r * self._max_zoom_in_percent, 0.)
    self._max_radius = start_r + start_r * self._max_zoom_out_percent

    # Decide the starting position for the camera.
    self._h_angle = self._random_state.uniform(self._min_h_angle,
                                            self._max_h_angle)

    self._v_angle = self._random_state.uniform(self._min_v_angle,
                                            self._max_v_angle)

    self._radius = self._random_state.uniform(self._min_radius,
                                            self._max_radius)

    self._roll = self._random_state.uniform(self._min_roll, self._max_roll)

    # Decide the starting velocity for the camera.
    vel = self._random_state.randn(3)
    vel /= np.sqrt(np.sum(vel**2.))
    vel *= self._random_state.uniform(0., self._max_vel)
    self._camera_vel = vel
    self._roll_vel = self._random_state.uniform(-self._max_roll_vel,
                                                self._max_roll_vel)

  def _apply(self, do_random_walk=True):
    if not self._camera_type:
      self._setup_camera()

    if do_random_walk:
      # Random walk the velocity.
      vel_delta = self._random_state.randn(3)

      self._camera_vel += vel_delta * self._vel_std * self._vel_scaling
      self._roll_vel += self._random_state.randn() * self._roll_vel_std

      # Clip velocity if it gets too big.
      vel_norm = np.sqrt(np.sum(self._camera_vel**2.))
      if vel_norm > self._max_vel * self._vel_scaling:
        self._camera_vel *= (self._max_vel * self._vel_scaling) / vel_norm

      self._roll_vel = np.clip(self._roll_vel, -self._max_roll_vel,
                                  self._max_roll_vel)

    cart_cam_pos = sphere2cart([self._radius, self._h_angle, self._v_angle])
    # Apply velocity vector to camera
    sphere_cam_pos2 = cart2sphere(cart_cam_pos + self._camera_vel)
    sphere_cam_pos2 = clip_cam_position(sphere_cam_pos2, self._min_radius,
                                        self._max_radius, self._min_h_angle,
                                        self._max_h_angle, self._min_v_angle,
                                        self._max_v_angle)

    self._camera_vel = sphere2cart(sphere_cam_pos2) - cart_cam_pos

    self._radius, self._h_angle, self._v_angle = sphere_cam_pos2

    roll2 = self._roll + self._roll_vel
    roll2 = np.clip(roll2, self._min_roll, self._max_roll)

    self._roll_vel = roll2 - self._roll
    self._roll = roll2

    cart_cam_pos = sphere2cart(sphere_cam_pos2)

    if self._limit_to_upper_quadrant:
      lookat_method = get_lookat_xmat_no_roll
    else:
      # This method avoids jitteriness at the pole but allows some roll
      # in the camera matrix. This is important for reacher.
      lookat_method = get_lookat_xmat

    if self._camera_type == 'fixed':
      lookat_mat = lookat_method(self._cam_initial_lookat_point,
                                  cart_cam_pos)
    else:
      # Go from agent centric to world coords
      cart_cam_pos += self.env.physics.named.data.subtree_com[1]
      lookat_mat = lookat_method(
          get_lookat_point(self.env.physics, self._camera_id), cart_cam_pos)

    lookat_mat = np.reshape(lookat_mat, (3, 3))
    roll_mat = rotvec2mat(self._roll, np.array([0., 0., 1.]))
    xmat = np.dot(lookat_mat, roll_mat)
    self.env.physics.named.data.cam_xpos[self._camera_id] = cart_cam_pos
    self.env.physics.named.data.cam_xmat[self._camera_id] = xmat.flatten()

  def _set_light_position(self):
    """Places light 0 on a sphere at inclination theta and azimuth phi."""
    r = self._light_sphere_radius
    pos = np.array([r*np.sin(self._theta)*np.cos(self._phi),
                    r*np.sin(self._theta)*np.sin(self._phi),
                    r*np.cos(self._theta)])
    light = self.env.physics.model.light(0)
    if light.mode[0] == 0:  # fixed light
      light.pos = pos
      light.dir = -light.pos.copy()/r
    elif light.mode[0] == 2:  # tracks the center of mass
      light.poscom0 = pos
      light.dir0 = -light.poscom0.copy()/r
    else:
      raise NotImplementedError(f'light mode {light.mode[0]} is not implemented')

  def step(self, action):
    is_reset = action['reset']
    if is_reset:
      # Model-level perturbations are applied before the task reset: reloading
      # the model discards the physics state, and the reset recomputes the light
      # positions that are rendered on the first frame.
      self._perturb_model()
    obs = self.env.step(action)
    if is_reset:
      if self._gen_type == 'cam_pos':
        current_cam_xpos = self.env.physics.data.cam_xpos[self._camera_id]
        self.env.physics.data.cam_xpos[self._camera_id] = current_cam_xpos + self._cam_xpos_offset
      elif self._gen_type in ['cam_ori', 'cam_dyn']:
        self._frame_count = 0
        self._setup_camera()
        self._apply()

      obs['image'] = self.render(self._image_size, self._image_size, camera_id=0, is_reset=True)
      return obs
    else:
      if self._gen_type == 'background_video':
        self._current_video_frame += 1
      elif self._gen_type == 'cam_pos':
        current_cam_xpos = self.env.physics.data.cam_xpos[self._camera_id]
        self.env.physics.data.cam_xpos[self._camera_id] = current_cam_xpos + self._cam_xpos_offset
      elif self._gen_type == 'moving_light':
        self._phi += self._phi_step
        self._set_light_position()
      elif self._gen_type in ['cam_ori', 'cam_dyn']:
        self._frame_count += 1
        self._apply(self._frame_count % 2 == 0)

      obs['image'] = self.render(self._image_size, self._image_size, camera_id=0)
      return obs

  def _perturb_model(self):
    """Samples and applies the per-episode perturbation of the MuJoCo model."""
    reset_kwargs = {}
    if self._gen_type == 'background_color':
      background_color = getattr(self, f'_colors_{self._gen_diff}')[self._random_state.randint(len(getattr(self, f'_colors_{self._gen_diff}')))]
      reset_kwargs['grid_rgb1'] = background_color['grid_rgb1']
      reset_kwargs['skybox_rgb'] = background_color['skybox_rgb']
      reset_kwargs['grid_rgb2'] = background_color['grid_rgb2']
      self._reload_physics(reset_kwargs)
    elif self._gen_type == 'background_video':
      self._reset_video()
      self._current_video_frame = 0
      reset_kwargs['skybox_rgb'] = [.0, .0, .0]
      reset_kwargs['skybox_rgb2'] = [.0, .0, .0]
      reset_kwargs['skybox_markrgb'] = [.0, .0, .0]

      if self._gen_diff == 'hard':
        reset_kwargs['grid_rgb1'] = [.0, .0, .0]
        reset_kwargs['grid_rgb2'] = [.0, .0, .0]
        reset_kwargs['grid_markrgb'] = [.0, .0, .0]
      self._reload_physics(reset_kwargs)
    elif self._gen_type in ['light_position', 'moving_light']:
      # theta and phi are inclination and azimuth of the spherical coordinate, respectively.
      # theta ranges [0, 30 deg] (easy) and [30,60 deg] (hard)
      self._theta = self._random_state.rand()*np.pi/6 if self._gen_diff == 'easy' else np.pi/6 + self._random_state.rand()*np.pi/6
      # phi ranges [0, 360 deg]
      self._phi = self._random_state.rand()*2*np.pi
      self._set_light_position()
    elif self._gen_type == 'light_color':
      light_diffuse_range = 0.2 if self._gen_diff == 'easy' else 10
      self.env.physics.model.light(0).diffuse = self._origin_light_diffuse + \
          self._random_state.uniform(-light_diffuse_range,light_diffuse_range,size=self._origin_light_diffuse.shape)
    elif self._gen_type == 'objects_color':
      self_color = getattr(self, f'_colors_{self._gen_diff}')[self._random_state.randint(len(getattr(self, f'_colors_{self._gen_diff}')))]
      reset_kwargs['self_rgb'] = self_color['self_rgb']
      self._reload_physics(reset_kwargs)

  def _interpolate_bg(self, bg, size:tuple):
    """Interpolate background to size of observation"""
    bg = cv2.resize(bg.astype(np.float32)/255, size, interpolation=cv2.INTER_LINEAR)
    return (bg*255.).astype(np.uint8)

  def _overlay_bg(self, img, bg):
    """Replace pure-black pixels of img with the corresponding pixels of bg."""
    assert isinstance(img, np.ndarray) and isinstance(bg, np.ndarray), 'inputs must be numpy arrays'
    assert img.dtype == np.uint8 and bg.dtype == np.uint8, 'inputs must be uint8 arrays'
    assert img.ndim == bg.ndim == 3, 'inputs must be in 3 dimensions'
    assert img.shape[-1] < img.shape[0] and img.shape[-1] < img.shape[1], 'channel should be in the last dimension'
    assert bg.shape[-1] < bg.shape[0] and bg.shape[-1] < bg.shape[1], 'channel should be in the last dimension'
    fixedRGB = np.array([0 for _ in range(img.shape[-1])], dtype='uint8')
    idx = np.where((img[:][:] == fixedRGB).all(axis=2), np.array(1, dtype=np.uint8),
                                                        np.array(0, dtype=np.uint8))
    idx = np.array([idx for _ in range(bg.shape[-1])]).transpose(1, 2, 0)
    img = (1 - idx) * img + idx * bg
    return img

  def render(self, width=None, height=None, camera_id=0, is_reset=False, visualization_only=False):
    """Returns (H, W, 3) if visualization_only, else (H, W, 3 * frame_stack)."""
    height = height or self._image_size
    width = width or self._image_size
    frame = self.env.render(width=width, height=height, camera_id=camera_id) # (H, W, C)
    num_frames = self._frame_stack if is_reset and not visualization_only else 1
    if self._gen_type == 'background_video':
      bg = self._video_frame[self._current_video_frame % len(self._video_frame)]  # select frame
      bg = self._interpolate_bg(bg, (height, width)) # scale bg to observation size, (H, W, C)
      if visualization_only:
        frame = self._overlay_bg(frame, bg) # (H, W, C)
      else:
        for _ in range(num_frames):
          self._frames.append(frame)
          self._bg_frames.append(bg)
        frame = self._overlay_bg(np.concatenate(self._frames, axis=-1), np.concatenate(self._bg_frames, axis=-1)) # (H, W, C)
    elif self._gen_type == 'normal_blur':
      kernel_height, kernel_width = height//self._denominator, width//self._denominator
      kernel_height = kernel_height+1 if kernel_height % 2 == 0 else kernel_height
      kernel_width = kernel_width+1 if kernel_width % 2 == 0 else kernel_width
      frame = cv2.blur(frame, (kernel_height, kernel_width))
      if not visualization_only:
        for _ in range(num_frames):
          self._frames.append(frame)
        frame = np.concatenate(self._frames, axis=-1)
    elif self._gen_type == 'gaussian_noise':
      if not visualization_only:
        noise = np.random.normal(self._noise_mean, self._noise_std, frame.shape).astype(frame.dtype)
        self._last_noise = noise
      else:
        repeat = height // self._image_size
        noise = np.repeat(np.repeat(self._last_noise, repeat, axis=1), repeat, axis=0)
        if noise.shape != frame.shape:
          noise = cv2.resize(noise, (height, width), interpolation=cv2.INTER_LANCZOS4)
      frame = np.clip(cv2.add(frame, noise), 0, 255)
      if not visualization_only:
        for _ in range(num_frames):
          self._frames.append(frame)
        frame = np.concatenate(self._frames, axis=-1)
    else:
      if not visualization_only:
        for _ in range(num_frames):
          self._frames.append(frame)
        frame = np.concatenate(self._frames, axis=-1)
    return frame

  def _reload_physics(self, reset_kwargs=None):
    xml_string, assets = _get_model_and_assets_from_reset_kwargs(
            f'{self._domain}.xml', reset_kwargs
        )
    key_list = list(assets.keys())
    value_list = list(assets.values())
    for i in range(len(key_list)):
      if type(assets[key_list[i]]).__name__ == 'str':
        assets[key_list[i]] = bytes(value_list[i], 'utf-8')

    self.env.physics.reload_from_xml_string(xml_string, assets=assets)

def _get_model_and_assets_from_reset_kwargs(model_fname, reset_kwargs=None):
  """"Returns a tuple containing the model XML string and a dict of assets."""
  assets = {filename: resources.GetResource(os.path.join(_SUITE_DIR, filename))
        for filename in _FILENAMES}

  if reset_kwargs is None:
    return common.read_model(model_fname), assets

  # Convert XML to dicts
  model = xmltodict.parse(common.read_model(model_fname))
  materials = xmltodict.parse(assets['./common/materials.xml'])
  skybox = xmltodict.parse(assets['./common/skybox.xml'])

  # Edit grid floor
  if 'grid_rgb1' in reset_kwargs:
    assert isinstance(reset_kwargs['grid_rgb1'], (list, tuple, np.ndarray))
    assert materials['mujoco']['asset']['texture']['@name'] == 'grid'
    materials['mujoco']['asset']['texture']['@rgb1'] = \
        f'{reset_kwargs["grid_rgb1"][0]} {reset_kwargs["grid_rgb1"][1]} {reset_kwargs["grid_rgb1"][2]}'
  if 'grid_rgb2' in reset_kwargs:
    assert isinstance(reset_kwargs['grid_rgb2'], (list, tuple, np.ndarray))
    assert materials['mujoco']['asset']['texture']['@name'] == 'grid'
    materials['mujoco']['asset']['texture']['@rgb2'] = \
        f'{reset_kwargs["grid_rgb2"][0]} {reset_kwargs["grid_rgb2"][1]} {reset_kwargs["grid_rgb2"][2]}'
  if 'grid_markrgb' in reset_kwargs:
    assert isinstance(reset_kwargs['grid_markrgb'], (list, tuple, np.ndarray))
    assert materials['mujoco']['asset']['texture']['@name'] == 'grid'
    materials['mujoco']['asset']['texture']['@markrgb'] = \
        f'{reset_kwargs["grid_markrgb"][0]} {reset_kwargs["grid_markrgb"][1]} {reset_kwargs["grid_markrgb"][2]}'
  if 'grid_texrepeat' in reset_kwargs:
    assert isinstance(reset_kwargs['grid_texrepeat'], (list, tuple, np.ndarray))
    assert materials['mujoco']['asset']['texture']['@name'] == 'grid'
    materials['mujoco']['asset']['material'][0]['@texrepeat'] = \
        f'{reset_kwargs["grid_texrepeat"][0]} {reset_kwargs["grid_texrepeat"][1]}'

  # Edit self
  if 'self_rgb' in reset_kwargs:
    assert isinstance(reset_kwargs['self_rgb'], (list, tuple, np.ndarray))
    assert materials['mujoco']['asset']['material'][1]['@name'] == 'self'
    materials['mujoco']['asset']['material'][1]['@rgba'] = \
        f'{reset_kwargs["self_rgb"][0]} {reset_kwargs["self_rgb"][1]} {reset_kwargs["self_rgb"][2]} 1'

  if reset_kwargs.__contains__('table_texture'):
    assert model['mujoco']['asset']['material'][1]['@name'] == 'table_mat'
    model['mujoco']['asset']['material'][1]['@texture'] = reset_kwargs['table_texture']

  if reset_kwargs.__contains__('ground_texture'):
    assert model['mujoco']['asset']['material']['@name'] == 'groundplane'
    model['mujoco']['asset']['material']['@texture'] = reset_kwargs['ground_texture']
  # Edit skybox
  if 'skybox_rgb' in reset_kwargs:
    assert isinstance(reset_kwargs['skybox_rgb'], (list, tuple, np.ndarray))
    assert skybox['mujoco']['asset']['texture']['@name'] == 'skybox'
    skybox['mujoco']['asset']['texture']['@rgb1'] = \
        f'{reset_kwargs["skybox_rgb"][0]} {reset_kwargs["skybox_rgb"][1]} {reset_kwargs["skybox_rgb"][2]}'
  if 'skybox_rgb2' in reset_kwargs:
    assert isinstance(reset_kwargs['skybox_rgb2'], (list, tuple, np.ndarray))
    assert skybox['mujoco']['asset']['texture']['@name'] == 'skybox'
    skybox['mujoco']['asset']['texture']['@rgb2'] = \
        f'{reset_kwargs["skybox_rgb2"][0]} {reset_kwargs["skybox_rgb2"][1]} {reset_kwargs["skybox_rgb2"][2]}'
  if 'skybox_markrgb' in reset_kwargs:
    assert isinstance(reset_kwargs['skybox_markrgb'], (list, tuple, np.ndarray))
    assert skybox['mujoco']['asset']['texture']['@name'] == 'skybox'
    skybox['mujoco']['asset']['texture']['@markrgb'] = \
        f'{reset_kwargs["skybox_markrgb"][0]} {reset_kwargs["skybox_markrgb"][1]} {reset_kwargs["skybox_markrgb"][2]}'

  # Convert back to XML
  model_xml = xmltodict.unparse(model)
  assets['./common/materials.xml'] = xmltodict.unparse(materials)
  assets['./common/skybox.xml'] = xmltodict.unparse(skybox)

  return model_xml, assets

def eul2mat(theta):
  """Converts euler angles (x, y, z) to a rotation matrix."""

  return np.array([[
      np.cos(theta[1]) * np.cos(theta[2]),
      np.sin(theta[0]) * np.sin(theta[1]) * np.cos(theta[2]) -
      np.sin(theta[2]) * np.cos(theta[0]),
      np.sin(theta[1]) * np.cos(theta[0]) * np.cos(theta[2]) +
      np.sin(theta[0]) * np.sin(theta[2])
  ],
                  [
                      np.sin(theta[2]) * np.cos(theta[1]),
                      np.sin(theta[0]) * np.sin(theta[1]) * np.sin(theta[2]) +
                      np.cos(theta[0]) * np.cos(theta[2]),
                      np.sin(theta[1]) * np.sin(theta[2]) * np.cos(theta[0]) -
                      np.sin(theta[0]) * np.cos(theta[2])
                  ],
                  [
                      -np.sin(theta[1]),
                      np.sin(theta[0]) * np.cos(theta[1]),
                      np.cos(theta[0]) * np.cos(theta[1])
                  ]])


def _mat_from_theta(cos_theta, sin_theta, a):
  """Builds a rotation matrix from theta and an orientation vector."""

  row1 = [
      cos_theta + a[0]**2. * (1. - cos_theta),
      a[0] * a[1] * (1 - cos_theta) - a[2] * sin_theta,
      a[0] * a[2] * (1 - cos_theta) + a[1] * sin_theta
  ]
  row2 = [
      a[1] * a[0] * (1 - cos_theta) + a[2] * sin_theta,
      cos_theta + a[1]**2. * (1 - cos_theta),
      a[1] * a[2] * (1. - cos_theta) - a[0] * sin_theta
  ]
  row3 = [
      a[2] * a[0] * (1. - cos_theta) - a[1] * sin_theta,
      a[2] * a[1] * (1. - cos_theta) + a[0] * sin_theta,
      cos_theta + (a[2]**2.) * (1. - cos_theta)
  ]
  return np.stack([row1, row2, row3])


def rotvec2mat(theta, vec):
  """Converts a rotation around a vector to a rotation matrix."""

  a = vec / np.sqrt(np.sum(vec**2.))
  sin_theta = np.sin(theta)
  cos_theta = np.cos(theta)

  return _mat_from_theta(cos_theta, sin_theta, a)


def get_lookat_xmat_no_roll(agent_pos, camera_pos):
  """Solves for the cam rotation centering the agent with 0 roll."""

  # NOTE(austinstone): This method leads to wild oscillations around the north
  # and south polls.
  # For example, if agent is at (0., 0., 0.) and the camera is at (.01, 0., 1.),
  # this will produce a yaw of 90 degrees whereas if the camera is slightly
  # adjacent at (-.01, 0., 1.) this will produce a yaw of -90 degrees. I'm
  # not sure what the fix is, as this seems like the behavior we want in all
  # environments except for reacher.
  delta_vec = agent_pos - camera_pos
  delta_vec /= np.sqrt(np.sum(delta_vec**2.))
  yaw = np.arctan2(delta_vec[0], delta_vec[1])
  pitch = np.arctan2(delta_vec[2], np.sqrt(np.sum(delta_vec[:2]**2.)))
  pitch += np.pi / 2.  # Camera starts out looking at [0, 0, -1.]
  return eul2mat([pitch, 0., -yaw]).flatten()


def get_lookat_xmat(agent_pos, camera_pos):
  """Solves for the cam rotation centering the agent, allowing roll."""

  # Solve for the rotation which centers the agent in the scene.
  delta_vec = agent_pos - camera_pos
  delta_vec /= np.sqrt(np.sum(delta_vec**2.))
  y_vec = np.array([0., 0., -1.])  # This is where the cam starts from.
  a = np.cross(y_vec, delta_vec)
  sin_theta = np.sqrt(np.sum(a**2.))
  cos_theta = np.dot(delta_vec, y_vec)
  a /= (np.sqrt(np.sum(a**2.)) + .0001)
  return _mat_from_theta(cos_theta, sin_theta, a)


def cart2sphere(cart):
  r = np.sqrt(np.sum(cart**2.))
  h_angle = np.arctan2(cart[1], cart[0])
  v_angle = np.arctan2(np.sqrt(np.sum(cart[:2]**2.)), cart[2])
  return np.array([r, h_angle, v_angle])


def sphere2cart(sphere):
  r, h_angle, v_angle = sphere
  x = r * np.sin(v_angle) * np.cos(h_angle)
  y = r * np.sin(v_angle) * np.sin(h_angle)
  z = r * np.cos(v_angle)
  return np.array([x, y, z])


def clip_cam_position(position, min_radius, max_radius, min_h_angle,
                  max_h_angle, min_v_angle, max_v_angle):
  new_position = [-1., -1., -1.]
  new_position[0] = np.clip(position[0], min_radius, max_radius)
  new_position[1] = np.clip(position[1], min_h_angle, max_h_angle)
  new_position[2] = np.clip(position[2], min_v_angle, max_v_angle)
  return new_position


def get_lookat_point(physics, camera_id):
  """Get the point that the camera is looking at.

  It is assumed that the "point" the camera looks at the agent distance
  away and projected along the camera viewing matrix.

  Args:
      physics: mujoco physics objects
      camera_id: int

  Returns:
      position: float32 np.array of length 3
  """
  dist_to_agent = physics.named.data.cam_xpos[
      camera_id] - physics.named.data.subtree_com[1]
  dist_to_agent = np.sqrt(np.sum(dist_to_agent**2.))
  initial_viewing_mat = copy.deepcopy(physics.named.data.cam_xmat[camera_id])
  initial_viewing_mat = np.reshape(initial_viewing_mat, (3, 3))
  z_vec = np.array([0., 0., -dist_to_agent])
  rotated_vec = np.dot(initial_viewing_mat, z_vec)
  return rotated_vec + physics.named.data.cam_xpos[camera_id]

