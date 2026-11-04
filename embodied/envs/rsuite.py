import functools
import os

import cv2
import elements
import embodied
import robosuite
import numpy as np
from robosuite.controllers import load_controller_config

class Robosuite(embodied.Env):
  def __init__(
      self, env, repeat=1, size=(64, 64)):
    if 'MUJOCO_GL' not in os.environ:
      os.environ['MUJOCO_GL'] = 'egl'
    episode_length = 500
    task_cfg = {'env_name': env, 'robots': 'Panda' if env not in ['TwoArmHandover', 'TwoArmLift', 'TwoArmPegInHole'] else ['Panda', 'Panda'],
        'camera_names': 'agentview',
        'camera_heights': size[0],
        'camera_widths': size[1],
        'camera_depths': False,
        'reward_shaping': True,
        'has_renderer': False,
        'ignore_done': False,
        'control_freq': 20,
        'hard_reset': False,
        'horizon': episode_length}
    task_cfg['controller_configs'] = load_controller_config(default_controller='OSC_POSE')
    self._env = robosuite.make(**task_cfg, use_camera_obs=True, has_offscreen_renderer=True)
    self._repeat = repeat
    self._size = size
    self._done = False

  @functools.cached_property
  def obs_space(self):
    spaces = {
        'reward': elements.Space(np.float32),
        'is_first': elements.Space(bool),
        'is_last': elements.Space(bool),
        'is_terminal': elements.Space(bool),
        'image': elements.Space(np.uint8, self._size + (3,)),
        'log/success': elements.Space(np.float32),
    }
    return spaces

  @functools.cached_property
  def act_space(self):
    return {
        'reset': elements.Space(bool),
        'action': elements.Space(np.float32, (self._env.action_dim,), self._env.action_spec[0], self._env.action_spec[1])
    }

  def step(self, action):
    for key, space in self.act_space.items():
      if not space.discrete:
        assert np.isfinite(action[key]).all(), (key, action[key])
    reset = action['reset']
    if reset or self._done:
      obs = self._env.reset()
      done, reward, info = False, 0.0, {}
      is_first = True
    else:
      done, total_reward = False, 0.0
      for _ in range(self._repeat):
        obs, reward, done, info = self._env.step(action['action'])
        total_reward += reward
        if done:
          break
      reward = np.float32(total_reward)
      is_first = False
    self._done = done
    obs = dict(
        reward=np.float32(reward),
        is_first=is_first,
        is_last=done,
        is_terminal=done,
        image=obs['agentview_image'],
    )
    obs['log/success'] = float(self._env._check_success())
    for key, space in self.obs_space.items():
      if np.issubdtype(space.dtype, np.floating):
        assert np.isfinite(obs[key]).all(), (key, obs[key])
    return obs

  def render(self, width=None, height=None, camera_id=0):
    return cv2.flip(self._env.sim.render(height=height, width=width), 0)

  def __getattr__(self, name):
    if name.startswith('__'):
      raise AttributeError(name)
    try:
      return getattr(self._env, name)
    except AttributeError:
      raise ValueError(name)