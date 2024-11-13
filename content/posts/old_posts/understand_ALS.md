---
title: "Understand ALS Algorithm"
date: 2023-05-05T00:44:53-04:00
draft: false
---

- This post will not go into the details about how ALS is mathmatically proven. We only care about how gradient descent handles the task
- The task is we have a matix with $m$ users and $n$ movies, each cell represent a rating from that user about that move
- Now we want to get a user matrix and a movie matrix with $k$ latent features as their embedding, such that:
  $$ U*{m \times k} \cdot M*{k \times n} = R\_{m \times n} $$
- Example:

  $$
  R = \begin{bmatrix}
  5 & 3 & 0 & 1 \\
  4 & 0 & 0 & 1 \\
  1 & 1 & 0 & 5 \\
  1 & 0 & 0 & 4 \\
  0 & 1 & 5 & 4
  \end{bmatrix}
  $$

  $$
  U = \begin{bmatrix}
  2.3 & 0.4 \\
  1.7 & 0.4 \\
  0.2 & 1.9 \\
  0.2 & 1.6 \\
  0.9 & 1.6
  \end{bmatrix}
  $$

  $$
  M = \begin{bmatrix}
  2.1 & 1.2 & 2.2 & 0.0 \\
  0.4 & 0.2 & 1.7 & 2.5
  \end{bmatrix}
  $$

- We know $R$, and we want to generate $U$ and $M$
- What we do is we randomly create $U$ and $M$ first
- Then we do gradient descent on them. However, that is a non-convex problem, and it might not converge, we cant have that.
- So we do **Alternate** gradient, keep U fixed and optimize M, and vice versa. This way the problem is always convex and have a global optimum.
- Another readon we use ALS is we can compute in parellel when one matrix is fixed, because vectors in another matrix is independent from one another.

- Here is a simple version of ALS

  ```python
  import torch

  # Set the seed for reproducibility
  torch.manual_seed(42)

  # Constants
  num_users = 5
  num_items = 4
  num_latent_factors = 3
  lmbda = 0.1 # Regularization constant

  # Initialize user and item matrices with random values
  user_matrix = torch.rand(num_users, num_latent_factors)
  item_matrix = torch.rand(num_items, num_latent_factors)

  # Generate a random user-item matrix with values between 0 to 5
  ratings = torch.randint(6, (num_users, num_items)).float()

  # ALS algorithm
  for _ in range(10): # Run for 10 iterations
      # Fix item_matrix and solve for user_matrix
      for u in range(num_users):
          user_matrix[u] = torch.linalg.solve(
              item_matrix.T @ item_matrix + lmbda * torch.eye(num_latent_factors),
              item_matrix.T @ ratings[u].unsqueeze(-1)).T
      # Fix user_matrix and solve for item_matrix
      for i in range(num_items):
          item_matrix[i] = torch.linalg.solve(
              user_matrix.T @ user_matrix + lmbda * torch.eye(num_latent_factors),
              user_matrix.T @ ratings[:, i].unsqueeze(-1)).T

  # Make a prediction for the first user and the first item
  prediction = user_matrix[0, :] @ item_matrix[0, :]

  print(f"Original rating value: {ratings[0, 0]}")
  print(f"Predicted rating value: {prediction.item()}")
  '''
  Output:
  Original rating value: 3.0
  Predicted rating value: 2.514726400375366
  '''
  ```

### Why Do we use `linalg.solve` Here?

- We know that direct matrix calculation is support in pytorch
- The reason we wrap the calculation in `linalg.solve` is as follows:
- We want to solve $R = U \cdot I$ Lets say we keep $I$ fixed:
- The problem becomes convex $U = R \cdot I^{-1}$
- However, The inverse calculation is computationally expensive and also numerically unstable
- Instead we do it as if its $y = kx$ where we know $y$ and $x$ we just want to know $k$, as for how, we let `linalg.solve` to figure that out.
- Turns out `linalg.solve` is smart, instead of doing inverse, it uses LU decomposition to solve this problem.
- What is LU decomposition? I have no idea. And that is exactly why we ask `linalg.solve` to solve instead of manual solve.
