# AWS Audit and Compliance Services

## AWS CloudTrail
Primarily used for IT audits. Tracks user activity & API usage in your AWS account.
- Data is stored in an S3 bucket
- Enables risk auditing by continuously monitoring & logging account activities, such as user actions

**Management events** — provide info about the management operations performed on AWS resources.

**Data events** — provide info about the resource operations performed on or in AWS resources.

## AWS Artifact
Provides on-demand AWS security & compliance reports.

## AWS Security Hub
Provides a centralized & comprehensive view of the security posture of your cloud infrastructure across multiple AWS accounts.

Collects security alerts & findings from:
- **Amazon GuardDuty** — threat detection service that monitors for malicious activity
- **Amazon Inspector** — automated security assessments for vulnerabilities and deviations from best practices
- **Amazon Macie** — uses ML to discover and protect sensitive data (like PII) stored in S3
- **AWS IAM Access Analyzer** — identifies resources shared with external entities, helps spot unintended access
- **AWS Firewall Manager** — centrally configures & manages firewall rules across accounts and resources

## Related Notes
- [cloudops-admin-overview.md](cloudops-admin-overview.md) — Security perspective under the Well-Architected Framework and CAF
- [monitoring-services.md](monitoring-services.md) — CloudWatch, which handles system/performance monitoring alongside CloudTrail's account activity auditing
- Maps to [cloudops-progress.md](cloudops-progress.md) Domain 4 (Security and Compliance)
