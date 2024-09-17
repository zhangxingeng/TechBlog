---
date: 2024-06-05
title: "Sagemaker Introduction"
---

### ML Workflow
1. Fetch, Clean, Prepare data 
2. Train and evaluate model
3. Deploy model, evaluate performance
4. back to 1.

### Typical ML Workflow
- Training Stage
  - -> S3 fetch training data
  - -> ECR fetch training code container
  - <> SageMaker train model
  - <- Save trained model to S3
- Deployment Stage
  - -> S3 fetch trained model
  - -> Fetch inference code container
  - <> EC2 / EKS deploy model for hosting

### Sagemaker Notebook
- use for data prep or prototyping
- Can use pre-built docker images ready for ML
- can spin up training jobs directly from notebook

### Sagemaker Data prep
- usually get data from S3
- can also ingest from Athena, EMR, Redshift, Amazon keyspace (Casandra)
- Can use Spark