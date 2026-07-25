# AWS Storage Services

## Block Storage

### Amazon EC2 Instance Store
- Temporary block-level storage
- Uses local disks/storage volumes physically attached to the underlying host computer of the EC2 instance
- Provides low-latency access to data
- **Loses its stored data if:** the underlying local storage fails, or the EC2 instance stops, hibernates, or terminates

### Amazon Elastic Block Store (EBS)
- Persistent block-level storage for EC2 — your data is still there even if you stop, restart, or terminate the instance (different from EC2 Instance Store)
- Called EBS volumes; mounted/attached to EC2 instances
- **Zonal in scope** — you can only attach a volume to an EC2 instance in the same AZ
- Can be encrypted at rest using AWS KMS
- Works with two kinds of underlying media, SSD or HDD, across 4 volume types:
  1. General Purpose SSD (1 instance at a time)
  2. Provisioned IOPS SSD
  3. Throughput Optimized HDD (1 instance at a time)
  4. Cold HDD (1 instance at a time)
- **EBS Multi-Attach** — lets you attach two or more Provisioned IOPS volumes to a single EC2 instance (must be Nitro-based instances)

## Object Storage

### Amazon S3 (Simple Storage Service)
- Object storage that's highly durable and scalable — can store virtually unlimited amounts of data
- Files are called "objects," uploaded to an S3 bucket
- Access files via a REST API call

**Storage classes:**
- S3 Standard — for frequently accessed data
- S3 Intelligent-Tiering — for changing or unknown access patterns
- S3 Standard-IA / S3 One Zone-IA (IA = Infrequent Access) — for storing long-lived but less frequently accessed data
- S3 Glacier / S3 Glacier Deep Archive — for low-cost, long-term storage and data archiving

**Other S3 features:**
- **Lifecycle Policy** — automatically transitions/moves data from one storage class to another
- **S3 ACL** (Access Control List) — secure access to your S3 buckets and objects
- **S3 Bucket Policy** — control external access to your S3 bucket
- **S3 Versioning + MFA** — prevent accidental data deletion in S3
- **CRR** (Cross Region Replication) — automatically replicates objects to a different AWS Region for backup purposes
- **Transfer Acceleration + Multipart Upload** — accelerate/expedite the data transfer (upload/download) of S3 objects

### Amazon S3 Glacier
- One of the storage classes in S3, but has its own web management console apart from S3
- Rarely accessed data = "cold." Frequently accessed data = "hot"
- Provides low-cost storage for data archiving and long-term backup
- Stored in a "vault"

**Deep Archive** — the cheapest storage type in AWS
- Minimum storage duration is 180 days, vs. 90 days for regular Glacier
- Objects deleted before these minimum periods incur a cost equal to the storage charge for the remaining days

**Disadvantage of Glacier:** takes a long time to retrieve archived data.

Archive retrieval options:

| Tier | S3 Glacier | Deep Archive |
|---|---|---|
| Expedited | 1–5 minutes | N/A |
| Standard | 3–5 hours | within 12 hours |
| Bulk | 5–12 hours | within 48 hours |

## Shared/Network File Storage

### Amazon EFS (Elastic File System)
- A scalable shared file storage solution, POSIX-compliant (Portable Operating System Interface)
- Can be simultaneously accessed by multiple Amazon Linux EC2 instances in different AZs
- Uses the NFS (Network File System) protocol, works as a file share
- **EFS only supports Linux servers** — must use Amazon FSx for Windows Server instead
- Storage class must be either EFS Standard or EFS Infrequent Access

### Amazon FSx for Lustre
- A scalable shared file storage service, identical to Amazon EFS
- "Lustre" refers to the open-source file system the service uses — Lustre = Linux Cluster, a parallel file system used for large-scale cluster computing
- Primarily used for High-Performance Computing (HPC), machine learning, or HPC applications
- For workloads that need high-performance parallel storage for frequently accessed ("hot") data
- Provides throughput of hundreds of gigabytes per second, offers millions of IOPS
- Can be mounted to instances or containers

### Amazon FSx for Windows File Server
- A fully managed Microsoft Windows file server service
- Uses the Server Message Block (SMB) protocol
- Can be integrated with your existing Microsoft AD or AWS Managed Microsoft AD
- Can be used as shared file storage for SharePoint, SQL Server DBs, Windows containers, or any other Windows-based app

## Backup & Hybrid Storage

### AWS Backup
- Fully managed backup service, automates your server and DB backup process
- 7-day retention period by default; max retention period is 35 days
- Can use AWS snapshots with retention set to 90 days, a year, or even longer

### AWS Storage Gateway
- A hybrid cloud storage service, connects your on-premises apps and data storage to the AWS Cloud
- Integrate local and cloud storage systems by using a gateway — a gateway is just a VM or hardware appliance running in your on-premises data center

**3 types:**
- **File Gateway** — store and retrieve objects in S3 using NFS and SMB; can be integrated with AD
- **Volume Gateway** — block storage to on-premises apps with low latency via the Internet Small Computer System Interface (iSCSI); uses S3 for point-in-time snapshots of your EBS volumes
- **Tape Gateway** — cloud-based Virtual Tape Library (VTL); uses S3 to back up tapes, can store archived tapes in Glacier or Deep Archive. On-premises apps connect to the tape gateway as iSCSI devices. Reduces cost by eliminating the use of physical backup tapes

## Related Notes
- [compute-services.md](compute-services.md) — EC2, the compute layer most of these storage services attach to or back up
- [database-services.md](database-services.md) — S3 is the backing store for Redshift Spectrum queries
- Maps to [cloudops-progress.md](cloudops-progress.md) Domain 2 (Reliability & Business Continuity — backup/restore, snapshots)
