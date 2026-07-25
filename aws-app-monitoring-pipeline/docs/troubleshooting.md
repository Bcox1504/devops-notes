# Troubleshooting postmortem: S3 export failures

## Symptom

Attempting to export CloudWatch Logs data to an S3 bucket via the console repeatedly failed with:

> Could not create export task. GetBucketAcl call on the given bucket failed. Please check if the specified Amazon S3 Bucket is in the same AWS region as CloudWatch Logs.

This error appeared regardless of which bucket was selected as the destination.

## What was ruled out first

The error message pointed at a region mismatch, but a straightforward reading of the setup didn't obviously support that — the bucket policy's service principal and `SourceArn` condition were both explicitly scoped to `us-east-2`, and the bucket itself was confirmed (via `aws s3api get-bucket-location`) to be in `us-east-2`.

Working through the usual suspects, each was checked and ruled out in turn:

1. **Bucket policy syntax** — an initial JSON syntax error (a missing closing quote on a key) was found and fixed, but the error persisted afterward.
2. **Bucket name / ARN mismatch** — confirmed the policy's `Resource` ARNs exactly matched the actual bucket name being used.
3. **Cross-account ownership** — `aws sts get-caller-identity` and the bucket's owner ID (via `get-bucket-acl`) both confirmed the same AWS account owned both the caller and the bucket.
4. **S3 Object Ownership / ACL settings** — confirmed "Bucket owner preferred" (ACLs enabled), which should support this export mechanism.
5. **Org-level SCPs** — ruled out; the account was not part of an AWS Organization.

At this point, every individually plausible cause had been checked and eliminated, and the bucket's own region was confirmed correct — which made the situation genuinely confusing.

## The breakthrough: CloudTrail

Rather than continuing to guess, CloudTrail's event history was used to find the *actual* API calls being rejected, since the console error message is generic boilerplate that doesn't reflect the true failure reason.

Every `GetBucketAcl` event found in CloudTrail, however, showed no `errorCode` at all — meaning every call being inspected had actually **succeeded**. This was the real clue: the calls being reviewed were manual CLI/console checks made by the account's root user, not the actual export attempt made by the CloudWatch Logs service on the user's behalf.

## Root cause

While investigating further, the CloudWatch Logs console was refreshed and the log group appeared to vanish entirely. Running:

```
aws logs describe-log-groups --region us-east-2
```

returned an empty list. Checking a different region:

```
aws logs describe-log-groups --region us-east-1
```

showed the log group present there instead.

**The log group had been living in `us-east-1` the entire time — not `us-east-2`.** The bucket, bucket policy, and every manual test had all been built around `us-east-2`, because that was the region the console happened to be defaulted to at the time. CloudWatch Logs export requires the log group and destination bucket to be in the *same* region, and the export task's request is made by the CloudWatch Logs service using that region's service principal (`logs.<region>.amazonaws.com`) — which never matched what the bucket policy allowed, because the policy was written for the wrong region from the start.

This also explains why every CloudTrail event inspected showed success: those were manual calls made against the *bucket's* actual region, which technically succeeded — while the *real* export request, made by the CloudWatch Logs service against a log group in a different region, was failing silently from a policy standpoint and never left a matching, easily-discoverable trail in the same search.

## Fix

1. Created a new S3 bucket in `us-east-1`, matching the log group's actual region.
2. Rewrote the bucket policy so both the `Principal.Service` and the `aws:SourceArn` condition referenced `us-east-1` instead of `us-east-2`.
3. Switched the AWS Console's active region selector to `us-east-1` before retrying the export.
4. The export succeeded on the first attempt afterward.

## Lessons learned

- **AWS's console error messages are a starting hypothesis, not a diagnosis.** "Check if it's in the same region" was technically the right direction, but pointed at the wrong resource (the bucket's region, which was fine) rather than the actual mismatch (the log group's region, which nothing had verified yet).
- **The AWS Console's region selector is a silent, global piece of state.** It's easy to be working across multiple regions without realizing it, especially when navigating between services that don't surface the active region prominently.
- **CloudTrail is only useful once you're looking at the right event.** Multiple CloudTrail entries looked relevant (same event name, same resource type) but were actually unrelated manual test calls. Distinguishing `userIdentity.type: Root` (a human/CLI call) from `userIdentity.type: AWSService` with an `invokedBy` field (a real service-to-service call) was the key to knowing whether a given event was even relevant.
- **When multiple layers each look individually correct, check whether they're all describing the same object.** Every component (bucket, policy, IAM, account) was internally consistent — they just weren't consistent *with each other*, because they silently referenced two different regions.
