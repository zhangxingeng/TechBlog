---
date: 2024-06-05
title: "Feature Engineering"
---

### Imputation of Missing Values
- Mean replacement: replace missing values with the mean of the column (generally not good)
- Dropping: if just a few missing values, drop the rows (never the best option)
- Machine Learning: KNN, Deep Learning, Regression (MICE: Multiple Imputation by Chained Equations)

### Unbalanced Data
- Oversampling, Undersampling
- Generate synthetic data
  - use KNN to generate synthetic data (SMOTE: Synthetic Minority Over-sampling Technique)
  - ADASYN (Adaptive Synthetic Sampling)
- Adjust the threshold of the model (but consider precision/recall tradeoff)

### Handle outliers
- Standard deviation
  - Standard deviation $\sigma$ is used to detect outliers
  - Data points beyond 1 standard deviation are considered outliers (since normal distribution is 1 standard deviation exactly)
  - box and whisker plot can be used to visualize outliers (or violin plot)
- Random Cut Forest
  - AWS use tree based algorithm to detect outliers

### Data Transformation
- Binning: Convert continuous data to categorical data
- Transforming: when have a data $x$, transform it to $x^2$, $\log(x)$ so your model can detect non-linear relationships from data
- Encoding: convert categorical data to numerical data

### Other stuff
- Normalization
- Shuffling
