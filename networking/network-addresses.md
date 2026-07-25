# Networking Addresses

How devices are actually identified on a network — MAC addresses (physical/hardware) and IP addresses (logical). General networking fundamentals, not AWS-specific — see [aws-cloudops/networking-services.md](../aws-cloudops/networking-services.md) for the AWS side.

## MAC Addresses
Unique 48-bit physical addresses assigned to network devices during manufacturing, often called "burned-in" addresses. MAC = **Media Access Control**.

- The first 24 bits of a MAC address, known as the **Organizationally Unique Identifier (OUI)** or vendor code, identify the device manufacturer
- Switches use MAC addresses to make forwarding decisions for data within a network, helping direct traffic efficiently

## IPv4 Addresses
A logical address assigned to devices — unlike a MAC address, which is a physical address burned into hardware.

- 32 bits long, divided into 4 sections of 8 bits each, called **octets**, written in dotted decimal notation (e.g., `192.168.1.1`)
- A **subnet mask** divides the IPv4 address into network and host parts, helping identify the device's location on the network
- IPv4 addresses are running out due to the sheer number of devices online, but **Network Address Translation (NAT)** helps extend usability by letting many devices on a private network share one public IP

## IPv6 Addresses
128 bits long, providing a vastly larger number of unique addresses compared to IPv4.

- Instead of subnet masks, IPv6 uses a **prefix length** to indicate how many bits represent the network portion
- Written in hexadecimal notation, divided into 8 groups called **quartets**
- Example: `2340:201A:00B2:0000:000A:00B6:0460:0001/64` — a `/64` prefix length means half the address is for the network, half for the host

This format and scalability make IPv6 essential for supporting the growing number of devices on networks today.

## Related Notes
- [network-foundations.md](network-foundations.md) — the network types (LAN, WAN, etc.) these addresses operate within
- [aws-cloudops/networking-services.md](../aws-cloudops/networking-services.md) — VPC CIDR blocks and subnetting use this same IPv4/IPv6 addressing
