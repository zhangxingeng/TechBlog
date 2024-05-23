---
date: 2024-05-01
title: "Summary of Gradient Descent Methods and Adam"
---

# Summary of Gradient Descent Methods and Adam

#### Definitions:
- **Weights $W$:** Parameters the model adjusts to minimize the loss function.
- **Learning rate $\alpha$:** Controls the step size in each iteration.
- **Gradient $\Delta_W$:** Gradient of the loss function with respect to weights.
- **Momentum $m$:** Accumulated moving average of the gradients.
- **Kinetic Energy $e$:** Squared gradients (element-wise).
- **Decay $D$:** Decay factor in RMSProp.

### Gradient Descent Methods:

1. **Vanilla Gradient Descent:**
   - Updates weights using the gradient of the loss function.
   $$
   W = W - \alpha \Delta_W
   $$

2. **Momentum:**
   - Updates momentum by accumulating past gradients.
   $$
   m_t = \beta m_{t-1} + (1 - \beta) \Delta_W
   $$
   - Updates weights using the momentum term.
   $$
   W = W - \alpha m_t
   $$

3. **AdaGrad:**
   - Accumulates the sum of squared gradients.
   $$
   e_t = e_{t-1} + (\Delta_W)^2
   $$
   - Adjusts the learning rate based on accumulated gradients.
   $$
   W = W - \frac{\alpha}{\sqrt{e_t + \epsilon}} \Delta_W
   $$

4. **RMSProp:**
   - Computes a decaying average of squared gradients.
   $$
   e_t = \beta e_{t-1} + (1 - \beta) (\Delta_W)^2
   $$
   - Updates weights using the decaying average.
   $$
   W = W - \frac{\alpha}{\sqrt{e_t + \epsilon}} \Delta_W
   $$

5. **Adam:**
   - Computes moving averages of the gradient and its square.
   $$
   m_t = \beta_1 m_{t-1} + (1 - \beta_1) \Delta_W
   $$
   $$
   e_t = \beta_2 e_{t-1} + (1 - \beta_2) (\Delta_W)^2
   $$
   - Reduces momentum bias.
   $$
   \hat{m}_t = \frac{m_t}{1 - \beta_1^t}
   $$
   - Reduces kinetic energy bias.
   $$
   \hat{e}_t = \frac{e_t}{1 - \beta_2^t}
   $$
   - Updates weights using both momentum and decaying average of squared gradients.
   $$
   W = W - \frac{\alpha \hat{m}_t}{\sqrt{\hat{e}_t} + \epsilon}
   $$

### Explanation of Adam's Logic:
Adam combines the benefits of both Momentum and RMSProp:
- **Momentum** ($m_t$) helps accelerate convergence by considering the direction and magnitude of past gradients.
- **RMSProp** ($e_t$) normalizes the gradients by considering the magnitude of recent squared gradients.

By combining these two methods, Adam adapts the learning rate based on both the mean and variance of past gradients, making it more efficient and robust for training deep learning models.

#### Notes:
- **$\beta_1$** and **$\beta_2$** are hyperparameters for the decay rates of the moving averages, typically set to 0.9 and 0.999, respectively.
- **$\epsilon$** is a small constant added to prevent division by zero.
- **$\beta^t$** refers to the decay rate raised to the power of $t$, where $t$ is the iteration step.