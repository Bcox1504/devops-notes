# AWS Analytics Services

AWS offers a comprehensive suite of analytics services for use cases like real-time data streaming, big data processing, data warehousing, and visualization.

> **Exam note:** analytics isn't a named domain on the SOA-C03 exam guide the way monitoring/reliability/deployment/security/networking are — but knowing what these services actually do helps you rule out wrong answers on scenario questions (e.g., "which service ingests real-time clickstream data" isn't asking you to design a data pipeline, just to recognize Kinesis).

## Amazon Kinesis
Enables real-time data stream processing, with different components for different jobs:
- **Kinesis Data Streams** — the core stream, ingests real-time data (clickstream analysis, IoT telemetry) for custom processing
- **Kinesis Data Firehose** — the "easy" delivery option; automatically loads streaming data into S3, Redshift, OpenSearch, etc. with no custom consumer code needed
- **Kinesis Data Analytics** — run SQL or Apache Flink queries directly against a streaming data source
- **Kinesis Video Streams** — same idea, but for streaming video

## Amazon Athena
Serverless SQL querying directly on data sitting in S3 — no need to load it into a database first. Pairs naturally with S3 as the storage layer and Glue as the catalog.

## Amazon OpenSearch Service
> **Naming note:** formerly "Amazon Elasticsearch Service" — AWS renamed it in 2021 after forking Elasticsearch. If you see "Amazon ES" in older material, this is the same service.

Managed search and analytics engine — commonly used for log analytics, full-text search, and application monitoring dashboards.

## Amazon EMR (Elastic MapReduce)
Managed big data framework — runs Apache Spark, Hadoop, Hive, and other big-data tools on a managed cluster instead of you standing up and patching the servers yourself.

## Amazon QuickSight
Scalable business intelligence (BI) dashboards — the visualization layer on top of the data these other services collect/process.

## AWS Glue & AWS Lake Formation
- **AWS Glue** — serverless ETL (Extract, Transform, Load) service; also maintains the **Glue Data Catalog**, a central metadata store that Athena, Redshift Spectrum, and EMR can all point to
- **AWS Lake Formation** — builds on Glue to set up a secure data lake faster, with centralized permissions across the data in it

Together, these services help handle structured & unstructured data efficiently, enabling timely insights and scalable analytics in the cloud.

## Related Notes
- [database-services.md](database-services.md) — Amazon Redshift (data warehouse) and Redshift Spectrum, which query S3 data the same way Athena does
- [storage-services.md](storage-services.md) — S3, the storage layer most of these analytics services read from or write to
- Peripheral to [cloudops-progress.md](cloudops-progress.md) — not a named domain, but useful for eliminating wrong answers on scenario questions
