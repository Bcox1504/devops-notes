# Networking Foundations: Basics

General networking fundamentals — not AWS-specific. For the AWS networking services (VPC, Route 53, CloudFront, etc.), see [aws-cloudops/networking-services.md](../aws-cloudops/networking-services.md) instead.

## What is a network?
A collection of interconnected devices that communicate — like a laptop connecting to an email server.

- Networks connect devices via **wired connections** (Ethernet cables) or **wireless connections** (Wi-Fi, cellular)

## Networks by geographic scope
Networks are categorized by how far they physically reach:

| Type | Name | Scope |
|---|---|---|
| PAN | Personal Area Network | 2 devices, very small (e.g., phone to a Bluetooth headset) |
| LAN | Local Area Network | Local to a building or area of a building |
| CAN | Campus Area Network | Nearby buildings |
| MAN | Metropolitan Area Network | Multiple offices in an area/city |
| WAN | Wide Area Network | Large geographic regions |

- WAN connections often use the internet, with encryption technologies like VPNs to secure the data as it crosses public networks

## Benefits of a network
- Ability to share resources (printers, files, internet connections)
- Communications
- Redundancy — backup data over the network
- Internet access
- Monitor connected devices

These basics provide a solid foundation for understanding how devices communicate in various environments — essential in IT support and network administration. Networking is integral to both personal and professional environments.

## Related Notes
- [network-addresses.md](network-addresses.md) — MAC/IPv4/IPv6 addressing, the actual identifiers devices on these networks use to find each other
- [homelab-vm-setup/](../homelab-vm-setup/) — hands-on networking setup for the homelab VirtualBox environment
- [aws-cloudops/networking-services.md](../aws-cloudops/networking-services.md) — how these fundamentals map onto AWS-specific networking (VPC, subnets, etc.)
