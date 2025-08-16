# Computer Networks Fundamentals

## Networking Models

### OSI Model (7 Layers)
| Layer | Name                | Purpose                                                                 |
|-------|---------------------|------------------------------------------------------------------------|
| 7     | Application         | User interface, network services (e.g., HTTP, FTP, SMTP)               |
| 6     | Presentation        | Data translation, encryption, compression                              |
| 5     | Session             | Establish, manage, terminate sessions                                  |
| 4     | Transport           | Reliable data transfer, error recovery (TCP/UDP)                       |
| 3     | Network             | Routing, logical addressing (IP)                                       |
| 2     | Data Link           | Physical addressing (MAC), error detection (Ethernet, PPP)             |
| 1     | Physical            | Transmission of raw bits over physical medium (cables, radio)          |

### TCP/IP Model (4 Layers)
| Layer         | OSI Mapping         | Purpose                                  |
|---------------|--------------------|------------------------------------------|
| Application   | 7, 6, 5            | Network processes to applications        |
| Transport     | 4                  | Host-to-host communication (TCP/UDP)     |
| Internet      | 3                  | Routing, addressing (IP)                 |
| Network Access| 2, 1               | Physical transmission (Ethernet, Wi-Fi)  |

## Encapsulation / Decapsulation
- **Encapsulation:** Wrapping data with protocol information at each layer (header added).
- **Decapsulation:** Removing headers as data moves up the layers.

## IP Addressing

### IPv4 vs IPv6
| Feature      | IPv4                        | IPv6                                 |
|--------------|-----------------------------|--------------------------------------|
| Address Size | 32 bits (e.g., 192.168.1.1) | 128 bits (e.g., 2001:0db8::1)        |
| Format       | Dotted decimal              | Hexadecimal, colon-separated         |
| Addresses    | ~4.3 billion                | ~340 undecillion                     |
| Features     | NAT, limited security       | Built-in security, no NAT needed     |

### Public vs Private IP
- **Public IP:** Routable on the internet, assigned by ISP.
- **Private IP:** Used within local networks, not routable on internet.
  - IPv4 Private Ranges:
    - 10.0.0.0 – 10.255.255.255
    - 172.16.0.0 – 172.31.255.255
    - 192.168.0.0 – 192.168.255.255

### Subnetting Basics (CIDR Notation)
- **CIDR:** Classless Inter-Domain Routing, e.g., `192.168.1.0/24`
  - `/24` means 24 bits for network, 8 bits for hosts.
- **Purpose:** Efficient IP allocation, network segmentation.

### Loopback (127.0.0.1)
- Used to test network stack locally; refers to the host itself.

### APIPA (169.254.x.x)
- Automatic Private IP Addressing; assigned when DHCP fails.

## Protocols

### TCP vs UDP
| Feature      | TCP (Transmission Control Protocol) | UDP (User Datagram Protocol)      |
|--------------|-------------------------------------|-----------------------------------|
| Connection   | Connection-oriented                 | Connectionless                    |
| Reliability  | Reliable, error-checked, ordered    | Unreliable, no order guarantee    |
| Use Cases    | Web, email, file transfer           | Streaming, gaming, VoIP           |

### Common Protocols
| Protocol | Purpose                        | Port(s) |
|----------|-------------------------------|---------|
| HTTP     | Web browsing                  | 80      |
| HTTPS    | Secure web browsing           | 443     |
| FTP      | File transfer                 | 21      |
| DNS      | Domain name resolution        | 53      |
| DHCP     | Dynamic IP assignment         | 67/68   |
| SMTP     | Sending email                 | 25      |
| POP3     | Receiving email               | 110     |
| IMAP     | Receiving email (advanced)    | 143     |
| SSH      | Secure remote login           | 22      |

### Well-Known Ports Table
| Protocol | Port |
|----------|------|
| HTTP     | 80   |
| HTTPS    | 443  |
| FTP      | 21   |
| SSH      | 22   |
| SMTP     | 25   |
| DNS      | 53   |
| DHCP     | 67/68|
| POP3     | 110  |
| IMAP     | 143  |

## Key Networking Concepts

### MAC Address
- Unique hardware address for network interfaces (e.g., `00:1A:2B:3C:4D:5E`).

### ARP (Address Resolution Protocol)
- Maps IP addresses to MAC addresses in a local network.

### DNS Resolution Process
1. User enters domain name.
2. OS checks local cache.
3. Query sent to DNS resolver.
4. Resolver queries root, TLD, and authoritative servers.
5. IP address returned to client.

### NAT (Network Address Translation)
- Translates private IPs to public IPs for internet access.

### Firewall Basics
- Controls incoming/outgoing traffic based on rules; protects network.

### VPN Basics
- Secure, encrypted connection over public networks; used for privacy and remote access.

## Common Commands (Practical)

| Command      | Purpose                                  |
|--------------|------------------------------------------|
| ping         | Test connectivity to a host              |
| traceroute   | Show path packets take to destination    |
| tracert      | Windows version of traceroute            |
| ipconfig     | Show IP configuration (Windows)          |
| ifconfig     | Show IP configuration (Linux/Mac)        |
| netstat      | Show network connections and stats       |
| nslookup     | Query DNS records                        |
| curl/wget    | Transfer data from/to servers            |

## Important Metrics

### Bandwidth vs Throughput vs Latency
- **Bandwidth:** Maximum data transfer rate (capacity).
- **Throughput:** Actual data transfer rate (performance).
- **Latency:** Delay in data transmission (measured in ms).

### Packet Loss
- Percentage of packets lost during transmission; affects quality.

### MTU (Maximum Transmission Unit)
- Largest packet size that can be sent over a network.

---

**Tip:** For interviews, focus on explaining concepts clearly, use examples, and relate protocols to real-world