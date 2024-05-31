---
date: 2024-05-24
title: "CI/CD/IaC Cheatsheet for ML Interview"
---

- CI: continous intergration: 
  - intergrate change to a shared repository
  - Tools: Github Actions, Kenkins, Azure DevOps
  - steps:
    - Code commit
    - Automated build
    - automated testing
    - feedback 
- CD: continous deployment: 
  - auto prep code for release
  - Tools: Jenkins, Azure DevOps
  - steps:
    - auto deploy to staging
    - run intergration tests
    - manual approval for production
- IaC: Infrastructure as Code
  - define infrastructure in code docker-compose.yml
  - Tools: CloudFormation, Terraform, Ansible
  - Best practices:
    - version control, config file
    - test before deployment
    - automated deployment

MLOps:
 - Model versioning
 - automated ML Pipeline
 - Steps:
    - Data collection
    - Data preprocessing
    - Model training
    - Model evaluation
    - Model deployment
    - Model monitoring
  
