---
date: 2025-06-04
title: "Glue"
---

### Glue Data Catalog & Crawlers
- Glue Data Catalog: A central metadata repository. You can search data needed wherever it is stored.
- crawler: find raw data anywhere, create their metadata, so you can query them in Athena or use them in ETL jobs.
- Data will go from a S3 to a database.
- crawler can also parse partitions and save them along with database.

### Glue ETL
- Glue ETL: transform data, clean data, enrich data, etc (before doing analysis)
- can use python or spark (scala)
- target can be S3, RDS, Redshift, or glue data catalog
- pay for resources used, serverless and scalable
- can use glue scheduler to schedule jobs, or use glue triggers to run on events
- For non-real-time pre-analysis.

### Glue DataBrew
- clean and normalize data without code
- Faster data prep
- save to S3 or Glue Data Catalog
- Can use Athena to query data after cleaning
