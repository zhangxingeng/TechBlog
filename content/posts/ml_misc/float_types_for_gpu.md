---
date: 2024-05-01
title: "How to estimate Time and GPU consumption for a deep learning model"
---
## What is Mixed precision training, and FloatPoint32 vs TensorFloat32?
- mixed means mix FP32 with TF32 (or even 16 or 64 mixed)
- FP: standard float point storage, computation is slower but higher precision
- TF: tensor float, faster computation but lower precision
- Mixed meaning:
  - Weights are stored in FP32 for better precision
  - gradients and activations in TF32
- Lets use 7 billion parameters as an example
- assume gpu is H100: 50TFLOPS for FP32, 
- Summary Comparison Table
| Format       | Total Bits | Sign Bit | Exponent Bits | Mantissa Bits | Exponent Bias |
| ------------ | ---------- | -------- | ------------- | ------------- | ------------- |
| **FP32**     | 32         | 1        | 8             | 23            | 127           |
| **TF32**     | 32         | 1        | 8             | 10            | 127           |
| **bfloat16** | 16         | 1        | 8             | 7             | 127           |

