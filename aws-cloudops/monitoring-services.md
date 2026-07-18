# AWS Monitoring Services

Monitoring is essential for managing IT infrastructure — it gives visibility into system health & performance, and helps detect & troubleshoot issues.

## Amazon CloudWatch
A metrics repository that collects system data from AWS services as well as your own custom metrics.
- Monitors & analyzes system metrics and notifies you if a certain threshold has been reached
- Can combine metrics across multiple resources
- Sends metrics to CloudWatch every 1 minute by default — for EC2 specifically, metrics are sent every 5 minutes by default

CloudWatch is really an umbrella term — it's made up of several sub-features that each handle a different job:

- **Dashboards** — a customizable home page in the console; build graphs and widgets out of metrics from multiple resources and regions into a single view
- **Metrics** — the raw time-series data points (CPU utilization, request count, etc.) everything else in CloudWatch is built on
- **Alarms** — watch a single metric and trigger an action (like an SNS notification or an Auto Scaling action) when it crosses a threshold over a set number of periods
- **Logs** — centralized storage for log data from EC2, Lambda, CloudTrail, and other services; supports retention settings and metric filters
- **Logs Insights** — an interactive query language for searching and analyzing the log data sitting in CloudWatch Logs
- **Events (Amazon EventBridge)** — a near real-time stream of events describing changes in your AWS resources; routes events to targets (like Lambda or SNS) based on rules. EventBridge is the newer, expanded version of the original CloudWatch Events, adding support for custom and third-party event buses
- **Synthetics (Canaries)** — configurable scripts that run on a schedule to monitor your endpoints and APIs the way a real customer would, so you catch issues before customers do
- **Container Insights** — collects, aggregates, and summarizes metrics/logs from containerized apps (ECS, EKS, Fargate)
- **Application Insights** — automatically sets up monitoring (metrics, logs, alarms) for common enterprise application frameworks running on AWS

## AWS Service Health Dashboard
Public dashboard that shows the status of all AWS services.

## AWS Personal Health Dashboard
Your account only — a personalized dashboard that shows the status of the AWS services YOU are using.

## AWS Health API
- Provides programmatic access to the AWS Health information that appears in the Personal Health Dashboard
- A RESTful web service — access it via HTTPS, returns a response in JSON
- Only available for Business or Enterprise support plans

## Related Notes
- [cloudops-admin-overview.md](cloudops-admin-overview.md) — AWS Support Plans (Business/Enterprise tiers, relevant to Health API access)
- [audit-compliance-services.md](audit-compliance-services.md) — CloudTrail, which handles account activity/API auditing alongside CloudWatch's system metrics
- Maps to [cloudops-progress.md](cloudops-progress.md) Domain 1 (Monitoring, Logging, Analysis, Remediation, and Performance Optimization)
