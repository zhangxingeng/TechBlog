### Spark vs Hadoop
- Hadoop:
  - HDFS(Hadoop Distributed File System): Hadoop's storage layer
  - MapReduce: Hadoop's processing layer
  - Batch Processing: disk->cpu->disk, even intermediate results, higher latency. (but need less RAM)
  - use YARN(Yet Another Resource Negotiator) for resource management and job scheduling
- Spark:
  - RDD(Resilient Distributed Dataset): its a data structure, not storage (you read from storage and convert to RDD in memory)
  - DAG(Directed Acyclic Graph): Spark's processing layer
  - In-memory processing: temp data are in RAM, faster but need more RAM
  - Resource Manager: yield to other cluster managers like YARN, Mesos, Kubernetes

- Practical example -- doing a `data.map().reduce()` function with Spark and Hadoop:
- First, cluster manager: 
  - they read resources info from nodes, 
  - and create a plan based on the resource distributions (it does not run any code)
- Hadoop:
  - Notice when we talk about node's storage its always a part of the HDFS
  - input data is 
    - already stored in HDFS nodes.
    - divided into splits by Hadoop based on user specs, and 
    - assigned to map task's node, and YARN's Resource Manager distributed data a bit (but prioritize locality over overloading and underutilization)
    - nodes then run map task on whatever data they locally have
  - Map Phase: 
    - Each map task read from its node's storage, 
    - process its split of data, 
    - and save back to its node's storage
  - the intermediate data is 
    - shuffled and sorted by MapReduce to ensure same key in same node
  - Reduce Phase:
    - yarn Resource manager handles resource utilization and locality
    - then each node run the reduce task with whatever data they have locally
- Spark:
  - read and transform data from whatever into an RDD
  - Based on the source code, spark create a DAG from the transformations implemented first
  - Spark ask the cluster manager to make a plan based on current cluster status, 
  - spark execution engine handles data locality and execute the tasks based on the plan

### Spark Shuffling
- occasionally (like when you sort) nodes need to exchange data between partitions, that is shuffling


