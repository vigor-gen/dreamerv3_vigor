"""Robosuite visual generalization benchmark (VGB) wrapper.

Scene presets and XML texture modding are adapted from SECANT
(https://github.com/LinxiFan/SECANT).
"""

import os
from copy import deepcopy
from typing import Optional, Union

import cv2
import embodied
import numpy as np
from robosuite.utils.mjmod import LightingModder, TextureModder

from .custom_xml import CustomMujocoXML, XMLTextureModder
from .preset_customization import DEFAULT_TASK_TEXTURE_LIST
from .preset_customization import get_custom_reset_config


class RoboVGBWrapper(embodied.Wrapper):
  """Applies a robosuite VGB scene (band x scene id) to a robosuite task.

  gen_type: train, eval-easy, eval-hard, eval-extreme. scene_id: 0 to 9.
  """

  def __init__(self, env, task, gen_type, scene_id, seed, image_size):
    super().__init__(env)
    self._robovgb_cfg = {
      'color': {
        'geom_names': None,  # all geoms are randomized
        'randomize_local': True,  # sample nearby colors
        'randomize_material': False,  # randomize material reflectance / shininess / specular
        'local_rgb_interpolation': 0.2,
        'local_material_interpolation': 0.3,
        'texture_variations': ['rgb', 'checker', 'noise', 'gradient',],  # all texture variation types
        'randomize_skybox': True  # by default, randomize skybox too
      },
      'light': {
        'light_names': None,  # all lights are randomized
        'randomize_position': False,
        'randomize_direction': False,
        'randomize_specular': False,
        'randomize_ambient': False,
        'randomize_diffuse': False,
        'randomize_active': False,
        'position_perturbation_size': 100,
        'direction_perturbation_size': 50,
        'specular_perturbation_size': 0.3,
        'ambient_perturbation_size': 0.3,
        'diffuse_perturbation_size': 0.3,
      }
    }
    assert gen_type in ['train', 'eval-easy', 'eval-hard', 'eval-extreme'], f'{gen_type} is not supported.'
    self._gen_type = gen_type
    if self._gen_type == 'train':
      self._randomize_color = self._randomize_lighting = False
      self._moving_light = False
      self._except_robot = True
      self._video_background = False
    elif self._gen_type == 'eval-easy':
      self._randomize_color = self._randomize_lighting = True
      self._moving_light = False
      self._except_robot = True
      self._video_background = False
    elif self._gen_type == 'eval-hard':
      self._randomize_color = self._randomize_lighting = True
      self._moving_light = True
      self._except_robot = False
      self._video_background = False
    elif self._gen_type == 'eval-extreme':
      self._randomize_color = self._randomize_lighting = True
      self._moving_light = True
      self._except_robot = True
      self._video_background = True
    assert scene_id in range(10), 'scene_id range: 0 ~ 9'
    self._scene_id = scene_id
    np.random.seed(seed)
    self._random_state = np.random.RandomState(seed)
    self._image_size = image_size[0] if isinstance(image_size, tuple) else image_size
    self._video_buf = self._load_video(self._gen_type, self._image_size, self._image_size) if self._video_background else None
    self._current_video_frame = 0

    custom_reset_config = get_custom_reset_config(
      task=task, gen_type=self._gen_type, scene_id=self._scene_id
    )
    if custom_reset_config is not None:
      if self._video_background:
        custom_reset_config['custom_texture']['tex_candidate']['floor'] = custom_reset_config['custom_texture']['tex_candidate']['wall'] = 'black'
      self._initialize_xml_modder(custom_reset_config.get("custom_texture", None), task)
      if custom_reset_config.get("custom_texture") is not None:
        self._reset_xml_next = True
    else:
      self._reset_xml_next = False
    self.is_first_episode = True

  def _initialize_modders(self):
    self._modders = []
    if self._randomize_color:
      self._robovgb_cfg['color']['geom_names'] = tuple(
        geom for geom in filter(lambda x: x != None, self.env.sim.model.geom_names) if 'robot' not in geom and 'gripper' not in geom)
      self._tex_modder = TextureModder(
        sim=self.env.sim, random_state=self._random_state, **self._robovgb_cfg['color']
      )
      self._modders.append(self._tex_modder)

    if self._randomize_lighting:
      self._light_modder = LightingModder(
        sim=self.env.sim,
        random_state=self._random_state,
        **self._robovgb_cfg['light'],
      )
      self._modders.append(self._light_modder)

    if self._moving_light:
      self.env.sim.model.light_pos[:, 2] = 4
      self._origin_light_pos = deepcopy(self.env.sim.model.light_pos)
      self.env.sim.model.light_castshadow = 1
      self.env.sim.model.light_directional = 0
      self._moving_light_step = 0.03
      self._light_pos_range = [self.env.sim.model.light_pos[:, 1] - 3, self.env.sim.model.light_pos[:, 1] + 3]

  def _initialize_xml_modder(self, custom_texture: Optional[Union[str, dict]], task: str):
    if custom_texture is not None:
      config = custom_texture.copy()
      if custom_texture.get("tex_to_change", None) is None:
        config["tex_to_change"] = DEFAULT_TASK_TEXTURE_LIST[task]
      self._secant_texture_modders = XMLTextureModder(**config)
    else:
      self._secant_texture_modders = None

  def _load_video(self, gen_type, image_height, image_width):
    current_dir = os.path.dirname(__file__)
    video_dir = os.path.join(current_dir, '../', 'data', gen_type)
    video_path = os.path.join(video_dir, f'video{self._scene_id}.mp4')
    cap = cv2.VideoCapture(video_path)
    self._video_len = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    buf = np.empty((self._video_len, image_height, image_width, 3),
             np.dtype('uint8'))
    i, ret = 0, True
    while (i < self._video_len and ret):
      ret, frame = cap.read()
      frame = cv2.resize(frame, (image_height, image_width))
      buf[i] = frame
      i += 1
    cap.release()
    return np.moveaxis(buf, -1, 1)

  def _reformat_obs(self, obs):
    obs = np.flipud(obs)
    if self._video_background:
      fixedRGB = np.array([0, 0, 0], dtype='uint8')
      idx = np.where((obs[:][:] == fixedRGB).all(axis=2), np.array(1, dtype=np.uint8),
               np.array(0, dtype=np.uint8))
      idx = np.array([idx, idx, idx]).transpose(1, 2, 0)
      obs = (1 - idx) * obs + idx * self._video_buf[self._current_video_frame % self._video_len, :,
                                                    :, :].transpose(1, 2, 0)
    return obs

  def step(self, action):
    is_reset = action['reset']
    if is_reset:
      self._current_video_frame = 0
      # reset from xml should only be called if a different texture/xml is requested
      if self._reset_xml_next:
        mujoco_xml = CustomMujocoXML.build_from_env(self)
        if self._secant_texture_modders is not None:
          self._secant_texture_modders.random_texture_change(mujoco_xml)
        self.env.reset_from_xml_string(mujoco_xml.to_string())
        self._reset_xml_next = False

      # update sims
      if self.is_first_episode:
        self._initialize_modders()
        self.is_first_episode = False
      for modder in self._modders:
        modder.update_sim(self.env.sim)
        modder.randomize()
      if not self._except_robot:
        rgb = self._random_state.uniform(0, 1, size=3)
        for geom in filter(lambda x: x != None, self.env.sim.model.geom_names):
          if 'robot' in geom or 'gripper' in geom:
            self._tex_modder.set_geom_rgb(geom, rgb)
      if self._moving_light:
        self.env.sim.model.light_pos = self._origin_light_pos
      self.env._reset_internal()
      self.env.sim.forward()
    else:
      self._current_video_frame += 1
      if self._moving_light:
        self.env.sim.model.light_pos[:, :] += self._moving_light_step
        y = self.env.sim.model.light_pos[:, 1]
        low, high = self._light_pos_range
        if np.any(y > high) or np.any(y < low):
          self._moving_light_step *= -1

    obs = self.env.step(action)
    obs['image'] = self._reformat_obs(obs['image'])
    return obs

  def render(self, height=None, width=None, camera_id=0):
    image = self.env.render(height, width)
    if self._video_background:
      fixedRGB = np.array([0, 0, 0], dtype='uint8')
      idx = np.where((image[:][:] == fixedRGB).all(axis=2), np.array(1, dtype=np.uint8),
                np.array(0, dtype=np.uint8))
      idx = np.array([idx, idx, idx]).transpose(1, 2, 0)
      image = (1 - idx) * image + \
        idx * cv2.resize(self._video_buf[self._current_video_frame % self._video_len, :, :, :].transpose(1, 2, 0), (image.shape[:2]))
      return image
    else:
      return image
