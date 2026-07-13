# AWS Compute Services

Primarily VM servers that allow you to process data or host your applications

Can use serverless, which essentially puts your resources on a physical Amazon server rather than a cloud server 

## Amazon EC2 (Elastic Compute Cloud)
- Runs VMs in the cloud (Windows, Linux, or MacOS)
- Type of IaaS (Infrastructure as a Service)
- Basic building block for cloud architecture
- Used by other AWS services as an underlying compute service

Shared Responsibility:

AWS: Manages data centers, physical facilities, hardware components, host operating system, & virtualization layer

You: Responsible for guest OS, applying OS patches, setting up security access controls, & managing data

*Called EC2 because it's elastic, or, it's ability to be changed, resized, or customized at any given point in time*

*Also scales automatically, increasing or decreasing the number of running Amazon EC2 instances based on incoming traffic*

## Related Notes
- [homelab-vm-setup/general-notes.md](../homelab-vm-setup/general-notes.md) — local VM/hypervisor practice, useful for comparing on-prem VMs to EC2's shared responsibility model
- [linux-admin/](../linux-admin/) — guest OS management (patching, users, permissions) is the customer side of the EC2 shared responsibility model
- Maps to [cloudops-progress.md](cloudops-progress.md) Domain 1 (EC2 performance/optimization) and Domain 3 (provisioning)
