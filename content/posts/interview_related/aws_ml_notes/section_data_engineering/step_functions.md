---
date: 2025-06-04
title: "Step Functions"
---

## Step Functions
- Orchestrate multiple services into a serverless workflow.
- Example: generate and clean dataset -> train model -> save model -> deploy model.

## AWS DataSync
- migrate data between on-premises storage and AWS storage (if DB then use DMS instead).
- On-Premise part: A Datasync Agent is deployed on-premises, which connects over internet / AWS-Direct-Connect to AWS.
- AWS part: data received by DataSync, it directs the data into S3.

## MQTT
- IoT standard messaging protocol.

## S3 Bucket policies vs Lifecycle policies