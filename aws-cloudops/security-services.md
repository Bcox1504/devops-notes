# AWS Security Services

AWS offers a variety of security services to protect your cloud infrastructure & data. This note focuses on network protection, encryption, and secrets — for the account-auditing/threat-detection side (GuardDuty, Inspector, Macie, Security Hub), see [audit-compliance-services.md](audit-compliance-services.md) so this stuff isn't written out twice.

## Network & Edge Protection

### AWS WAF (Web Application Firewall)
Protects web apps from common exploits (SQL injection, cross-site scripting) by letting you define rules that filter incoming HTTP/HTTPS traffic. Sits in front of CloudFront, ALB, API Gateway, or AppSync.

### AWS Shield
DDoS protection.
- **Shield Standard** — automatically included for all AWS customers at no extra cost, protects against the most common network/transport layer attacks
- **Shield Advanced** — paid tier with enhanced detection, 24/7 access to the AWS DDoS Response Team (DRT), and cost protection for scaling during an attack

### AWS Network Firewall
A managed, stateful network firewall for your VPC — filters traffic at the VPC level (vs. WAF, which is app-layer). Useful for inspecting traffic going in/out of a VPC and between VPCs.

## Encryption & Key Management

### AWS KMS (Key Management Service)
A managed, multi-tenant service for creating and controlling encryption keys used to encrypt your data across AWS services (S3, EBS, RDS, etc.).
- Keys never leave KMS unencrypted — services call KMS to encrypt/decrypt rather than handling the raw key themselves

### AWS CloudHSM
Dedicated, single-tenant hardware security modules (HSMs) for managing your own encryption keys.
- Use this instead of KMS when you need full control of the hardware or have compliance requirements that don't allow a shared/multi-tenant key store

### AWS Certificate Manager (ACM)
Provisions, manages, and renews SSL/TLS certificates for use with AWS services (like CloudFront, ALB, API Gateway) — handles the renewal headache for you.

### AWS Secrets Manager
Securely stores and automatically rotates sensitive info like database passwords and API keys.
- Apps retrieve secrets at runtime via API call instead of hardcoding them
- Compare to [Systems Manager Parameter Store](management-governance-services.md): Parameter Store is free/cheaper and fine for general config + secrets, Secrets Manager costs more but adds automatic rotation — a common exam distinction

## Investigation

### Amazon Detective
Analyzes and visualizes security data to help you get to the root cause of a potential security issue — takes the findings from GuardDuty/Security Hub and helps you investigate *why* something happened, rather than just flagging that it happened.

> Amazon Macie, Amazon Inspector, and how these tie into Security Hub are already covered in [audit-compliance-services.md](audit-compliance-services.md) — check there instead of duplicating.

## Related Notes
- [audit-compliance-services.md](audit-compliance-services.md) — GuardDuty, Inspector, Macie, IAM Access Analyzer, Firewall Manager, and Security Hub (the detection/auditing side of AWS security)
- [identity-services.md](identity-services.md) — IAM, which controls who can access KMS keys and Secrets Manager secrets
- [networking-services.md](networking-services.md) — VPC, where Network Firewall and WAF actually sit
- Maps to [cloudops-progress.md](cloudops-progress.md) Domain 4 (encryption at rest/in transit — KMS, ACM, Secrets Manager) and Domain 5 (WAF/Shield/Network Firewall)
