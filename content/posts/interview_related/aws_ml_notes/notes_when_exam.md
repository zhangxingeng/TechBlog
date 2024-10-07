---
date: 2024-06-05
title: "AWS Exam Notes"
---

### General Rules of AWS Exam
- Always find the simplest solution, use managed if can
- Always consider secure system by design (IAM, at rest and in transit encryption, shared responsibility model)


### SageMaker
- sagemaker pipe mode: used for efficient data streaming for training (like a cache)
  
### tf-idf
- tf-idf matrix: col: sentences (documents), row: unigram (unique words) bigram (unique 2 words from sentence)

### ML stuff
- reduce batch size means you need to also reduce learning rate, they are correlated
- Random Cut Forest: detect anomalies, not like random forest (classification)
- DeepAR: AutoRegression: for time series forecasting
- Have label, do classification, no label, do clustering
- Different models and their purpose
  - SVM with non-linear kernel: very good for non-linear boundaries (square shaped for example)
  - Logistic Regression: good for binary classification / regression but not good for non-linear boundaries
  - Perceptron with tanH: less capable than SVM, unless add layers
- seq2seq: for sequence to sequence translation, not used for typical language problems (use comprehend instead)
- 

### stats
- to evaluate a regression model use residual plot, evaluate classification model use confusion matrix
- 


### Security Stuff
- Defense in depth: data should be encrypted when in storage and in transit (use KMS to encrypt at S3 before transmit to SageMaker)
- shared responsibility model: AWS is responsible for security of the cloud, customer is responsible for security **within** the cloud


### Cloudwatch stuff
- Dashboard: monitoring latency, RAM usage CPU usage etc.


### Different DBs
- Athena: support SQL query
- DynamoDB: fro noSQL
- Amazon RDS: for SQL, supports wide variety of DB engines
- redshift: for structured data only, good at complex SQL queries


### Other Stuff
- ElastiCache: for im-RAM cache, like Redis

### Docker Stuff
- utilize GPU on EC2 instances: build the docker to be NVIDIA-Docker compatible -- gpu driver is used by reference to the host's driver



### Data Storage Stuff
- Multi-Node Redshift Cluster: for high-performance large volume data storage (and SQL querying)
-  Relational Database Service (RDS) vs redshift: RDS is row-based (thus good at transactional data, or OLTP), while redshift is columnar based, which is more efficient for bulk data analysis (OLAP)
-  you can have RDS for real time and sync to redshift for analytics. use pipeline or DMS (database mgment service) for sync
-  

### SageMaker Stuff
- 