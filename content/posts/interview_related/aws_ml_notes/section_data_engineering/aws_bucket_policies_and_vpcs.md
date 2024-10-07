---
date: 2024-06-02
title: "AWS Bucket Policies and VPCs"
---


# Bucket Policies


### Security of S3
- **User Based**: Which user can use which API calls (IAM policies)
- **Resource Based**: bucketwise rules (instead of user based)
- **permission granted if** IAM pass && bucket policy pass && no explicit DENY
- **Encryption**: obvious

### Bucket Policies (JSON file)
  - `Effect`: (`Allow` or `Deny`) - what current rule does
  - `Sid`: id for current rule (statement)
  - `Resource`: ARN (Amazon Resource Names) of the resource (e.g `arn:aws:s3:::mybucket/*`)
  - `Action`: APIs this rule applies to (e.g. `s3:GetObject`)
  - `Principal`: who this rule applies to (e.g. `*` for all users)
  - One Example:
    ```json
    {
      "Version": "2012-10-17",
      "Id": "PutObjPolicy",
      "Statement": [
        {
          "Sid": "DenyObjectsThatAreNotSSEKMS",
          "Effect": "Allow",
          "Principal": "*",
          "Action": "s3:GetObject",
          "Resource": "arn:aws:s3:::mybucket/*"
        }
      ]
    }
    ```
  - polices can be generated by AWS Policy Generator
  
### Object Encryption
- SSE (Sever-side Encryption)
  - SSE-S3: AWS auto encrypt, user care-free
  - SSE-KMS: AWS key management service, it generates and store keys but user can manage them
    - Requesting for keys cost money
  - SSE-C: (customer provide) User provides own keys
  - Client-side encryption: user encrypts before uploading
- enforce https in policy: `"Condition": {"Bool": {"aws:SecureTransport": "false"}}`
- enforce encryption in policy 
  - (enfoce KMS in example): `"Condition": {"StringNotEquals": {"s3:x-amz-server-side-encryption": "aws:kms"}}`
  - (enforce Customer side encryption): `"Condition": {"Null": {s3:x-amz-server-side-encryption-customer-algorithm": "true"}}`

### VPC Endpoints Gateway for S3
- default S3 is public (EC2 -> Internet -> S3)
- AWS Owns there own physical (fiber optics) network that connects their data centers
- Within these physical networks, each VPC have their own logical isolation so routing and security is guaranteed (data wont leak to other customers)
- VPC: create a private connection to S3

### Physical Structure of AWS Data Centers
- Network Devices: routers and switches are used for managing traffic, Load balancers also used for distributing traffic
- So what is VPC endpoint?
  - AWS still uses TCP/IP for routing, they just built virtual networks over it (using ENIs).
  - ENIs: Elastic Network Interfaces - they are private virtual IP addresses for VPCs
  - Control Plane: a centralized network controller, it manages routing tables to ensure secure routing
  - Instead of routing between IPs, VPC routes between ENIs. The algorithm for path-finding is also different to prevent data leaks
