# Terraform Basics

Intro notes from learning Terraform — what it is, HCL, providers, resources, the init/plan/apply/destroy workflow, and state. Terraform is also in scope for the CloudOps exam (Domain 3, Skill 3.1.6 — Git/Terraform for IaC), so this ties into [aws-cloudops/cloudops-progress.md](../aws-cloudops/cloudops-progress.md).

## What is Terraform?
**Terraform:** "an Infrastructure as Code (IaC) tool developed by HashiCorp that allows you to provision and manage infrastructure using configuration files instead of manually creating resources."

So instead of clicking through the AWS Console to launch an EC2 instance, you just write the instance out in a config file and let Terraform build it.

### Declarative vs. imperative
Terraform is **declarative**, "meaning you describe the infrastructure you want, and Terraform determines the actions needed to achieve that desired state."

| Style | What it means |
|---|---|
| Imperative | "Specify the individual steps required to accomplish a task." |
| Declarative | "Specify the desired outcome and let the tool determine the necessary actions." |

Example — rather than building an EC2 instance by hand, you declare it:

```hcl
resource "aws_instance" "web_server" {
    ami           = "ami-123456"
    instance_type = "t3.micro"
}
```

> The AMI ID here is just a made-up example, not a real image you can deploy.

## HCL (HashiCorp Configuration Language)
**HCL** stands for HashiCorp Configuration Language — "the configuration language commonly used to write Terraform files."

Easy way to keep them straight:

| Term | What it is |
|---|---|
| Terraform | The Infrastructure as Code tool |
| HCL | The language used to describe infrastructure configurations |
| `.tf` | The file extension used for Terraform config files written in HCL |

HCL uses **blocks, arguments, and values**. General shape:

```hcl
resource "RESOURCE_TYPE" "LOCAL_NAME" {
    argument = "value"
}
```

The arguments inside the block are what actually configure the resource.

## Providers
**Provider:** "a plugin that allows Terraform to interact with a particular platform, service, or API."

Terraform can't do anything without providers. Common ones: AWS, Microsoft Azure, Google Cloud, Kubernetes, GitHub.

### Declaring vs. configuring a provider
These are two different blocks and it's easy to mix them up:

**Declaring** (tells Terraform the project needs the AWS provider):
```hcl
terraform {
    required_providers {
        aws = {
            source = "hashicorp/aws"
        }
    }
}
```

**Configuring** (tells the provider how to behave — here, use US East (Ohio)):
```hcl
provider "aws" {
    region = "us-east-2"
}
```

- `required_providers` = which provider dependencies Terraform needs
- `provider` = how that provider operates
- Neither one creates any infrastructure by itself

> AWS credentials have to be set up before Terraform can touch AWS. **Don't hardcode access keys or secrets in `.tf` files.**

## Resources
**Resource:** "an infrastructure object that Terraform manages." Examples: EC2 instances, S3 buckets, VPCs, security groups, subnets.

```hcl
resource "aws_instance" "web_server" {
    ami           = "ami-123456"
    instance_type = "t3.micro"
}
```

| Piece | Meaning |
|---|---|
| `resource` | Declares a managed resource |
| `aws_instance` | Resource type: AWS EC2 instance |
| `web_server` | Local name Terraform uses to reference the resource |
| `ami` | Amazon Machine Image used to launch the instance |
| `instance_type` | EC2 instance size/type |

### Referencing a resource
- The resource itself: `aws_instance.web_server`
- Its instance ID: `aws_instance.web_server.id`

This is how you plug one resource's attributes into another part of the config.

## Arguments
**Arguments:** "settings inside Terraform blocks that define how something should be configured." Format is always `argument = value`.

```hcl
resource "aws_instance" "dev_server" {
    ami           = "ami-123456"
    instance_type = "t3.small"
}
```

`ami` picks the machine image, `instance_type` picks the size.

### Quick AMI refresher
**AMI** = Amazon Machine Image — "a template used to launch EC2 instances." Can be Amazon Linux, Ubuntu, Windows Server, etc. AMI IDs are specific to AWS regions and images, so an ID from one region won't necessarily work in another. More on EC2/AMIs in [aws-cloudops/compute-services.md](../aws-cloudops/compute-services.md).

## Terraform local names vs. AWS names
The Terraform local name is **not** necessarily what shows up in the AWS Console.

```hcl
resource "aws_instance" "web_server" {
    ami           = "ami-123456"
    instance_type = "t3.micro"

    tags = {
        Name = "Development-Web-Server"
    }
}
```

- Terraform local name: `aws_instance.web_server` → what Terraform uses to reference it
- AWS `Name` tag: `Development-Web-Server` → metadata AWS uses to show a friendly name in the console

### Tags
**Tags:** "key-value pairs used to organize and identify AWS resources."

```hcl
tags = {
    Name        = "Dev-Linux-01"
    Environment = "Development"
    Department  = "IT"
    Owner       = "Infrastructure"
}
```

Useful for: resource organization, cost allocation, identifying ownership, filtering/reporting, automation.

> Setting `Environment = "Development"` doesn't actually set up a dev environment — it's just a label.

## The Terraform workflow
```
terraform init  →  terraform plan  →  terraform apply  →  terraform destroy
```

| Command | Purpose |
|---|---|
| `terraform init` | Prepare the project |
| `terraform plan` | Preview changes |
| `terraform apply` | Execute changes |
| `terraform destroy` | Remove managed infrastructure |

### `terraform init`
Initializes a Terraform working directory — installs the required providers and modules and initializes the backend. Run it when starting a new project, or when dependencies/backend settings change.

### `terraform plan`
Previews proposed changes by comparing your config against the managed infrastructure and state. **Doesn't actually change anything.**

