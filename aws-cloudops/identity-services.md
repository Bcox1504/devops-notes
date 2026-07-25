# AWS Identity Services

These services help securely manage user identities, permissions, & access across AWS and hybrid environments. This is the big gap-filler for Domain 4 ("IAM details — MFA, roles, federated identity, policies").

## IAM (Identity and Access Management)
The core service to create users, groups, roles, and policies to control access to AWS resources.
- **Users** — an individual identity (person or app) with long-term credentials
- **Groups** — a way to attach the same permissions to a bunch of users at once
- **Roles** — a set of permissions that can be *assumed* temporarily (by a user, an AWS service, or an external identity) — no long-term credentials attached, which is why roles are the recommended way to give EC2/Lambda/etc. access to other AWS resources
- **Policies** — JSON documents that define what's allowed/denied. Can be attached to users, groups, or roles
  - **Identity-based policies** — attached to the user/group/role itself
  - **Resource-based policies** — attached to the resource (e.g., an S3 bucket policy), defines who can access *that resource*
- **MFA (Multi-Factor Authentication)** — requires a second factor (virtual/hardware token, SMS) in addition to a password; strongly recommended for the root user and any privileged IAM user
- **Federated identity** — lets users sign in with an existing identity (corporate AD, Google, Facebook, SAML 2.0, or OIDC provider) instead of creating a separate IAM user; the user gets temporary credentials via **AWS STS (Security Token Service)**
- **Principle of least privilege** — a user/role should only have the exact permissions needed to do its job, nothing more — this shows up constantly on the exam as the "correct" answer to access-control scenario questions

## AWS IAM Identity Center (formerly AWS SSO)
> **Naming note:** AWS renamed "AWS Single Sign-On (AWS SSO)" to **AWS IAM Identity Center** back in 2022 — same service, don't confuse the old name with the new one if you see "AWS SSO" in older material.

Allows users to log in once to access multiple AWS accounts and business applications (like Salesforce, Box, Microsoft 365), instead of juggling separate credentials for each.

## Amazon Cognito
Enables user sign-up, sign-in, and access control for web and mobile apps — this is for *your app's end users*, not for managing your AWS account access (that's IAM's job).
- Supports social identity providers (Google, Facebook, Apple) and enterprise identity providers (SAML, OIDC)
- **User Pools** — a user directory for sign-up/sign-in
- **Identity Pools** — grants temporary AWS credentials to your app's users so they can access AWS resources directly (e.g., upload to S3 from a mobile app)

## AWS Directory Service
Provides a managed Microsoft Active Directory in the cloud, simplifying integration with existing on-prem AD and improving security & management.
- Useful when you need to extend an existing corporate AD into AWS, or need AD for Windows-based workloads (like [Amazon FSx for Windows File Server](storage-services.md))

## Related Notes
- [security-services.md](security-services.md) — KMS/Secrets Manager, which IAM policies commonly gate access to
- [audit-compliance-services.md](audit-compliance-services.md) — IAM Access Analyzer, which flags unintended external access granted through IAM/resource policies
- [storage-services.md](storage-services.md) — FSx for Windows File Server, which integrates with AWS Directory Service / on-prem AD
- Maps to [cloudops-progress.md](cloudops-progress.md) Domain 4 (Security and Compliance — IAM, MFA, federated identity, policies)
