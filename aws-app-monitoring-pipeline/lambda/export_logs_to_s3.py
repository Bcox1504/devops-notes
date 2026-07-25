"""
Scheduled Lambda that exports the last 24 hours of a CloudWatch Logs
log group to an S3 bucket. Intended to run on a recurring EventBridge
schedule (e.g. every 12 hours) as the archival half of a log
monitoring pipeline.

Required IAM permissions (see docs/architecture.md):
  - logs:CreateExportTask
  - logs:DescribeExportTasks
  - logs:DescribeLogGroups
  - logs:CreateLogGroup / CreateLogStream / PutLogEvents on
    arn:aws:logs:<region>:<account-id>:log-group:/aws/lambda/*
    (for the Lambda's own execution logs)
"""

import boto3
import time
from datetime import datetime, timedelta

REGION = "us-east-1"
LOG_GROUP_NAME = "/sandbox/application-target"  # replace with your log group
BUCKET_NAME = "YOUR-BUCKET-NAME"                # replace with your bucket
DESTINATION_PREFIX = "scheduled-exports"
LOOKBACK_HOURS = 24


def lambda_handler(event, context):
    logs_client = boto3.client("logs", region_name=REGION)

    end_time = int(time.time() * 1000)
    start_time = int(
        (datetime.now() - timedelta(hours=LOOKBACK_HOURS)).timestamp() * 1000
    )

    response = logs_client.create_export_task(
        logGroupName=LOG_GROUP_NAME,
        fromTime=start_time,
        to=end_time,
        destination=BUCKET_NAME,
        destinationPrefix=DESTINATION_PREFIX,
    )

    print(f"Export task started: {response['taskId']}")
    return {
        "statusCode": 200,
        "body": f"Export task created: {response['taskId']}",
    }
