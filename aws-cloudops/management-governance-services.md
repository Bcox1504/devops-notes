# AWS Management and Governance Services

AWS gives you multiple ways to manage cloud resources: the web-based **AWS Management Console**, the **AWS CLI** (command line), a **mobile app**, and **AWS Systems Manager** for visibility & control over both cloud and on-prem infrastructure.

## AWS Systems Manager
A collection of tools for operating your fleet of instances (EC2 and on-prem servers) at scale — this is the piece that fills the "Systems Manager Automation" gap for Domain 1 and Domain 3.

- **Automation** — runs pre-built or custom "runbooks" (documents) to patch, configure, or fix instances without you logging in manually. This is the actual "Automation" feature the exam guide references.
- **Run Command** — execute a command or script across many instances at once, no SSH/RDP needed
- **Patch Manager** — automates OS & software patching on a schedule
- **State Manager** — keeps instances in a defined, consistent state (e.g., make sure an agent is always installed and running)
- **Session Manager** — gives you a shell into an instance through the console/CLI, without opening SSH port 22 or managing key pairs
- **Parameter Store** — secure, hierarchical storage for config data and secrets (plaintext or encrypted with KMS); commonly pulled into scripts/Lambda instead of hardcoding values
- **Inventory** — collects metadata about your instances (installed apps, OS version, network config) for auditing

## AWS Config
Tracks and records configuration changes to your AWS resources over time.
- Answers "what changed, and when" — lets you see a timeline of a resource's config history
- Can evaluate resources against **Config Rules** (e.g., "flag any S3 bucket that isn't encrypted") for continuous compliance checking
- This is the main gap-filler for Domain 4's "AWS Config" callout

## AWS Organizations
Centrally manages and governs multiple AWS accounts.
- Lets you group accounts into **Organizational Units (OUs)** and apply **Service Control Policies (SCPs)** — guardrails that set the maximum permissions an account (even the root user) can have
- Enables **consolidated billing** — one bill across all accounts, and volume pricing discounts apply across the whole org

## AWS Control Tower
Automates the setup of a secure, multi-account AWS environment (a "landing zone") built on top of Organizations.
- Applies pre-built **guardrails** (mandatory or optional compliance rules) automatically to new accounts
- The easy button for "set up best-practice multi-account structure" instead of doing it by hand in Organizations

## AWS Service Catalog
Lets admins create a catalog of approved, pre-configured "products" (basically CloudFormation templates) that end users can self-service deploy — without needing to know the underlying infrastructure details or have broad IAM permissions.

## AWS Trusted Advisor
Automatically inspects your AWS environment and gives recommendations across 5 categories: cost optimization, performance, security, fault tolerance, and service limits.
- Basic/Developer support plans only get a handful of security & service-limit checks
- Full check list requires Business or Enterprise support — same tiering as the [AWS Health API](monitoring-services.md)

## AWS License Manager
Tracks software licenses (your own or AWS-provided) across accounts so you don't accidentally go over what you're licensed for.

## AWS Compute Optimizer
Uses ML to analyze your resource utilization (EC2, EBS, Lambda) and recommends right-sizing — e.g., "you're paying for an m5.xlarge but only using 10% of it, downsize to m5.large."

## Related Notes
- [deployment-services.md](deployment-services.md) — CloudFormation, the templating engine that Service Catalog products and Control Tower guardrails are often built on
- [monitoring-services.md](monitoring-services.md) — AWS Support plan tiers, which also gate Trusted Advisor's full check list
- [audit-compliance-services.md](audit-compliance-services.md) — Security Hub/GuardDuty/Config work alongside AWS Config for compliance visibility
- Maps to [cloudops-progress.md](cloudops-progress.md) Domain 1 (Systems Manager Automation) and Domain 4 (multi-account strategies, Trusted Advisor, AWS Config)
