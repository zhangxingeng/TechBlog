---
date: 2024-05-01
title: "Loss Functions Summary"
---
# Loss Functions Summary

### MSE vs Cross-Entropy
#### Mean Squared Error (MSE)
- Numerical - penalizes deviations more heavily than categorical, but help in achieving accurate continuous predictions. (better for regression)
- **Example:** Predicting house prices. 
- **Equation:** 
  \[
  \text{MSE} = \frac{1}{N} \sum_{i=1}^N (y_i - \hat{y}_i)^2
  \]

#### Cross-Entropy Loss
- Categorical - Cares less about deviations, good for discrete classes.
- , but help in achieving accurate discrete class predictions
- **Example:** Classifying emails as spam or not spam.
- **Equation:**
  \[
  \text{Cross-Entropy} = -\frac{1}{N} \sum_{i=1}^N \left[ y_i \log(\hat{y}_i) + (1 - y_i) \log(1 - \hat{y}_i) \right]
  \]
- Notice since prediction value is between 0 and 1, log would be negative converging from $-\infty$ to 0. Hence, the negative sign in the equation.

### Differences and Examples:

1. **Classification Task Example:**
   - **Problem:** Classify images of cats and dogs.
   - **MSE:** If MSE is used, it may penalize the predictions in an incompatible way, not capturing the essence of classification tasks where the output is categorical.
   - **Cross-Entropy:** Properly handles the probability distributions and penalizes wrong classifications more effectively.
   - **Outcome:** Cross-Entropy performs better as it aligns with the discrete nature of the output.

2. **Regression Task Example:**
   - **Problem:** Predict the temperature of a city.
   - **MSE:** Accurately penalizes the error in continuous predictions, making it suitable for regression.
   - **Cross-Entropy:** Inappropriately applies for continuous outputs, as it expects probabilities for discrete classes.
   - **Outcome:** MSE performs better as it matches the continuous nature of the output.

### Theoretical Basis:
Both MSE and Cross-Entropy can be derived from maximum likelihood estimation (MLE) with different assumptions:
- **MSE:** Assumes a Gaussian distribution of the dependent variable.
- **Cross-Entropy:** Assumes a Bernoulli distribution for binary classification or a categorical distribution for multi-class classification.

### Summary:
- **MSE:** Best for continuous output predictions in regression tasks.
- **Cross-Entropy:** Best for discrete class probability predictions in classification tasks.