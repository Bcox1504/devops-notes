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

## AWS Lambda
A serverless computing service
- Allows you to run code, a function, or an entire app without managing any servers
- Only pay for the compute time you actually used
- Uploaded code in AWS Lambda is called a **Lambda function** — can perform a custom task that you control or program, also highly scalable
- Fully managed by AWS, not you
- Languages supported include Java, Go, Ruby, Node.js, Python, and many others through the use of runtimes
- Runtimes are powered by Amazon EC2 Linux

## Orchestration

### AWS Batch
- Allows you to run batch computing workloads on the AWS Cloud
- Dynamically provisions the optimal quantity and type of compute resources, based on the volume and specific resource requirements
- Does the planning, scheduling, and execution of your batch computing workloads using Amazon EC2 instances

### AWS Elastic Beanstalk
- Automates the deployment, management, scaling, and monitoring of your custom apps in AWS
- Just upload your app and it will automatically handle the common tasks to run it
- Handles capacity provisioning, load balancing, database management, auto-scaling, and health monitoring
- Able to access these servers at any time

## Amazon Lightsail
- An easy-to-use Virtual Private Server (VPS)
- Has its own management console
- Provides other services like databases, load balancers, DNS records, and many more

## AWS Outposts
- A hybrid service that allows you to run AWS services, like Amazon EC2, in your on-premises data center

## AWS Container Services
A container emulates an application and not the entire OS — essentially a lightweight version of a VM.
- Commonly used for microservices architecture, in which you package an app along with its runtime dependencies
- Use either Docker or Kubernetes to create a container

### Amazon ECS (Elastic Container Service)
- A container orchestration service that supports Docker containers
- Allows you to easily install, operate, and scale your cluster management infrastructure in AWS
- Containers are defined in a **task definition**, which you use to run an ECS task, or are grouped together as an ECS service
- Run tasks using EC2 or AWS Fargate
- An IAM Role can be attached to your ECS task in the `TaskRoleArn` property of your task definition, for security control

### Amazon EKS (Elastic Kubernetes Service)
- A fully managed Kubernetes service
- Portable, extensible, open-source platform for managing containerized workloads and services
- Containers are grouped into **Pods** — the basic operational unit for Kubernetes
- Launches and orchestrates a cluster of compute resources using EC2 or Fargate
- Considered cloud-agnostic, as it allows you to easily move your workloads to your on-premises network or to other cloud service providers like Azure, GCP, etc.

### AWS Fargate
- A serverless compute engine that works with both ECS and EKS
- Allows you to focus on building your applications without worrying about server provisioning, scaling, and management
- Provides a more cost-effective solution than a container running on the EC2 launch type
- Runs each ECS task or Kubernetes pod in its own kernel, providing the tasks and pods their own isolated compute environment

### Amazon ECR (Elastic Container Registry)
- A fully managed Docker container registry
- Allows you to store, manage, and deploy Docker container images
- Integrated with ECS
- Stores Docker images in a highly available and scalable architecture
- Can use IAM to provide resource-level control of each repository

### AWS App2Container (A2C)
- A command-line tool
- Transforms .NET and Java apps into containerized apps
- Packages the app artifact and dependencies into container images
- Configures the network ports and generates the ECS task and Kubernetes pod definitions

### AWS Copilot
- Also a command-line tool
- Enables you to quickly launch and easily manage containerized apps on AWS
- Automates the deployment lifecycle of your containers

## Related Notes
- [homelab-vm-setup/general-notes.md](../homelab-vm-setup/general-notes.md) — local VM/hypervisor practice, useful for comparing on-prem VMs to EC2's shared responsibility model
- [linux-admin/](../linux-admin/) — guest OS management (patching, users, permissions) is the customer side of the EC2 shared responsibility model
- [storage-services.md](storage-services.md) and [database-services.md](database-services.md) — other AWS service categories from the same source material
- Maps to [cloudops-progress.md](cloudops-progress.md) Domain 1 (EC2 performance/optimization) and Domain 3 (provisioning, container services)
