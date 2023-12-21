---
date: 2023-12-2
title: "How to succeed with a startup"
---

url: https://www.udemy.com/course/aws-machine-learning

## Data Engineering
### AWS S3
- Object Storage Service
- Data (Objects) are stored in Buckets
- Object are identified by a unique (within bucket) key (basically file name)
- Buckets' also have keys. They are unique across all of AWS S3.
- Max object size is 5TB
- For Machine Learning:
  - S3 is Backbone for many ML services (e.g. SageMaker)
  - create 'Data Lake' (infinite size, no provisioning)
  - Centralized Architecture
### AWS S3 Storage Classes
- File can be moved between classes using S3 Lifecycle configurations (or manually)
- Durability: All S3 classes have 99.999999999% (eleven-9s) durability
- Availability: differ between classes
- Different classes
  - S3 Standard - General Purpose
  - S3 Standard-Infrequent Access (IA)
  - S3 One Zone-Infrequent Access
  - S3 Glacier Instant Retrieval
  - S3 Glacier Flexible Retrieval
  - S3 Glacier Deep Archive
  - S3 Intelligent Tiering