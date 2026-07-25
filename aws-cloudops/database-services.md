# AWS Database Services

## Amazon RDS (Relational Database Service)
- A relational database that's managed by both you (with limited access) and AWS
- The time-consuming tasks are handled by AWS — patching, backups, maintenance, hardware provisioning
- You can configure the underlying EC2 instance, and also get to decide the maintenance window
- For a single AZ, Amazon RDS is the primary DB. For a multi-AZ setup, you have a primary and a standby DB

## Amazon Aurora
- A database engine (that you can run on Amazon RDS) and a fully managed database service
- Compatible with MySQL and PostgreSQL
- Scales automatically, performs faster, and costs less than other DBs
- Automatically grows its storage
- Deployed as a DB cluster consisting of a primary DB and a read replica, similar to Multi-AZ deployments (RDS)
- **Single-master configuration** — apps can only write data to a single, master DB instance
- **Multi-master cluster** — all DB instances have read/write capability

Primarily used for **OLTP** (Online Transaction Processing) applications.

## Amazon Redshift
- A fully managed data warehouse
- Allows you to analyze all your data using standard SQL or through existing Business Intelligence tools
- Optimized to analyze relational data coming from transactional systems, business applications, and other sources for fast SQL queries
- Offers a concurrency scaling feature that supports virtually unlimited concurrent users and queries
- **Redshift Spectrum** — lets you query and retrieve structured and semi-structured data from files stored in Amazon S3 without having to manually load the data into Redshift tables
- Primarily used for **OLAP** (Online Analytical Processing) apps like data reporting and analytics

## The NoSQL Databases

### Amazon DynamoDB
- A fully managed NoSQL database service
- A non-relational database that doesn't have a rigid schema or extensive table relationships

### Amazon DocumentDB
- A fast, scalable, highly available MongoDB-compatible database service
- MongoDB = a document-oriented program that's cross-platform and a NoSQL database
- Each document contains fields and values in JSON format, with no rigid schema enforced

## In-Memory Databases

### Amazon ElastiCache
- A caching service that lets you set up, run, and scale open-source in-memory databases like Memcached or Redis
- Faster than disk-based databases
- Useful for database caching that eliminates unnecessary, frequent calls to the database just to return identical data sets
- Provides sub-millisecond latency, data partitioning, and can be integrated into apps with minimal code change

**2 types of engines you can launch:**

**Memcached**
- Based on the open-source Memcached in-memory data store
- Suitable for building a simple, scalable caching layer for data-intensive apps
- Lacks data replication capability
- **Does not:** support advanced data structures, or provide a highly available caching layer

**Redis**
- Based on the open-source Redis in-memory data store
- Provides: advanced data structures, pub/sub messaging, geospatial support, and point-in-time snapshot support
- Has a replication feature that provides high availability via data replication
- **Cluster Mode** can be enabled in Redis to have multiple primary nodes and replicas across two or more AZs

## Other DB Services

### Amazon Keyspaces
- A scalable, highly available, and managed Apache Cassandra-compatible DB service
- Designed for large amounts of data

### Amazon Neptune
- A fast, reliable, fully managed graph database service
- Makes it easy for you to build and run apps that work with highly connected DBs

### Amazon Timestream
- A fast, scalable, serverless time series DB service
- Primarily used for IoT and operational apps
- Tracks the changes of your data over time

### Amazon QLDB (Quantum Ledger Database)
- A fully managed ledger DB service
- Provides a transparent and immutable transaction log, owned by a central trusted authority
- Creates logs that are cryptographically verifiable
- Provides an auditable history of all changes made to your app data — can be used to track each and every app data change

## Related Notes
- [compute-services.md](compute-services.md) — EC2 underlies RDS deployments
- [storage-services.md](storage-services.md) — S3 backs Redshift Spectrum and AWS Backup
- Maps to [cloudops-progress.md](cloudops-progress.md) Domain 2 (Reliability & Business Continuity — RDS/Aurora replicas, ElastiCache)
