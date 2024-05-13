---
date: 2023-12-2
title: "AWS Storage Classes"
---

## Durability and availability
- 11-9s durability
- S3 standard: 99.99% availability
## S3 Storage (Checkings Account)
### S3 Standard - General Purpose
- frequently accessed data
### S3 Infrequent Access
- cost on retrieval
- 99.9% availability
- For backups
- Standard / One Zone
## S3 Glacier (Savings Account)
- Low cost for archiving
- 90 days minimum storage
### instant retrieval
- instant retrieval
### flexible retrieval
- minutes to hours retrival
### deep archive
- 12 hours retrieval

## S3 intelligent tiering
- auto tiering cost money

## Lifecycle on S3
- Use logic to move data between storage classes

## Handle deletion
- enable S3 versioning

## S3 Analytics
- analyze daily, help decide right storage class
