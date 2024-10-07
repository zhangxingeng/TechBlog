---
date: 2024-06-05
title: "Deep Learning on EC2"
---

### EMR (Elastic MapReduce)
- Notice EMR is not just map reduce despite the name, its a managed cluster system where your task is auto-scaling. You can totally run deep learning on it.
- support MXNet, TensorFlow, PyTorch, etc
- common GPU instances: P3: 8xV100, P2: 16xK80, G3: 4xM60, G5g: T4G (not available for EMR yet), P4d: latest A100, support UltraClusters for supercomputing (expensive)
- Trn1 instances: optimized for training LLMs. fast fabric ethernet for clusters.
- Trn1n instance: even faster fabric.
- Inf2 instances: Inferentia2 chips for ML inference

### AMI (Machine Images)
- virtual machine images for EC2, EMR, etc. There are special ones for deep learning


### Neural Net Tuning
- batch size: smaller batch means more "wiggly" learning, get out of local minima.

### Regularization
- prevent overfitting:
  - use simpler model
  - drop out
  - early stopping
  - L1 and L2 regularization (L1 is sparse)
  - Special Note: L1 tend to push less important weights to 0 (this is what sparse means, and also what feature selection means)
  - L1 is computationally inefficient: since its loss function is not differentiable at 0 (can be addressed by using L2 when close to 0 or using Subgradients)

### Gradient Related
- The vanishing gradient problem: stops learning for deep networks. (Exploding gradient similar but less common)
- Solution: LSTM, residual networks, a better activation function (like ReLU)

### Confusion Matrices
- Its True if prediction is correct. Positive is the prediction (binary thus positive). (if your prediction is cat you can call it True Cat for correctly predicting cat)
- Recall / Sensitivity: $predicted_cat_count / total_cat_count$ (what percent of cat is predicted correctly)
  - **Letting bad people get away is not tolerable**
  - Fraud: you want a high recall of fraud
  - $True_pos / (True_pos + False_neg)$: obviously this is to highlight False_neg (is cat but failed to predict cat)
- Precision: $predicted_cat_count / total_predicted_cat_count$
  - **Letting innocent people get accused is not tolerable**
  - Medical diagnosis: you want a high precision of cancer
  - $True_pos / (True_pos + False_pos)$: obviously this is to highlight False_pos (is not cancer but predicted cancer)
- F1 Score: $2 * (Precision * Recall) / (Precision + Recall)$
  - Harmonic mean of precision and recall: harmonic mean emphasizes the lower values which makes it a good metric, (Think a wood barrel's shortest plank)
  - RMSE: root mean square error

### ROC (Receiver Operating Characteristic) Curve
- False positive rate: $false_pos / (false_pos + true_neg)$
- Plot of recall vs false positive rate
- the more toward the top left the better
### AUC (area under the curve)
- the area under the ROC curve
- 0.5 is useless, 1 is perfect
### P-R Curve (Precision-Recall Curve)
- For large scale imbalanced data (ROC cant show the imbalance)
- Search another post regarding when P-R curve is better than ROC curve [](/posts/misc/roc_vs_pr_curve.md)
- 