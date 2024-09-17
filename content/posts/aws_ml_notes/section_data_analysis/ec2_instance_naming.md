---
date: 2024-06-05
title: "EC2 Instance Naming"
---
### EC2 Instance Types
#### First Letter
- T: general purpose burstable performance
- M: General purpose balance of compute
- C: Compute optimized
- R: RAM optimized
- X: High RAM high Compute
- P: GPU based for HPC
- G: GPU for graphics
- F: FPGA
- I: I/O optimized
- D: Dense storage
- H: High disk throughput
- A: ARM based (AWS Graviton)
#### Generation number
- 4 is older than 5 and so on

#### Additional Suffixes
- a: AMD CPU
- d: NVME SSD
- n: Networking optimized
- g: AWS Graviton (ARM) based
- i: intel (rarely used)

#### Instance Size
- micro: minimal everything, for low-throughput applications
- small, midium: for moderate applications
- large, xlarge: for high throughput applications
- \[2x-16x\]large: large scale, High performance stuff