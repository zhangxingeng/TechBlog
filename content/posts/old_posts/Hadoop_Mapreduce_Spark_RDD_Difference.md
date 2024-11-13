---
title: "Understanding Difference Between Hadoop MapReduce and Spark RDD"
date: 2023-05-04T23:30:52-04:00
author: "Xingeng Zhang"
draft: false
---

### What is HDFS

- HDFS is a distributed file system
- It stores and manages large datasets across many computers.
- It is the primary data storage layer in Hadoop clusters.
- HDFS stores by breaking files into smaller blocks and replicating them across multiple nodes in a cluster.
- HDFS is the storage system for Hadoop

### What is MapReduce

- a job typically consists of one or more Map tasks followed by one or more Reduce tasks.
- the Map and Reduce tasks are designed to work with data stored in HDFS or other distributed file systems, which requires reading the data from storage, processing it, and writing the results back to storage.

### Explain By Example: How do we do average with MapReduce

- The data is stored in HDFS, which means distributed
- First read the data from HDFS do a Map (parse string to float for example), write back to disk
- Again, data is large, cant fit in RAM
- Then, Read data from HDFS, do Reduce (get avg for example), write back to disk
- We notice that we have to think about storage all the time, this is tiring and complex

### What is RDD

- When a user creates an RDD, Spark automatically partitions the data into a set of smaller partitions, each of which can be processed independently on a different node in the cluster.
- Once the data is partitioned, Spark distributes the partitions across the nodes in the cluster, and each node processes the data in parallel using a functional programming paradigm.

### How to do average now with RDD

- just `s.map().reduce()` as if you are handling very small dataset
- RDDs provides abstraction that makes the data look like they are in memory, user dont have to care about read and write to HDFS after each computation.
- In reality, RDDs are doing the heavy lifting behind the scenes to handle the distributed storage and processing of data.

### Spark is Lazy

- Spark uses lazy evaluation
- the data procedure flow is first converted int a DAG
- then optimized to reduce repetitive computing
- for example, you do multiply by 2 first then divide by 10, spark would reduce that to divide by 10/2=5, saves time on IO, since big data only care about IOs
