# AWS CloudOps Cert Progress Tracker

> **Cert pivot:** AWS retired the SOA-C02 exam (SysOps Administrator – Associate) on Sept 29, 2025 and replaced it with the **AWS Certified CloudOps Engineer – Associate (SOA-C03)** exam — same associate-level cert, updated name and content outline (6 domains collapsed to 5, containers/CDK added). This folder now tracks SOA-C03. Domain breakdown below reflects the current SOA-C03 exam guide (checked July 2026).

## Domain Breakdown & Coverage

### Domain 1: Monitoring, Logging, Analysis, Remediation, and Performance Optimization — 22%
Covers CloudWatch (metrics, alarms, dashboards, agent), CloudTrail, EventBridge, Systems Manager Automation, and performance tuning for EC2/EBS/S3/RDS/EFS.

- **Notes so far:** [monitoring-services.md](monitoring-services.md) covers CloudWatch (dashboards, metrics, alarms, logs, logs insights, EventBridge/events, synthetics canaries, container/application insights), the AWS Service Health Dashboard, Personal Health Dashboard, and the Health API. [audit-compliance-services.md](audit-compliance-services.md) also covers CloudTrail (management vs. data events) from the audit angle. [management-governance-services.md](management-governance-services.md) now covers Systems Manager (Automation, Run Command, Patch Manager, State Manager, Session Manager, Parameter Store, Inventory) — closes the Systems Manager Automation gap.
- **Gap:** hands-on performance tuning for EC2/EBS/S3/RDS/EFS.

### Domain 2: Reliability and Business Continuity — 22%
Covers Auto Scaling, ElastiCache, RDS/Aurora replicas, ELB + Route 53 health checks, Multi-AZ, backup/restore (AWS Backup, snapshots, RTO/RPO), disaster recovery.

- **Notes so far:** [database-services.md](database-services.md) covers RDS Multi-AZ (primary/standby) and Aurora cluster replicas (single-master vs. multi-master), plus ElastiCache (Memcached vs. Redis, Redis Cluster Mode replication). [storage-services.md](storage-services.md) covers AWS Backup (retention periods, snapshots) and Storage Gateway.
- **Gap:** Auto Scaling, ELB + Route 53 health checks, RTO/RPO, disaster recovery strategies.

### Domain 3: Deployment, Provisioning, and Automation — 22%
Covers AMIs/container images, CloudFormation, AWS CDK, StackSets, cross-account/cross-Region provisioning, deployment strategies (blue/green, rolling, canary), Systems Manager, Terraform/Git for IaC.

- **Notes so far:** [compute-services.md](compute-services.md) covers EC2 fundamentals (IaaS, shared responsibility), Lambda, AWS Batch, Elastic Beanstalk, and container services (ECS, EKS, Fargate, ECR, App2Container, Copilot). [deployment-services.md](deployment-services.md) now covers IaC concepts, CloudFormation (Change Sets, StackSets), CDK, SAM, Elastic Beanstalk environments, CodeDeploy, ECS/EKS orchestration, EKS Anywhere/EKS Distro, Outposts, OpsWorks, and Proton. [management-governance-services.md](management-governance-services.md) covers AWS Organizations, Control Tower, and Service Catalog (multi-account/self-service provisioning), plus Systems Manager and Trusted Advisor. [application-integration-services.md](application-integration-services.md) and [transfer-migration-services.md](transfer-migration-services.md) cover decoupled/event-driven architecture pieces (SQS, SNS, Step Functions) and migration tooling (DMS, DataSync, Snow Family, Migration Hub).
- **Gap:** deployment strategies (blue/green, rolling, canary), Git/Terraform-based IaC (see [github-ssh/](../github-ssh/) once populated).

### Domain 4: Security and Compliance — 16%
Covers IAM (MFA, roles, federated identity, policies), CloudTrail/IAM Access Analyzer auditing, multi-account strategies, Trusted Advisor, encryption at rest/in transit (KMS, ACM), Secrets Manager, Security Hub/GuardDuty/Config/Inspector.

- **Notes so far:** [cloudops-admin-overview.md](cloudops-admin-overview.md) briefly mentions "Security" under the Well-Architected Framework and "Managing user identity & access" under CloudOps engineer roles. [audit-compliance-services.md](audit-compliance-services.md) now covers CloudTrail (management/data events), AWS Artifact, and Security Hub (GuardDuty, Inspector, Macie, IAM Access Analyzer, Firewall Manager). [identity-services.md](identity-services.md) now covers IAM in depth (users/groups/roles/policies, MFA, federated identity via STS, least privilege), AWS IAM Identity Center (formerly SSO), Cognito, and Directory Service. [security-services.md](security-services.md) covers KMS, CloudHSM, ACM, Secrets Manager, and Amazon Detective. [management-governance-services.md](management-governance-services.md) covers AWS Config, Trusted Advisor, and Organizations/Control Tower (multi-account strategies).
- **Gap:** none of the originally listed items — this domain's service-reference groundwork is now complete. Remaining work is scenario/procedural practice (applying these services to exam-style questions).

