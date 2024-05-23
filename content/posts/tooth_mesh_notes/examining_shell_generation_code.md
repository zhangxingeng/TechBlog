---
date: 2023-12-06
title: "Examining Shell Generation Code"
---
## Intro
This is a breakdown of the code Shell Generation https://github.com/Golriz-code/shellGeneration/tree/main.

- The code starts from `main.py`
  - init CUDA, distributed mode, logger, tensorboard
  - logging runtime configs
  - Either run test: `test_net` or run training `run_net`
- Test is almost the same as training so lets just go through training for now  `run_net`:
  - build train and val dataloader from `PoinTr.yaml` - `dataset` (contains `train`, `val` and `test`)
  - build model from `PoinTr.yaml` - `model`