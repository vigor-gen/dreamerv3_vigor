# DreamerV3 + VIGOR

This repository adds VIGOR, a set of auxiliary objectives for zero-shot visual
generalization, to [DreamerV3][dreamerv3]. Agents are trained on clean images
and evaluated without fine-tuning on unseen visual perturbations from a visual
generalization benchmark (VGB) built on the DeepMind Control Suite (DMC) and
robosuite. A TD-MPC2-based variant of VIGOR ([TD-MPC2+VIGOR][tigor]) uses the same benchmark and evaluation protocol. For more details, please visit [here][vigor-gen].

## Changes from DreamerV3

This code is based on [danijar/dreamerv3][dreamerv3] at commit
[`f8817c4`][base]. The DreamerV3 agent (`dreamerv3/agent.py`,
`dreamerv3/rssm.py`) is unchanged. The changes are:

- `dreamerv3/agent_vigor.py`, `dreamerv3/vigor_aug.py`: the VIGOR objectives.
- `dreamerv3/eval.py`: the zero-shot generalization sweep.
- `embodied/vgb/`: benchmark wrappers for DMC (`DMCVGBWrapper`) and robosuite
  (`RoboVGBWrapper`), plus robosuite scene presets.
- `embodied/envs/rsuite.py`: a robosuite environment (Panda arms, `OSC_POSE`
  controller, 64x64 `agentview` camera, 500-step episodes, shaped reward).
- `embodied/data/`: background videos, colors, and textures for the benchmark.
- `embodied/envs/dmc.py`: seeds the task through `suite.load` and returns a
  placeholder image, which `DMCVGBWrapper` replaces with the rendered and
  perturbed frame.
- `dreamerv3/configs.yaml`: the `robosuite` and `dreamer_vigor` config blocks,
  the `agent.vigor` hyperparameters, the `run.gen_type` and `run.gen_diff`
  options, and new defaults (`seed: 5`, `script: train_eval`,
  `run.steps: 1e6`, `run.envs: 10`, `replay.size: 1e6`,
  `run.report_every: 10000`, `env.dmc.use_seed: True`).
- `embodied/run/train_eval.py`: logs episode success for robosuite
  (`successes.jsonl`).

## Installation

The code needs Linux, an NVIDIA GPU with CUDA 12, and Python 3.11. MuJoCo
renders headlessly through EGL (`MUJOCO_GL=egl` is set by default).

Install with [uv][uv], which uses the pinned versions in `uv.lock`:

```sh
uv sync
source .venv/bin/activate
```

Or install with conda and pip:

```sh
conda create -n dreamerv3-vigor python=3.11
conda activate dreamerv3-vigor
pip install -U -r requirements.txt
```

Then create the robosuite macros file once:

```sh
python $(python -c "import robosuite, os; print(os.path.dirname(robosuite.__file__))")/scripts/setup_macros.py
```

VIGOR training also needs the [Places365][places] images (about 27 GB).
Evaluation and the DreamerV3 baseline do not.

```sh
wget http://data.csail.mit.edu/places/places365/places365standard_easyformat.tar
tar -xf places365standard_easyformat.tar  # creates places365_standard/train/...
```

### Docker

```sh
docker build -f Dockerfile -t dreamerv3-vigor .
docker run -it --rm --gpus all \
  -v ./log:/logdir -v /path/to/places365_standard:/places365_standard \
  dreamerv3-vigor python dreamerv3/main.py \
  --logdir /logdir/walker_walk/vigor/5 --seed 5 \
  --task dmc_walker_walk --configs dmc_vision dreamer_vigor \
  --agent.vigor.places_dir /places365_standard
```

## Training

| Suite | `--task` | `--configs` |
|---|---|---|
| DMC | `dmc_walker_walk`, `dmc_walker_stand`, `dmc_cheetah_run`, `dmc_cartpole_swingup`, `dmc_reacher_easy`, `dmc_finger_spin` | `dmc_vision` |
| robosuite | `robosuite_Door`, `robosuite_Lift`, `robosuite_NutAssemblyRound`, `robosuite_TwoArmPegInHole` | `robosuite` |

Train the DreamerV3 baseline:

```sh
python dreamerv3/main.py --logdir ./log/walker_walk/dreamer/5 --seed 5 \
  --task dmc_walker_walk --configs dmc_vision
```

Train DreamerV3+VIGOR by adding the `dreamer_vigor` config block and the
Places365 directory:

```sh
python dreamerv3/main.py --logdir ./log/walker_walk/vigor/5 --seed 5 \
  --task dmc_walker_walk --configs dmc_vision dreamer_vigor \
  --agent.vigor.places_dir /path/to/places365_standard

python dreamerv3/main.py --logdir ./log/Door/vigor/5 --seed 5 \
  --task robosuite_Door --configs robosuite dreamer_vigor \
  --agent.vigor.places_dir /path/to/places365_standard
```

### VIGOR hyperparameters (set with `--agent.vigor.<name>`):

| Name | Default | Description |
|---|---|---|
| `places_dir` | `''` | Places365 directory containing `train/`. Required for VIGOR. |
| `num_bg` | `2048` | Number of Places365 images loaded at startup. |
| `alpha` | `0.5` | Blend weight of the background in the strong view. |
| `pad` | `4` | Padding of the random shift, in pixels. |
| `weak_ratio` | `0.5` | Fraction of sequences that use the weak-only view. |
| `es_scale` | `1.0` | Weight of the ES loss. |
| `partition` | `train` | Places365 split to load. |
| `seed` | `0` | Seed for choosing the background images. |

