# AWS Networking & Content Delivery Services

## Amazon VPC (Virtual Private Cloud)
A logical private network within the AWS Cloud that lets you launch EC2 instances and other resources in a virtual network you define.
- Gives you control over IP ranges, subnets, & gateways to connect with the internet or on-prem networks

## Amazon Elastic Load Balancing
Distributes incoming traffic across multiple resources to improve availability & performance.
- **Application Load Balancer** — for HTTP/HTTPS traffic
- **Network Load Balancer** — for TCP/UDP traffic

## Amazon Route 53
Manages DNS routing to direct traffic to AWS resources or external endpoints, supporting various routing policies.

## AWS Global Accelerator
Provides static IP addresses as fixed entry points to improve global application availability & performance.

## Amazon CloudFront
A CDN (Content Delivery Network) service — caches content at edge locations worldwide for faster delivery.

## AWS PrivateLink & VPN Services
Enable secure, private connections between your VPC and other networks without using the public internet — keeps traffic safe from interception.

## AWS Direct Connect
Offers dedicated network connections for consistent & secure data transfer.
- Higher bandwidth than a standard internet connection
- Does not pass through the public internet

## AWS Transit Gateway
Simplifies connecting multiple VPCs & networks through a single gateway, reducing complexity.

## AWS API Gateway
Manages & secures APIs, acting as a front door for backend services.

## AWS App Mesh
Provides service-to-service communication for containerized apps, enhancing network visibility & reliability.

## AWS Cloud Map
Commonly used in microservices architectures. Helps apps dynamically discover & connect to resources, improving availability.

Collectively, these services help build secure, scalable, & efficient network architectures in AWS.

## Related Notes
- [compute-services.md](compute-services.md) — EC2 instances that live inside the VPCs these services route traffic to
- [security-services.md](security-services.md) — WAF, Shield, and Network Firewall, which protect the traffic flowing through this networking layer
- [../networking/](../networking/) — general (non-AWS) networking fundamentals: network types, MAC/IPv4/IPv6 addressing that underlies VPC CIDR blocks and subnetting
- Maps to [cloudops-progress.md](cloudops-progress.md) Domain 5 (Networking and Content Delivery)
