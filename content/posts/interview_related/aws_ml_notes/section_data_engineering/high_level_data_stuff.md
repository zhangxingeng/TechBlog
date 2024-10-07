---
date: 2025-06-05
title: "Data Stores & Data Pipeline"
---
## Understand At High Level Only
### Redshift
- Data Warehousing, can do SQL queries, for analytics
- **OLAP** (online Analytical Processing)
- need load from S3 or use Redshift Spectrum to query S3 directly

### RDS, Aurora
- RDS: row-based, can use SQL to query, just to store row data, not for analytics
- **OLTP** (online Transaction Processing)

### DynamoDB
- NoSQL, serverless, fully managed

### S3
- Object storage, unlimited storage

### OpenSearch (old name: ElasticSearch)
- indexing and search

### ElastiCache
- Caching mechanism, not really used for ML

## AWS Data Pipeline
- a EC2 instance is created automatically to run the pipeline
- Manage task dependencies, orchestrate and move data between different services
- do retries and notify on failure etc
- **Compared to Glue**: 
  - pipeline is just a box you can put anything in the EC2 instance.
  - Glue is managed and just for ETL using spark and nothing else.

## AWS Batch
- Run batch jobs as Docker images (clustering)
- serverless, pay for EC2s used by it
- Generic Batch oriented service, way wider than glue
- Your Docker image defines the job

## DMS (Database Migration Service)
- Migrate data from one database to another
- resilient and self-healing
- migration is hot (source db remains online)
- Support migrate between different db engines (e.g. MSSQL to Aurora)


