---
date: 2024-05-24
title: "AWS Cheatsheet for ML Interview"
---


## AWS and Bedrock Stuff

- Bedrock: hosting ML models only, serverless
  - Fully managed
  - offer FMs(foundations models) using API
- SageMaker: for training and fine-tuning models
  - Ground Truth: data labeling (auto or human)
- Amazon Lex (auto speech recoginition - ASR): for natural language understanding (NLU)
- Polly (TTS): for text to speech
- Amazon Comprehend (NLP): for sentiment analysis, identify features of text with contexts.
- DynamoDB (NoSQL DB) for storing session data.
- AWS Lambda
  - Event driven (on data change, or API Gateway etc)
  - Auto scaling
- AWS CloudWatch for logging
- Athena: SQL database
- AWS glue: Extract, Transform, Load (ETL) service, serverless, for data prep.
- Lambda: event driven, also serverless, for real time processing
- Retrival Augmented Generation (RAG): let LLM ask your database (the expert model) for answers
- Inf1 instances: for ML inference, use AWS Inferentia NPU chips, deploy using AWS Neuron SDK

## Different ML models
- Collaborative filtering for recommendation
- CNN, RNN for images
- RNN transformer for time series
- Graph data: GNN

## Data Processing
- Problem definition
- Creteria for success
- Data Structure
- Univariate analysis
  - Find distributions, plot for insights
  - categorical vs numerical
- Bivariate analysis
  - Z-test
  - T-test
  - Chi-square test
  - degree-of-freedom
  - p-value
- **Modeling**
- Evaluation
- Deployment
- 