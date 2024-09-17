---
date: 2024-06-05
title: "MapReduce and EMR"
---

## Elastic MapReduce (EMR)
- Managed Hadoop framework
- includes Spark, HBase, Presto, Flink, etc
- Charge by hour + EC2 Charges

### EMR Cluster
- Master Node: manages the cluster
- Core Node (at least 1): stores data and runs tasks
- Task Node: runs tasks only (only for computation, called spot instances)

### EMR usage
- can use spot instances to run temp tasks
- can use reserved instances for long-term tasks
- VPC, IAM, CloudWatch, S3 can integrate with EMR

### EMR Storage
- HDFS: Hadoop Distributed File System
- EMRFS: use S3 as if its HDFS
