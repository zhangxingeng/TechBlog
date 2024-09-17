---
date: 2024-06-05
title: "deep net and llms"
---

### activation functions
- sigmoid / logistic $\sigma(z) = \frac{1}{1 + e^{-z}}$, y range: $(0, 1)$ feature: similar to softmax but can produce more than one label
- Tanh $tanh(z) = \frac{e^z - e^{-z}}{e^z + e^{-z}}$ y range: $(-1, 1)$ feature: mean at 0, **RNN works well with tanh**
- ReLU $max(0, z)$, feature: fast to compute. problem: negative values are set to 0, can cause dying ReLU problem
- Leaky ReLU $max(\alpha z, z)$, solves dying ReLU problem
- Parametric ReLU $max(\alpha z, z)$, $\alpha$ is a learnable parameter (by back propagation), computationally expensive
- Maxout $max(w_1^T x + b_1, w_2^T x + b_2)$, computationally expensive, but works well
- Swish $z \cdot \sigma(z)$, computationally expensive, but works really well, especially in deep networks
- Softmax: $softmax(z) = \frac{e^{z_i}}{\sum_{j=1}^{k} e^{z_j}}$, convert float output to probability distribution


### CNN
- used when you are not sure where the feature is located (like where a car is in an image)
- Typical use: Conv2D -> MaxPooling2D -> Dropout -> Flatten -> Dense -> Dropout -> Softmax
- Different CNNs:
  - LeNet-5: simple, AlexNet: image classification, 
  - GoogleNet: inception module, 
  - ResNet: residual learning (use skip connection avoid vanishing gradient problem)

### RNN
- used for sequential data where timeline matters to make sense of the data

### Transformers
- use knowledge distillation to train smaller model
- BERT: Bidirectional Encoder Representations from Transformers
- GPT: Generative Pre-trained Transformer

### Transfer Learning
- Hugging Face offer pre-trained models
- integrate with sagemaker via DLC(hugging face Distributed Learning Containers)

