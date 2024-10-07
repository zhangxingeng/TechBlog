---
date: 2024-06-05
title: "AWS Bucket Policies and VPCs"
---

### Athena
- Serverless query service
- can handle stuff like plain text or logs
- can work well with Glue (crawl to catalog then use athena to query, finally use quicksight to visualize)
- Pay-per TB scanned
- Columnar format (ORC, Parquet) saves money!
- Not for formatted reports (use quicksight for that)
- Not for ETL (use Glue for that)

### QuickSight
- Analytics & Visualization tool
- create nice dashboards or graphs or reports fast and at scale
- more of an app than a service
- Serverless
- Source: Athena, Redshift, Aurora, RDS, S3, etc, even files, anything.
- 'Machine Learning Insights': (use ML in QuickSight) detect anomalies, forecasting, etc
- QuickSight Q: answer questions with natural language (instead of `select * from`), addon
- Paginated reports: just pretty reports
- not for ETLs
- Security: Row level security, column level security (enterprise edition only)
- User Management: can use IAM or email sign-up, can do single sign-on, support MFA
- Pricing:  pay by / user / month (different editions different prices)

### QuickSight Visual Types
- AutoGraph: automatically choose the best graph for your data
- Bar Chart: for distribution
- Line Graph: change over time
- Scatter Plot, Heat map: correlation
