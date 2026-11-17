# DevOps Notes

Personal repository of DevOps learning notes, homelab setup docs, and IT support reference material.

## Current Goals

- AWS CloudOps Engineer Certification (formerly SysOps Administrator)
- Linux Administration
- Docker
- Kubernetes
- Terraform

## Folder Index

- **aws-cloudops/** — Study notes for the AWS Certified CloudOps Engineer – Associate cert (formerly SysOps Administrator): cloud fundamentals, Well-Architected Framework, CAF, support plans, compute services, storage services, database services, monitoring services, deployment services, audit & compliance services, networking & content delivery services, management & governance services, identity services, security services, application integration services, analytics services, machine learning services, transfer & migration services. See [cloudops-progress.md](aws-cloudops/cloudops-progress.md) for the current exam domain breakdown and what's covered vs. still a gap.
- **linux-admin/** — Linux administration reference notes: commands & shell basics (including wildcards and safe file removal), filesystem hierarchy, file permissions, viewing/searching/editing files (cat, head, tail). `systemctl.md` and `users-and-groups.md` are still placeholders to be filled in.
- **networking/** — General networking fundamentals, not tied to the AWS cert: network types (PAN/LAN/CAN/MAN/WAN), MAC addresses, IPv4/IPv6 addressing. Separate from `aws-cloudops/` since this material isn't from the CloudOps course.
- **terraform/** — Terraform / Infrastructure as Code notes: HCL basics, providers, resources, the init/plan/apply/destroy workflow, and state (`terraform-basics.md`). Terraform is also in scope for CloudOps Domain 3, so see [cloudops-progress.md](aws-cloudops/cloudops-progress.md) for how it ties in.
- **homelab-vm-setup/** — Setup notes for the homelab: Ubuntu VM and VirtualBox configuration, networking setup.
- **github-ssh/** — GitHub and SSH configuration notes. `ssh-key-setup.md` covers making an SSH key on the Mac, adding it to GitHub, switching the repo remote from HTTPS to SSH, and fixing the errors hit along the way.
- **it-support-internship/** — Reference material from the IT support internship.
  - **troubleshooting/** — Step-by-step troubleshooting guides for common issues.
  - **tools/** — Notes on internship-specific tools (Encompass, myUHM, ZUHM, Argyle).
  - Ticket resolution notes live directly in this folder — use the template in `_templates/ticket-template.md` for each one.
- **challenges/** — Hands-on practice write-ups from completed challenge scenarios (currently: a Linux filesystem cleanup challenge). Cross-references the relevant topic folder (e.g. `linux-admin/`) for the underlying command reference.
- **runbooks/** — Step-by-step procedures for recurring operational tasks.
- **_templates/** — Reusable note templates. Currently: `ticket-template.md` for documenting IT support tickets (issue description, system/software, steps taken, root cause, resolution).
- **_review/** — Holding area for anything flagged as possibly redundant or outdated, pending a look before deletion. (Currently empty — nothing has been flagged.)

## Naming Convention

- Folders: lowercase, hyphenated (e.g. `aws-cloudops`, `homelab-vm-setup`)
- Files: lowercase, hyphenated, descriptive (e.g. `ssh-key-setup.md`)
- Numbered prefixes only where sequence matters (e.g. AWS exam domains); otherwise no numbering
