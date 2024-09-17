---
date: 2025-06-01
title: "Begin"
---

## Scalability
- VPS: Virtual Private Server vs Shared Web Hosting
- Horizontal Scaling: Add more servers
- Vertical Scaling: Add more power to existing single server
- Load Balancer: Distribute traffic across multiple servers
  - DNS stores Load Balancer IP, load balancer redirects user to a picked server
- CAP theorem: Consistency, Availability, Partition Tolerance
  - Can only have 2 out of 3
  - Partition Tolerance: system continues to operate despite network failures
  - Consistency: all nodes have same data
  - Availability: all nodes can be accessed
- CP: bank where data error is not acceptable
- AP: social media where as long as the data is Eventually Consistent, it's fine
- Consistency Patterns:
  - Weak Consistency: data can get lost after write (streaming)
  - Eventual Consistency: data will be consistent eventually
  - Strong Consistency: data is consistent immediately (when transaction is done)
- Availability Patterns:
  - Failover: (active-active & active-passive) backup server takes over
  - Replication: data is copied to multiple servers
  - Load Balancer: distribute traffic
- CDN: Content Delivery Network
  - Caches data closer to user
  - Reduces latency
  - Protects against DDoS
  - Serves static content
- Reverse Proxy
- Sharding: split data into smaller parts

## ~~Database~~
- ACID:
  - Atomicity - Each transaction is all or nothing
  - Consistency - Any transaction will bring the database from one valid state to another
  - Isolation - Executing transactions concurrently has the same results as if the transactions were executed serially
  - Durability - Once a transaction has been committed, it will remain so

## When use NoSQL
- no complex queries like joins