---
date: 2023-12-06
title: "Examining Shell Generation Code"
---
## Intro
When I am reading the shell generation code I noticed the use of pytorch distributed computing. I have seen them before but never really dig deep into how they work. Now I have decided to dive into the details with the help of ChatGPT.

## Initialization
-`torch.distributed.init_process_group(backend, init_method, world_size, rank)`
    - Init the default process group (A logical group of processes, not OS level. Used as a scope for broadcasting )
    - `backend`: setup inter-process communication backend (e.g. `nccl`, `gloo`, etc.) for `inter-node` (within machine between GPUs) and `intra-node` (between machines) communication
      - `nccl` GPU-to-GPU communication directly (only for Nvidia?)
      - `gloo` CPU based cross GPU communication (probably less efficient? since you need to copy from GPU to CPU and back repeatitively for each update)
    - `world_size`: total number of processes
    - `rank`: unique ID assigend to each process

## Communication Mechanisms
- Distributed Data Parallel (DDP)
  - class `torch.nn.parallel.DistributedDataParallel`
  - DDP wraps a model and sync params across machines or GPUs.
  - Each process will have a copy of the code and model and run independently from one another (but communicate and sync during training)
-`torch.distributed.all_reduce(tensor, op, group, async_op)`
    - this operation is used to distribute averaged gradients are provided to all processes
- `torch.distributed.barrier(group)`
  - used to sync process stages (stop and wait then go together)
- Master Slave Architecture
  - One process (usually rank 0) often act as the 'master' for operations like logging and saving. 
  - but mostly processes equally share the computation
  - not as strict as other master-slave architecture

## Training Phases
- Forward Pass: Each process computes forward pass independently
- Backword Pass: Each process computes the backward pass independently (this is where the gradient is calculated but not added to the weights yet?)
- Gradient Averaging: this is where inter-process communication occurs
- Parameter update: each process updates its model independently (using its own gradient or use the averaged gradient?)

## Pytorch is scalable, not scaling
- It can be scaled using a scheduler like SLURM or Kubernetes
- Itself is not a parallel manager
- This means if you have two machines and you want to run 6 tasks, you will need to:
  - Go to each machine, run python code 3 times on one machine, 3 times again on another machine.
  - the command would look something like this:
  - `python main.py --world_size=6 --rank=0 --master_addr="192.168.1.1" --master_port=12345`
  - You need to change rank value for each process. and other distributed computing related stuff.
  - this means pytorch code is **Scalable** (There is a way to scale it) not **Scaling** (it self does not contain scaling features).
  - PyTorch is deligating the scaling tasks to more capable hands.