### Domain 5: Networking and Content Delivery — 18%
Covers VPC (subnets, route tables, NACLs, security groups, gateways), private connectivity, WAF/Shield/Network Firewall, Route 53 + DNS, CloudFront, troubleshooting (VPC Flow Logs, hybrid connectivity).

- **Notes so far:** [networking-services.md](networking-services.md) covers VPC, Elastic Load Balancing (ALB/NLB), Route 53, Global Accelerator, CloudFront, PrivateLink/VPN, Direct Connect, Transit Gateway, API Gateway, App Mesh, and Cloud Map. [security-services.md](security-services.md) now covers WAF, Shield, and Network Firewall. General (non-AWS) networking fundamentals — network types, MAC/IPv4/IPv6 addressing — now live in the separate top-level [../networking/](../networking/) folder, since that material isn't from the CloudOps course.
- **Gap:** subnets/route tables/NACLs/security groups detail, troubleshooting (VPC Flow Logs, hybrid connectivity).

## Cross-Reference to Other Notes

- [homelab-vm-setup/general-notes.md](../homelab-vm-setup/general-notes.md) — hypervisor/VM concepts here reinforce the shared responsibility model in Domain 3, but doesn't map to AWS services directly.
- [linux-admin/](../linux-admin/) — commands, filesystem hierarchy, and file permissions are filled in now; supports Domain 1 (CloudWatch agent on instances) and Domain 3 (instance management). `systemctl.md` and `users-and-groups.md` are still empty stubs.
- [github-ssh/](../github-ssh/) — Git/Terraform are explicitly in scope for Domain 3 (Skill 3.1.6), so once populated this folder is directly exam-relevant, not just a side project.
- [storage-services.md](storage-services.md) and [database-services.md](database-services.md) — service-reference notes covering the storage and database side of Domain 2.
- [monitoring-services.md](monitoring-services.md), [deployment-services.md](deployment-services.md), [audit-compliance-services.md](audit-compliance-services.md), [networking-services.md](networking-services.md) — service-reference notes covering Domains 1, 3, 4, and 5.
- [management-governance-services.md](management-governance-services.md), [identity-services.md](identity-services.md), [security-services.md](security-services.md) — closed out the remaining Domain 1/3/4/5 gaps (Systems Manager Automation, IAM depth, encryption, WAF/Shield, Trusted Advisor, AWS Config, multi-account strategies).
- [application-integration-services.md](application-integration-services.md), [transfer-migration-services.md](transfer-migration-services.md), [analytics-services.md](analytics-services.md), [machine-learning-services.md](machine-learning-services.md) — not tied to a specific exam domain, but useful general AWS service literacy for ruling out wrong answers on scenario questions.
- [../networking/](../networking/) — general (non-AWS) networking fundamentals: network types and MAC/IPv4/IPv6 addressing. Kept separate from this folder since it isn't CloudOps course material.
- [../challenges/](../challenges/) — hands-on practice write-ups (currently a Linux filesystem cleanup challenge) that reinforce concepts from [linux-admin/](../linux-admin/).

## Summary

| Domain | Weight | Status |
|---|---|---|
| 1. Monitoring, Logging, Analysis, Remediation & Perf. Optimization | 22% | Started (CloudWatch, Health dashboards/API, Systems Manager Automation covered; hands-on perf tuning still open) |
| 2. Reliability and Business Continuity | 22% | Started (backup/restore & DB reliability basics) |
| 3. Deployment, Provisioning, and Automation | 22% | Started (EC2, Lambda, containers, CloudFormation/CDK/SAM, Elastic Beanstalk, CodeDeploy, Organizations/Control Tower covered; deployment strategies & Git/Terraform IaC still open) |
| 4. Security and Compliance | 16% | Service-reference groundwork complete (CloudTrail, Artifact, Security Hub, IAM, MFA/federation, KMS/ACM/Secrets Manager, Trusted Advisor, AWS Config all covered) |
| 5. Networking and Content Delivery | 18% | Started (VPC, ELB, Route 53, CloudFront, Direct Connect, Transit Gateway, API Gateway, WAF/Shield/Network Firewall covered; NACLs/security groups detail, Flow Logs still open) |

Every domain now has service-reference groundwork, and Domain 4 is essentially done at the reference level. Remaining work across the board is the operational/procedural side: Auto Scaling & DR strategies (Domain 2), deployment strategies & Git/Terraform IaC (Domain 3), and NACL/security group depth (Domain 5).

Source: [AWS Certified CloudOps Engineer – Associate (SOA-C03) Exam Guide](https://d1.awsstatic.com/onedam/marketing-channels/website/aws/en_US/certification/approved/pdfs/docs-cloudops-associate/AWS-Certified-CloudOps-Engineer-Associate_Exam-Guide.pdf), [AWS Training blog: exam update and new name](https://aws.amazon.com/blogs/training-and-certification/exam-update-and-new-name-for-operations-certification/)
