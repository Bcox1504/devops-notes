# Overview of the course 

## Defining Cloud Computing
 On-demand delivery of compute, database storage, application, and other IT resources

## Features
- Instantaneous access
- Access resources where and when you want
-  More flexible and affordable than legacy IT infrastructure 
- Affordable for organizations and individuals with smaller budgets 

## What is a Hypervisor?
Software that links multiple hardware to use as one giant resources

*See [homelab-vm-setup/general-notes.md](../homelab-vm-setup/general-notes.md) for hands-on hypervisor practice (VirtualBox on the admin VM).*

## The AWS Well-Architectured Framework: 
1. Avoid unnecessary costs
    - Use only what you need
    - Reserve resources in advance
    - Continue to monitor for optimization
2. Reliability
    - Test disaster recovery settings
    - Incorporate redundancy
    - Have duplicate copies of resources 
3. Security
    - Best practices should be automated
    - Data should always be protected
    - Enable traceability
    - Manage access
4. Efficiency
    - Use computing resources to adjust to system requirements
    - Allow for more experimentation
    - Globalize changes in minutes
5. Operational Excellence
    - Document everything (like I am doing now)
    - Refine operational procedures
    - Anticipate failure
    - Update processes
    - Learn from failures

## AWS CAF or Cloud Adoption Framework
 - Best practices to help successful IT infrastructure migration to the cloud
 - Migrating to the cloud takes a lot of collaboration with different stakeholders
 - Provides recommendations for implementing, adopting, configuring, and maintaining effective workflows in the cloud

## Transformation Value Chain
- Technological Transformation: utilize cloud to migrate & modernize legacy infrastructure, apps, & data and analytics platforms
- Process Transformation: digitize, automate, and optimize business operations
- Organization Transformation: reimagine operational model, or how your business & tech teams work together to create customer value & meet strategic goals
- Product Transformation: reimagine the business model by creating new value propositions & revenue models 

# The 6 Cloud Perspectives
    Business Perspective
        - ensure that cloud investments accelerate digital transformation & business outcomes
    People Perspective
        - Create a culture of continuous growth & learning where change is embraced
    Governance Perspective
        - Maximize organizational benefits while minimizing cloud transformation related risks
    Platform Perspective
        - Build enterprise-grade, scalable, hybrid cloud platforms, implement cloud-native solutions, & modernize existing infrastructure
    Security Perspective
        - Achieve the confidentiality, integrity, and availability needs of cloud data and workloads
    Operations Perspective
        - Ensure that the cloud services delivered meet business needs

## The 4 Phases
1. Envision Phase: 
    Demonstrate how cloud adoption will help accelerate business outcomes & objectives
2. Align Phase:
    Identify capability gaps across the six CAF perspectives, identify cross-organization dependencies, & recognize stakeholder concerns
3. Launch Phase:
    Deliver pilot initiatives in production & demonstrate incremental business value before scaling to full production
4. Scale Phase:
    Expand pilots, scaling up to meet desired business needs while sustaining business benefits 


# Roles and Responsibilities of a CloudOps Engineer
1. Provisioning & managing cloud VMs
2. Maintaining backups for cloud resources
3. Automating logs & monitoring processes 
4. Monitoring billing and devoloping cost optimization strategies
5. Setting up cloud networks
6. Managing user identity & access
7. Fine-tuning cloud infrastructure systems based on automated monitoring results 

## The Exam Domains
- Monitoring, logging, & remediation
- Reliability & business continuity
- Deployment, provisioning, & automation 
- Security & compliance
- Networking & content delivery
- Cost & performance optimization

> **Note:** this domain list is from the old SOA-C02 exam (SysOps Administrator – Associate), which AWS retired on Sept 29, 2025 and replaced with **AWS Certified CloudOps Engineer – Associate (SOA-C03)** — the cert this repo is now tracking. SOA-C03 has a revised 5-domain breakdown (cost/performance folded into Domain 1). See [cloudops-progress.md](cloudops-progress.md) for the up-to-date domain list and progress tracking.

## AWS Support Plans
There are 5 support plans for AWS:
- Basic — free
- Developer — $
- Business — $$
- Enterprise On-Ramp — $$$
- Enterprise — $$$$

Cost optimization in general focuses on the ability to run your systems and deliver business value at the lowest price point possible. It's a continual process of improving your AWS workloads while minimizing costs to achieve the outcomes the business expects, in a cost-effective manner. Aims to increase revenue and maximize ROI.

*Maps to the Cost & Performance Optimization portion of Domain 1 — see [cloudops-progress.md](cloudops-progress.md).*