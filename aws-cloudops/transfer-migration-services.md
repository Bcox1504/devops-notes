# AWS Transfer & Migration Services

AWS offers both online and offline options for getting data and workloads from on-prem into AWS.

## Online Data Transfer

### AWS DataSync
Automates online data transfers between on-prem storage (or other clouds) and AWS storage services (S3, EFS, FSx) — handles scheduling, encryption in transit, and validation for you.

### AWS Transfer Family
Fully managed file transfers straight into S3 or EFS using SFTP, FTPS, or FTP — useful when you have partners/clients who need to keep uploading via those legacy protocols and can't just switch to an API or the console.

## Offline Data Transfer (Snow Family)
For when your data set is too large (or your bandwidth too limited) to move over the network in a reasonable time.
- **AWS Snowcone** — smallest device, for small-scale edge/offline transfer (a few TB)
- **AWS Snowball** — a physical, ruggedized storage device AWS ships you; you load your data onto it and ship it back (tens of TB range)
- **AWS Snowmobile** — a literal shipping container on a truck, for exabyte-scale migrations

> **Exam tip:** the general rule of thumb is bandwidth vs. data size — if it would take weeks to upload over your internet connection, that's your cue to reach for the Snow Family instead of DataSync.

## Migration Services
For assessing and moving whole environments/workloads, not just data.

- **AWS Application Discovery Service** — scans and inventories your on-prem environment (servers, dependencies, utilization) before you migrate, so you know what you're actually moving
- **AWS Database Migration Service (DMS)** — migrates databases to AWS with minimal downtime; can migrate between the same engine (e.g., MySQL to MySQL) or different engines (e.g., Oracle to Aurora) when paired with the **Schema Conversion Tool (SCT)**
- **AWS Server Migration Service (SMS, now part of Application Migration Service)** — migrates on-prem servers to AWS as EC2 instances without needing an agent on every box
- **AWS Migration Hub** — a single place to track migration progress across multiple AWS and partner migration tools
- **AWS Migration Evaluator** — helps build the business case before you migrate; analyzes current on-prem costs/usage to project what it'll cost to run in AWS

These services help efficiently move and manage data and workloads between on-prem environments and AWS, addressing different scales and connectivity scenarios.

## Related Notes
- [storage-services.md](storage-services.md) — S3/EFS/FSx, the usual landing spots for DataSync and Transfer Family
- [database-services.md](database-services.md) — RDS/Aurora, common DMS migration targets
- Maps to [cloudops-progress.md](cloudops-progress.md) Domain 3 (Deployment, Provisioning, and Automation — cross-account/cross-Region provisioning and migration planning)
