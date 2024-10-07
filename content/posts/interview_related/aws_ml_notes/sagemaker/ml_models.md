---
date: 2024-06-05
title: "Sagemaker ML Models"
---

### Linear Learner
- normalize and shuffle data
- train multiple model in parallel, most optimal is selected
- parameters:
  - `Balance_multiclass_weights`: bool, give each class equal importance
  - `Learning_rate`, `mini_batch_size`, `L1` (use L1), `Wd` (use weight decay / L2)
  - `target_precision`, `target_recall`: auto hold the value and maximize the other

### XGBoost
- eXtreme Gradient Boosting
  - chain of decision trees, fast and winning Kaggle
  - can classify well, but can also regress (regression trees)
  - Hyperparameters:
    - `Subsample`: prevent overfitting
    - `Eta`: step size shrinkage, prevent overfitting, 
    - `Gamma`: minimum loss reduction to create new tree split, larger = more conservative
    - `Alpha`: L1 regularization
    - `Lambda`: L2 regularization
    - `eval_metric`: optimize for this metric (AUC, error, rmse, etc)
    - `scale_pos_weight`: balance positive and negative weights
    - `max_depth`: max depth of tree, too high = overfitting
  - Instance Type: 
    - memory bound not compute-bound, M5 is good
    - New XGBoost use GPU, so P2, P3, G4dn, G5
    - Latest: can do distributed: set `use_dask_gpu_training=True`, set `fully_replicated=True` in `TrainingInput`.

### Seq2Seq
- Input RecordIO-protobuf format (tokens are ints)
- use pre-trained models
- use RNN and CNN with attention
- Prams:
  - `Batch_size`, `Learning_rate`, `Num_layers_encoder`, `Num_layers_decoder`
  - `Optimizer_type`: adam, sgd, rmsprop etc
  - Can optimize on Accuracy, BLEU, Perplexity (cross-entropy loss)
  - Use P3 cannot parallelize, but can use multiple GPUs on same machine

### DeepAR (Deep AutoRegressive)
- Forecasting, time series
- can find frequency and seasonality
- Use RNNs
- Input type: Json, parquet
- train over entire dataset, evaluate on last time points
- Train on multiple time series at once
- Params:
  - `Context_length`: how many time points to look back
  - other basic ML stuff
- CPU or GPU. 
  - Start with CPU: ml.c4.2xlargem 4xlarge first
  - move to gpu if needed (only help with large models / large mini-batch size)
  - Inference only CPU

### BlazingText
- Text classification (label sentences), word2vec(word embedding)

### Object2Vec
- General purpose converting objects to vectors
- typical params
- single machine only can use multiple GPUs

### Object Detection, Image Classification, Semantic Segmentation
- MXNet or TensorFlow
- params typical
- use GPU multi-GPU even multi-instance

### Random Cut forest
- Anomaly detection
- unsupervised

### Neural Topic Model
- Organize Documents into topics
- not just TF-IDF
- unsupervised

### LDA (Latent Dirichlet Allocation)
- similar to Neural Topic Model
- unsupervised clustering
- only cpu

### KNN (K-Nearest Neighbors)
- classification, regression
- supervised
- CPU or GPU

### K-means
- clustering unsupervised
- prefer CPU, if GPU only 1 is used

### PCA
- dimensionality reduction
- unsupervised
  
### Factorization Machines
- sparse data classification (e.g. recommender system)
- supervised
- CPU better

### IP Insights
- Find suspicious IP addresses


### Reinforcement Learning in SageMaker
- Q-learning
- can be distributed

### Automatic Model Tuning
- Hyperparameter optimization
- reduce range and parallel jobs to reduce cost

### Spark
- `sagemaker_pyspark` library let you use Spark in SageMaker
- `SageMakerEstimator`: KMeans, PCA, XGBoost, etc. (it will return a `SageMakerModel` object)

### SageMaker Studio
- user interface based on VSCode
- can use Jupyter notebooks (also share)
- SageMaker Experiments: track experiments and compare

### SageMaker Debugger
- Dashboard like tensorboard
- work with SageMaker Studio visually
- work with TensorFlow, PyTorch, MXNet, XGBoost, generic sagemaker estimator

### Autopilot
- AutoML: find a best model, and params for you

### Model Monitor
- get alerts on quality deviation via CloudWatch
- Visualize Data drift
- Detect outliers, new features
- no code
- work with Clarify for bias detection, and more explainability
- Data is stored in S3
  
### Deployment Safegards
- Deployment GuardRails: control shift from dev to prod
  - CanaryL shift a small portion of traffic to new model
  - Linear, all-at-once, etc
- support rollback
- Shadow test: compare performance of new model with old model

### SageMaker Canvas
- For business people no need to code

### Bias Metrics
- Class Imbalance(CI): underrepresented class
- Difference in Proportions of Labels(DPL): difference in proportion of labels
- KL Divergence and Jensen-Shannon Divergence: measure difference between two probability distributions
- LP norm: distance between two vectors
- Total Variation Distance(TVD): difference between two probability distributions
- Kolmorogov-Smirnov(KS) Test: test if two distributions are the same
- Conditional Demographic Disparity(CDD): difference in model performance across different demographic groups

### SageMaker Training Compiler
- Optimize for GPU faster training

### SageMaker Feature Store
- Features: here is just tabular data used for training

### ML Lineage Tracking
- 