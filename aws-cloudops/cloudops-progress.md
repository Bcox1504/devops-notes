# AWS CloudOps Cert Progress Tracker

> **Cert pivot:** AWS retired the SOA-C02 exam (SysOps Administrator – Associate) on Sept 29, 2025 and replaced it with the **AWS Certified CloudOps Engineer – Associate (SOA-C03)** exam — same associate-level cert, updated name and content outline (6 domains collapsed to 5, containers/CDK added). This folder now tracks SOA-C03. Domain breakdown below reflects the current SOA-C03 exam guide (checked July 2026).

## Domain Breakdown & Coverage

### Domain 1: Monitoring, Logging, Analysis, Remediation, and Performance Optimization — 22%
Covers CloudWatch (metrics, alarms, dashboards, agent), CloudTrail, EventBridge, Systems Manager Automation, and performance tuning for EC2/EBS/S3/RDS/EFS.

- **Notes so far:** none
- **Gap:** this is the largest domain and nothing is written yet — start here.

### Domain 2: Reliability and Business Continuity — 22%
Covers Auto Scaling, ElastiCache, RDS/Aurora replicas, ELB + Route 53 health checks, Multi-AZ, backup/restore (AWS Backup, snapshots, RTO/RPO), disaster recovery.

- **Notes so far:** none
- **Gap:** fully open.

### Domain 3: Deployment, Provisioning, and Automation — 22%
Covers AMIs/container images, CloudFormation, AWS CDK, StackSets, cross-account/cross-Region provisioning, deployment strategies (blue/green, rolling, canary), Systems Manager, Terraform/Git for IaC.

- **Notes so far:** [compute-services.md](compute-services.md) covers EC2 fundamentals (IaaS, shared responsibility) — a starting point for Task 3.1, but CloudFormation/CDK/deployment strategies aren't covered yet.

- **Gap:** CloudFormation, CDK, StackSets, deployment strategies, automation via Systems Manager.

### Domain 4: Security and Compliance — 16%
Covers IAM (MFA, roles, federated identity, policies), CloudTrail/IAM Access Analyzer auditing, multi-account strategies, Trusted Advisor, encryption at rest/in transit (KMS, ACM), Secrets Manager, Security Hub/GuardDuty/Config/Inspector.

- **Notes so far:** [cloudops-admin-overview.md](cloudops-admin-overview.md) briefly mentions "Security" under the Well-Architected Framework and "Managing user identity & access" under CloudOps engineer roles, but nothing IAM/KMS-specific yet.
- **Gap:** almost everything — IAM details, encryption, Trusted Advisor, GuardDuty/Security Hub.

### Domain 5: Networking and Content Delivery — 18%
Covers VPC (subnets, route tables, NACLs, security groups, gateways), private connectivity, WAF/Shield/Network Firewall, Route 53 + DNS, CloudFront, troubleshooting (VPC Flow Logs, hybrid connectivity).

- **Notes so far:** none
- **Gap:** fully open.

## Cross-Reference to Other Notes

- [homelab-vm-setup/general-notes.md](../homelab-vm-setup/general-notes.md) — hypervisor/VM concepts here reinforce the shared responsibility model in Domain 3, but doesn't map to AWS services directly.
- [linux-admin/](../linux-admin/) — guest-OS-level skills (permissions, users, systemctl) support Domain 1 (CloudWatch agent on instances) and Domain 3 (instance management), but files are still empty stubs.
- [github-ssh/](../github-ssh/) — Git/Terraform are explicitly in scope for Domain 3 (Skill 3.1.6), so once populated this folder is directly exam-relevant, not just a side project.

## Summary

| Domain | Weight | Status |
|---|---|---|
| 1. Monitoring, Logging, Analysis, Remediation & Perf. Optimization | 22% | Not started |
| 2. Reliability and Business Continuity | 22% | Not started |
| 3. Deployment, Provisioning, and Automation | 22% | Started (EC2 basics only) |
| 4. Security and Compliance | 16% | Barely started (glancing mentions only) |
| 5. Networking and Content Delivery | 18% | Not started |

Biggest gaps by weight: Domains 1 and 2 (22% each, nothing written) and Domain 5 (18%, nothing written). Domain 3 has the most groundwork but still needs CloudFormation/CDK/deployment strategy coverage.

Source: [AWS Certified CloudOps Engineer – Associate (SOA-C03) Exam Guide](https://d1.awsstatic.com/onedam/marketing-channels/website/aws/en_US/certification/approved/pdfs/docs-cloudops-associate/AWS-Certified-CloudOps-Engineer-Associate_Exam-Guide.pdf), [AWS Training blog: exam update and new name](https://aws.amazon.com/blogs/training-and-certification/exam-update-and-new-name-for-operations-certification/)