Example output:
```
Plan: 1 to add, 0 to change, 0 to destroy.
```
- 1 to add → one resource will be created
- 0 to change → nothing existing gets modified
- 0 to destroy → nothing gets deleted

### `terraform apply`
Actually makes the changes. It generates a plan, shows you what it's going to do, and normally asks for confirmation before talking to the provider APIs to create/update/delete stuff. You can also apply a previously saved plan file.

### `terraform destroy`
Removes the infrastructure managed by the current config and state. It shows what it's going to delete and normally asks for confirmation.

> **Always review a destroy plan carefully**, especially on company or production infrastructure.

## Terraform state
**Terraform state:** "Terraform's record of the infrastructure resources it manages."

With local state it usually lives in `terraform.tfstate`. State is how Terraform links what's in your `.tf` files to the real stuff in AWS — e.g. it records that `aws_instance.web_server` is actually EC2 instance `i-0a12b34c56d78e90f`.

### The three-way mental model (most important part)
| Concept | Means |
|---|---|
| **Configuration** | What I want (your `.tf` files) |
| **State** | What Terraform manages (tracked resources, IDs, attributes) |
| **Infrastructure** | What actually exists (the real resources in AWS) |

Terraform works to reconcile the differences between them.

### Why state matters
Say Terraform created an instance with `instance_type = "t3.micro"` and you change it to `"t3.small"`. Because of state, Terraform knows *which* existing instance to update instead of spinning up a new one.

### What if you delete the state file?
Deleting local state normally does **not** delete the actual AWS resources — but Terraform loses track of what it manages. That can cause:
- Terraform trying to create duplicate resources
- Existing infrastructure becoming unmanaged
- Trouble making future changes
- Having to import existing resources back into state

### State best practices
- Never casually delete or manually edit state files
- **Don't commit `terraform.tfstate` to GitHub**
- Treat state as potentially sensitive
- Keep backups and access controls on it
- On teams, use a remote backend with state locking

## Using Terraform in VS Code
Simplest project:
```
terraform-practice/
└── main.tf
```

Bigger projects usually split things up:
```
terraform-project/
├── main.tf
├── providers.tf
├── variables.tf
├── outputs.tf
└── terraform.tfvars
```

| File | Typical purpose |
|---|---|
| `main.tf` | Resource configurations |
| `providers.tf` | Provider requirements and configuration |
| `variables.tf` | Input variable declarations |
| `outputs.tf` | Output value declarations |
| `terraform.tfvars` | Values assigned to input variables |

Terraform loads **all** the `.tf` files in the folder as one config, so these names are just conventions, not requirements.

### Workflow in VS Code
1. Open the Terraform project folder
2. Create/edit your `.tf` files
3. Open the integrated terminal
4. Run Terraform commands from the project directory
5. Review the plan before applying

The HashiCorp Terraform VS Code extension gives you syntax highlighting, formatting, etc. — but it **doesn't** replace installing the Terraform CLI.

## Key terms
| Term | Definition |
|---|---|
| IaC | Infrastructure as Code |
| Terraform | Tool for provisioning and managing infrastructure |
| HCL | HashiCorp Configuration Language |
| Provider | Plugin connecting Terraform to a platform or API |
| Resource | Infrastructure object managed by Terraform |
| Argument | Configuration setting within a block |
| AMI | Amazon Machine Image |
| EC2 | Amazon Elastic Compute Cloud |
| Tag | Metadata attached to a resource |
| State | Terraform's record of managed infrastructure |
| Declarative | Describing the desired outcome instead of individual steps |
| Drift | Difference between actual infrastructure and its expected configuration |

## Knowledge check
Try these without looking back at the notes:
1. What does HCL stand for?
2. What's the difference between Terraform and HCL?
3. What's the purpose of a Terraform provider?
4. What does `aws_instance` represent?
5. What's the difference between a resource's local name and its AWS `Name` tag?
6. What does `terraform init` accomplish?
7. What's the difference between `terraform plan` and `terraform apply`?
8. What does `Plan: 2 to add, 1 to change, 0 to destroy` mean?
9. What's the purpose of Terraform state?
10. Why could deleting `terraform.tfstate` cause problems?
11. What does it mean that Terraform is declarative?
12. Why should you review a plan before applying it in production?

## Practice challenge — configure an AWS provider
**Difficulty:** Beginner · **Environment:** VS Code

**Goal:** write a Terraform config that declares and configures the AWS provider.

Requirements:
1. Make a folder called `terraform-practice`
2. Make a `main.tf` file in it
3. Declare the AWS provider with `required_providers`
4. Configure the provider to use `us-east-2`
5. Run `terraform init`

Rules:
- Don't create an EC2 instance yet
- Don't run `terraform apply`
- Write the HCL yourself instead of copying a full solution

Done when:
- [ ] `main.tf` has the provider declaration and configuration
- [ ] `terraform init` finishes successfully
- [ ] I can explain the difference between declaring and configuring a provider

> Initializing a provider doesn't create any AWS resources.

## Main takeaways
1. HCL is the language used to write Terraform configs
2. Providers let Terraform talk to services like AWS
3. Resources describe the infrastructure Terraform manages
4. Plan and apply let you preview and then execute changes
5. State is how Terraform tracks existing infrastructure

**Configuration = what I want · State = what Terraform manages · Infrastructure = what actually exists**

## Related Notes
- [aws-cloudops/deployment-services.md](../aws-cloudops/deployment-services.md) — AWS-native IaC (CloudFormation, CDK), good to compare against Terraform
- [aws-cloudops/compute-services.md](../aws-cloudops/compute-services.md) — EC2 and AMIs, the resources used in all the examples here
- [aws-cloudops/cloudops-progress.md](../aws-cloudops/cloudops-progress.md) — Terraform/Git IaC is listed as a Domain 3 gap