## Evaluation

Run the full sweep on a trained log directory, passing the same `--task`,
`--configs`, and `--seed` as for training:

```sh
python dreamerv3/eval.py --logdir ./log/walker_walk/vigor/5 --seed 5 \
  --task dmc_walker_walk --configs dmc_vision
```

The script loads `<logdir>/checkpoint.pkl`, or the file given with
`--run.from_checkpoint`. VIGOR checkpoints load into the base DreamerV3 agent,
so Places365 is not needed for evaluation. To evaluate a single condition, pass
`--run.gen_type` (and `--run.gen_diff` for DMC), for example
`--run.gen_type cam_pos --run.gen_diff hard`.

DMC conditions, each at `easy` and `hard` difficulty:

| `gen_type` | Perturbation |
|---|---|
| `original` | None (the training condition; evaluated once) |
| `background_color` | Random floor and sky colors |
| `background_video` | Natural videos behind the agent; `hard` also hides the floor |
| `cam_pos` | Offset camera position |
| `light_position` | Light moved to a random position on a sphere |
| `light_color` | Random light color |
| `moving_light` | Light that circles the scene during the episode |
| `objects_color` | Random agent color |

robosuite bands, each with scenes 0 to 9:

| `gen_type` | Perturbation |
|---|---|
| `train` | Training-distribution scenes |
| `eval-easy` | Unseen textures, random colors and lighting |
| `eval-hard` | Unseen textures, random colors and lighting, a moving light, and a random robot color |
| `eval-extreme` | Unseen textures, random colors and lighting, a moving light, and video backgrounds |

Each condition is evaluated with 10 seeds, 25 to 34. Set the `EVAL_SEED_BASE`
environment variable to start from a different seed. On DMC, each seed runs
`run.envs` episodes (10 by default). On robosuite, each seed runs one episode
per scene, and success means the task is solved at the last step of the
episode. The seed fixes the initial states, the perturbations, and the
policy's action noise, so a condition gives the same results when rerun,
whether it is evaluated alone or as part of the full sweep.

Results are written to the log directory as `eval_avg.csv` for the full sweep,
or `<gen_type>_<gen_diff>.csv` (DMC) / `<gen_type>.csv` (robosuite) for a
single condition. The script will not
overwrite an existing results file. The evaluation config is saved as
`eval_config.yaml`.

| Suite | CSV columns |
|---|---|
| DMC | `exp_name`, `seed`, `episode_idx`, `episode_return` |
| robosuite | `exp_name`, `seed`, `episode_return`, `scene_id`, `success_rate` |

## License

This project is released under the MIT license (see `LICENSE`), which covers
both the DreamerV3 code and the changes in this repository. The following parts are adapted from other
projects and remain under their original licenses:

- `embodied/vgb/dmc.py` adapts code from [RL-ViGen][rlvigen]([DMControl-GB][dmcgb]), including its
  copy of the [Distracting Control Suite][dcs] camera code. The DMC background
  videos in `embodied/data/video_easy` and `embodied/data/video_hard` come from
  DMControl-GB.
- `embodied/vgb/rsuite.py`, `embodied/vgb/custom_xml.py`, and
  `embodied/vgb/preset_customization.py` adapt the robosuite scene
  customization from [RL-ViGen][rlvigen]([SECANT][secant]).
- [Places365][places] images are subject to the dataset's terms of use.

## Citation

If you use this code, please cite VIGOR and DreamerV3:

```bibtex
@article{park2026vigor,
  title={VIGOR: Zero-Shot Visual Generalization via Latent-Space Consistency in Model-Based Reinforcement Learning},
  author={Park, Mingyu and Noh, Samyeul and Myung, Hyun and Lee, Donghwan},
  journal={arXiv preprint arXiv:2610.02801},
  year={2026}
}

@article{hafner2025dreamerv3,
  title={Mastering diverse control tasks through world models},
  author={Hafner, Danijar and Pasukonis, Jurgis and Ba, Jimmy and Lillicrap, Timothy},
  journal={Nature},
  pages={1--7},
  year={2025},
  publisher={Nature Publishing Group}
}
```

## Acknowledgements

This code builds on [DreamerV3][dreamerv3], [dm_control][dmc],
[robosuite][robosuite], [RL-ViGen][rlvigen], [DMControl-GB][dmcgb], the
[Distracting Control Suite][dcs], [SECANT][secant], and [Places365][places].

[dreamerv3]: https://github.com/danijar/dreamerv3
[base]: https://github.com/danijar/dreamerv3/tree/f8817c4040cebada9bb9712554b0234c70c291d5
[uv]: https://docs.astral.sh/uv/
[places]: http://places2.csail.mit.edu/
[dmc]: https://github.com/google-deepmind/dm_control
[robosuite]: https://github.com/ARISE-Initiative/robosuite
[rlvigen]: https://github.com/gemcollector/RL-ViGen
[dmcgb]: https://github.com/nicklashansen/dmcontrol-generalization-benchmark
[dcs]: https://github.com/google-research/google-research/tree/master/distracting_control
[secant]: https://github.com/LinxiFan/SECANT
[vigor-gen]: https://vigor-gen.github.io
[tigor]: https://github.com/vigor-gen/tdmpc2_vigor.git