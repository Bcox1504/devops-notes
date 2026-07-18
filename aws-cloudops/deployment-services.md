# AWS Deployment Services

## Infrastructure as Code (IaC)
The process of managing & provisioning your servers, databases, CDNs, and other resources through machine-readable definition files.
- You only need to provide a text-based definition file that automatically provisions the required resources at the click of a button

## AWS CloudFormation
Primary IaC service. Provisions & manages your AWS resources using a custom code template in JSON or YAML format.
- Has a built-in graphical drag-and-drop tool called **CloudFormation Designer**
- **Change Set** — lets you see how your changes might impact running resources before you actually implement them
- **StackSet** — extends CloudFormation stacks by letting you create, update, or delete stacks across multiple accounts and AWS Regions in a single operation

## AWS Cloud Development Kit (CDK)
An open-source software development kit used to programmatically model AWS infrastructure using TypeScript, Python, Java, .NET, or any other supported language.

## AWS Serverless Application Model (SAM)
An open-source framework that simplifies the development of serverless apps in AWS.
- Commonly used for Lambda, DynamoDB, API Gateway, and other serverless services

## AWS Elastic Beanstalk
Lets you upload your app code to AWS and it provisions the required cloud environment for you, automatically.
- **Web Server Environment** — runs a static website, web app, or web API that serves HTTP requests
- **Worker Environment** — runs a worker app that processes long-running workloads on demand; also performs scheduled tasks and can integrate with an Amazon SQS queue
- Uses a config file to automatically deploy & configure your apps — these files are stored in the `.ebextensions` folder

## AWS CodeDeploy
Fully managed deployment service that automates your app deployments in AWS.
- **Does NOT create or provision AWS resources** — that's the key difference from CloudFormation

## Amazon ECS (Elastic Container Service)
A container orchestration service that supports Docker containers.
- Automates installing, operating, managing, networking, & scaling your cluster management infrastructure in AWS

## Amazon EKS (Elastic Kubernetes Service)
A fully managed orchestration service that supports Kubernetes containers.
- Automates installing, operating, managing, networking, & scaling your Kubernetes control plane, pods, and nodes in AWS

**AWS Outposts** — a physical server rack supplied by AWS but managed by you, for running Kubernetes on-premises.

**Amazon EKS Anywhere** — a deployment option that lets you create and operate Kubernetes clusters on your own infrastructure (on-prem, VMware vSphere, or bare metal) instead of in AWS, while still using the same EKS-consistent tooling and automation. Good fit when you need Kubernetes outside of AWS but still want a supported, standardized setup.

**EKS Distro** — the same open-source Kubernetes distribution AWS uses under the hood to build Amazon EKS clusters, packaged for you to run and manage yourself, anywhere. It's essentially the "engine" that EKS Anywhere is built on top of — gives you the certified Kubernetes binaries and dependencies without having to build, patch, and test them yourself.

## AWS OpsWorks
A configuration management service.
- Provides managed instances for your automation platforms, based on Chef and Puppet

## AWS Proton
A service that automates container & serverless deployment.
- Grants developers the freedom to innovate, but still within the guardrails the security team has set
- Offers a self-service portal for developers
- **Proton Templates** contain all the info required to deploy your custom environments & services

## Related Notes
- [compute-services.md](compute-services.md) — EC2, Lambda, and the container services (ECS/EKS/Fargate) this deployment tooling provisions and deploys onto
- Maps to [cloudops-progress.md](cloudops-progress.md) Domain 3 (Deployment, Provisioning, and Automation)
