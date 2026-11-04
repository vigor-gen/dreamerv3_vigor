"""Zero-shot generalization sweep of a trained checkpoint."""

import os
os.environ.setdefault('MUJOCO_GL', 'egl')
import datetime
import pathlib
import sys
import time

folder = pathlib.Path(__file__).parent
sys.path.insert(0, str(folder.parent))
sys.path.insert(1, str(folder.parent.parent))
__package__ = folder.name

import elements
import numpy as np
import pandas as pd
import portal
import ruamel.yaml as yaml
from termcolor import colored

from .main import make_agent, make_env

DMC_GEN_TYPES = [
    'original', 'background_color', 'background_video', 'cam_pos',
    'light_position', 'light_color', 'moving_light', 'objects_color']
DMC_GEN_DIFFS = ['easy', 'hard']
ROBO_GEN_TYPES = ['train', 'eval-easy', 'eval-hard', 'eval-extreme']
ROBO_SCENES = list(range(10))
NUM_SEEDS = 10


def main(argv=None):
  from .agent import Agent
  [elements.print(line) for line in Agent.banner]

  configs = elements.Path(folder / 'configs.yaml').read()
  configs = yaml.YAML(typ='safe').load(configs)
  parsed, other = elements.Flags(configs=['defaults']).parse_known(argv)
  config = elements.Config(configs['defaults'])
  for name in parsed.configs:
    config = config.update(configs[name])
  config = elements.Flags(config).parse(other)
  config = config.update(logdir=(
      config.logdir.format(timestamp=elements.timestamp())))

  logdir = elements.Path(config.logdir)
  print('Logdir:', logdir)
  logdir.mkdir()
  config.save(logdir / 'eval_config.yaml')

  def init():
    elements.timer.global_timer.enabled = config.logger.timer

  portal.setup(
      errfile=config.errfile and logdir / 'error',
      clientkw=dict(logging_color='cyan'),
      serverkw=dict(logging_color='cyan'),
      initfns=[init],
      ipv6=config.ipv6,
  )

  gen_type, gen_diff = config.run.gen_type, config.run.gen_diff
  suite, task = config.task.split('_', 1)
  # gen_diff only applies to DMC; a robosuite condition covers all scenes.
  if gen_type == 'all':
    csv_name = 'eval_avg.csv'
  elif suite == 'dmc':
    csv_name = f'{gen_type}_{gen_diff}.csv'
  else:
    csv_name = f'{gen_type}.csv'
  csv_path = pathlib.Path(config.logdir) / csv_name
  if csv_path.exists():
    raise FileExistsError(f'{csv_path} already exists.')

  seed_base = int(os.environ.get('EVAL_SEED_BASE', 25))
  seeds = [seed_base + i for i in range(NUM_SEEDS)]

  # VIGOR only changes the training loss and adds no parameters, so its
  # checkpoints load into the base agent without needing Places365.
  agent = make_agent(config.update(agent_variant='dreamer'))
  cp = elements.Checkpoint()
  cp.agent = agent
  cp.load(
      config.run.from_checkpoint or logdir / 'checkpoint.pkl', keys=['agent'])

  print(colored('Start evaluation', 'green'))
  start = time.time()
  rows = []
  for name, gen in conditions(suite, gen_type, gen_diff):
    for seed in seeds:
      np.random.seed(seed)
      agent.config = agent.config.update(seed=seed)
      # Action sampling is seeded by (seed, n_actions); restart the counter so
      # each run does not depend on the conditions evaluated before it.
      with agent.n_actions.lock:
        agent.n_actions.value = 0
      env = make_env(config.update(seed=seed), 0, gen)

      if suite == 'dmc':
        print(colored(f'Evaluating (exp: {name}) (seed: {seed})', 'yellow'))
        returns = [rollout(agent, env) for _ in range(config.run.envs)]
        rows += [[name, seed, i, ret] for i, ret in enumerate(returns)]
        columns = ['exp_name', 'seed', 'episode_idx', 'episode_return']
        summary = f'{task:<22}{name}+seed{seed}\tR: {np.mean(returns):.01f}  '
      else:
        scene = gen[1]
        print(colored(
            f'Evaluating (exp: {name}) (seed: {seed}) (scene: {scene})',
            'yellow'))
        ret = rollout(agent, env)
        success = float(env._check_success())
        rows.append([name, seed, ret, scene, success])
        columns = [
            'exp_name', 'seed', 'episode_return', 'scene_id', 'success_rate']
        summary = (
            f'{task:<22}{name}+seed{seed}+scene#{scene}'
            f'\tR: {ret:.01f}  \tSR: {success:.01f}  ')

      elapsed = datetime.timedelta(seconds=int(time.time() - start))
      print(colored(f'  {summary}\tT: {elapsed}', 'blue'))
      pd.DataFrame(np.array(rows)).to_csv(csv_path, header=columns, index=None)
      try:
        env.close()
      except Exception:
        pass

  elapsed = datetime.timedelta(seconds=int(time.time() - start))
  print('Finished. Elapsed time in HH:MM:SS ', str(elapsed))


def conditions(suite, gen_type, gen_diff):
  """Yields (name, gen) for every condition; gen is passed to make_env."""
  if suite == 'dmc':
    types = DMC_GEN_TYPES if gen_type == 'all' else [gen_type]
    diffs = DMC_GEN_DIFFS if gen_type == 'all' else [gen_diff]
    for t in types:
      for d in diffs:
        if t == 'original' and d == 'hard':
          continue
        yield (t if t == 'original' else f'{t}_{d}'), (t, d)
  elif suite == 'robosuite':
    types = ROBO_GEN_TYPES if gen_type == 'all' else [gen_type]
    for t in types:
      for scene in ROBO_SCENES:
        yield t, (t, scene)
  else:
    raise NotImplementedError(suite)


def rollout(agent, env):
  """Runs one episode with the eval policy and returns the episode return."""
  carry = agent.init_policy(1)
  acts = {
      k: np.zeros((1,) + v.shape, v.dtype) for k, v in env.act_space.items()}
  acts['reset'] = np.ones(1, bool)
  score = 0.0
  while True:
    obs = env.step({k: v[0] for k, v in acts.items()})
    obs = {k: np.stack([v]) for k, v in obs.items() if not k.startswith('log/')}
    carry, acts, _ = agent.policy(carry, obs, mode='eval')
    score += obs['reward'].item()
    if obs['is_last']:
      return score
    acts = {**acts, 'reset': obs['is_last']}


if __name__ == '__main__':
  main()
