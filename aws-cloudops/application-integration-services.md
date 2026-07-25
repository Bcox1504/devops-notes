# AWS Application Integration Services

These services help decoupled, scalable, and flexible cloud apps talk to each other — especially useful in serverless and microservices environments.

## Amazon SQS (Simple Queue Service)
Provides managed message queues, two types:
- **Standard** — at-least-once delivery, best-effort ordering (a message could theoretically be delivered more than once, or slightly out of order)
- **FIFO** — exactly-once delivery, strict ordering (First-In-First-Out), but lower throughput than Standard

Great for decoupling components and scaling EC2 instances based on queue depth (e.g., Auto Scaling on `ApproximateNumberOfMessages`).

## Amazon SNS (Simple Notification Service)
A pub/sub messaging service that enables notifications to multiple subscribers — including other AWS services and users via email or SMS.
- Supports message filtering, so different subscribers only get the specific messages relevant to them
- Common pattern: **fan-out** — one SNS message triggers multiple SQS queues/Lambdas at once

## AWS Step Functions
Lets you orchestrate multiple Lambda functions (or other AWS services) into workflows using visual state machines — helps coordinate complex, multi-step processes with built-in error handling/retry logic instead of writing that glue code yourself.

## Amazon MQ
A managed message broker supporting standard messaging protocols like JMS and MQTT.
- Use this instead of SQS/SNS when you're migrating an existing app that already speaks one of these protocols and don't want to rewrite the messaging logic

## Amazon AppSync
Uses GraphQL to let applications query exactly the data they need from multiple sources in a single API call — simplifies API management vs. hitting several REST endpoints separately.

## Amazon AppFlow
Securely transfers and transforms data between SaaS applications (Salesforce, Slack, ServiceNow, etc.) and AWS services, on a schedule or triggered by events — no custom integration code needed.

> **Amazon EventBridge** (serverless event bus for connecting apps/SaaS to AWS services) is already covered in [monitoring-services.md](monitoring-services.md) under CloudWatch Events, since that's where it evolved from — check there instead of duplicating.

## Related Notes
- [compute-services.md](compute-services.md) — Lambda, the thing most of these services (SQS, SNS, Step Functions, EventBridge) trigger or orchestrate
- [monitoring-services.md](monitoring-services.md) — EventBridge, the event-routing piece of application integration
- Maps to [cloudops-progress.md](cloudops-progress.md) Domain 3 (Deployment, Provisioning, and Automation — decoupled/event-driven architectures)
