# Architecture

## Overview

This pipeline has two independent paths that both originate from a single CloudWatch Logs log group:

1. A **real-time alerting path** that notifies an engineer within roughly a minute of a matching error being logged.
2. A **scheduled archival path** that exports logs to S3 every 12 hours regardless of whether any alarms fired.

## Real-time alerting path

### 1. Log group

Application logs are written to a CloudWatch Logs log group (e.g. `/sandbox/application-target`). This is the single source of truth that both paths read from.

### 2. Metric filter

A metric filter named `CriticalErrorCount` is attached to the log group with the filter pattern:

```
ERROR
```

Any log line containing the literal uppercase string `ERROR` anywhere in it matches. Each match emits a value of `1` to a custom CloudWatch metric:

- Namespace: `Sandbox/Application`
- Metric name: `AppErrorEvents`

### 3. CloudWatch alarm

An alarm (`Sandbox-Application-Error-Alarm`) watches the `AppErrorEvents` metric with these settings:

- Statistic: Sum
- Period: 1 minute
- Threshold: `AppErrorEvents >= 1`
- Datapoints to alarm: 1 out of 1 (fires on a single match, no repeated breaches required)

When the threshold is breached, the alarm transitions from `OK` (or `INSUFFICIENT_DATA`) to `ALARM`.

### 4. SNS notification

The alarm's action is configured to publish to an SNS topic with an email subscription. On alarm state change, subscribers receive an email notification within roughly a minute.

## Scheduled archival path

### 1. EventBridge schedule

An EventBridge rule triggers a Lambda function on a fixed interval:

```
rate(12 hours)
```

### 2. Lambda function

The Lambda (`ExportLogsToS3`, see [`lambda/export_logs_to_s3.py`](../lambda/export_logs_to_s3.py)) calls the CloudWatch Logs `create_export_task` API each time it runs, exporting the **last 24 hours** of logs from the log group to the destination S3 bucket, under the `scheduled-exports/` prefix.

The 24-hour lookback combined with a 12-hour schedule means every run overlaps with the previous one, so a missed or delayed run doesn't create a gap in archived data.

### 3. IAM role

The Lambda's execution role grants only:

- `logs:CreateExportTask`, `logs:DescribeExportTasks`, `logs:DescribeLogGroups` — required to start and check on export tasks
- `logs:CreateLogGroup`, `logs:CreateLogStream`, `logs:PutLogEvents` scoped to `/aws/lambda/*` — required for the Lambda's own execution logging only

### 4. S3 bucket policy

The destination S3 bucket has a resource policy (see [`policies/s3-bucket-policy.json`](../policies/s3-bucket-policy.json)) granting the CloudWatch Logs service principal for the relevant region permission to:

- `s3:GetBucketAcl` on the bucket
- `s3:PutObject` on objects in the bucket, conditioned on the request's `aws:SourceArn` matching the log group's ARN

**Important:** the service principal (`logs.<region>.amazonaws.com`) and the `aws:SourceArn` condition must reference the *same region* the log group actually lives in. See [`troubleshooting.md`](troubleshooting.md) for what happens when they don't.

## Setup steps

1. Create (or identify) the CloudWatch Logs log group and confirm its region.
2. Create an S3 bucket in the **same region** as the log group.
3. Apply the bucket policy from `policies/s3-bucket-policy.json`, substituting your bucket name, account ID, and region.
4. Create the metric filter and custom metric on the log group.
5. Create the CloudWatch alarm on that metric, with an SNS topic as its action.
6. Subscribe an email address to the SNS topic and confirm the subscription.
7. Create the IAM role for Lambda with the scoped permissions above.
8. Deploy the Lambda function using `lambda/export_logs_to_s3.py`, with the role attached.
9. Add an EventBridge trigger to the Lambda on a `rate(12 hours)` schedule.
10. Test end-to-end (see below) before relying on it.

## Testing end-to-end

1. Push a test log event containing `ERROR` into the log group.
2. Confirm the `AppErrorEvents` metric increments in CloudWatch Metrics.
3. Confirm the alarm transitions to `ALARM`.
4. Confirm the SNS email arrives.
5. Manually invoke the Lambda (or wait for its schedule) and confirm a new object appears in the S3 bucket under `scheduled-exports/`.
