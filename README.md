# DevOps Notes

Personal repository of DevOps learning notes, homelab setup docs, and IT support reference material.

## Current Goals

- AWS SysOps Administrator Certification
- Linux Administration
- Docker
- Kubernetes
- Terraform

## Folder Index

- **aws-sysops/** — Study notes for the AWS Certified CloudOps Engineer – Associate cert (formerly SysOps Administrator): cloud fundamentals, Well-Architected Framework, CAF, compute services. See [sysops-progress.md](aws-sysops/sysops-progress.md) for the current exam domain breakdown and what's covered vs. still a gap.
- **linux-admin/** — Linux administration reference notes (commands, file permissions, users & groups, systemctl). Some files are still placeholders to be filled in.
- **homelab-vm-setup/** — Setup notes for the homelab: Ubuntu VM and VirtualBox configuration, networking setup.
- **github-ssh/** — GitHub and SSH configuration notes (key setup, git config, workflow). Currently empty — to be filled in.
- **it-support-internship/** — Reference material from the IT support internship.
  - **troubleshooting/** — Step-by-step troubleshooting guides for common issues.
  - **tools/** — Notes on internship-specific tools (Encompass, myUHM, ZUHM, Argyle).
  - Ticket resolution notes live directly in this folder — use the template in `_templates/ticket-template.md` for each one.
- **runbooks/** — Step-by-step procedures for recurring operational tasks.
- **_templates/** — Reusable note templates. Currently: `ticket-template.md` for documenting IT support tickets (issue description, system/software, steps taken, root cause, resolution).
- **_review/** — Holding area for anything flagged as possibly redundant or outdated, pending a look before deletion. (Currently empty — nothing has been flagged.)

## Naming Convention

- Folders: lowercase, hyphenated (e.g. `aws-sysops`, `homelab-vm-setup`)
- Files: lowercase, hyphenated, descriptive (e.g. `ssh-key-setup.md`)
- Numbered prefixes only where sequence matters (e.g. AWS exam domains); otherwise no numbering
