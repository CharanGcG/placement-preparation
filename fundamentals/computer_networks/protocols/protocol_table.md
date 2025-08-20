***

# 📌 Computer Network Protocols – Cheat Sheet (Sorted by OSI Layers)

| Protocol | OSI Layer | Description | Example Use Case | Analogy |
|----------|-----------|-------------|------------------|---------|
| **ARP**  | Data Link (Layer 2 helper) | Maps IP addresses to MAC addresses | Finding MAC of a device in LAN | Asking “Who lives at this address?” in a neighborhood |
| **IP**   | Network (Layer 3) | Handles addressing and routing packets across networks | Sending data across the internet | Postal system deciding where a letter should go |
| **ICMP** | Network (Layer 3 control) | Used for error reporting & diagnostics | Running `ping` or `traceroute` | Traffic police signaling road issues |
| **TCP**  | Transport (Layer 4) | Reliable, connection-oriented protocol with error-checking | Web browsing, file transfers | A phone call – confirms delivery |
| **UDP**  | Transport (Layer 4) | Fast, connectionless protocol without guarantees | Video streaming, gaming | Loudspeaker announcement – fast but not guaranteed |
| **SSL/TLS** | Presentation/Security (Layer 6/7) | Secures communication with encryption | HTTPS secure data transport | Secret handshake before sharing info |
| **TELNET** | Application (Layer 7) | Remote login without encryption | Legacy remote admin tools | Talking on a public line where everyone can hear |
| **SSH**  | Application (Layer 7) | Secure remote login and file transfer | Administering servers remotely | Locked private door with a secret key |
| **HTTP** | Application (Layer 7) | Protocol for transferring web pages in plain text | Browsing blogs, static sites | Reading an open library book |
| **HTTPS** | Application (Layer 7) | Secure version of HTTP (uses TLS/SSL) | Online banking checkout | Same library, but book in a locked case |
| **FTP**  | Application (Layer 7) | Transfers files between client and server | Uploading/downloading site files | Courier delivering packages |
| **SMTP** | Application (Layer 7) | Sends outgoing emails | Sending mail via Gmail/Outlook | Dropping letter in a mailbox |
| **POP3** | Application (Layer 7) | Downloads emails, removes from server | Basic email client usage | Mailman delivering letters & not keeping copies |
| **IMAP** | Application (Layer 7) | Retrieves emails but keeps them on server | Sync Gmail on multiple devices | Post office stores copies of letters |
| **DNS**  | Application (Layer 7) | Resolves domain names to IP addresses | Turning *google.com* → IP | Phone directory mapping names to numbers |
| **DHCP** | Application (Layer 7) | Dynamically assigns IP addresses | Auto-assignment on Wi-Fi | Hotel reception assigning room keys |
| **SNMP** | Application (Layer 7) | Manages/monitors network devices | Monitoring enterprise routers | Security cameras reporting activity |
| **NTP**  | Application (Layer 7) | Synchronizes clocks across systems | Servers keeping same time | Family resetting watches to same clock |
| **RDP**  | Application (Layer 7) | Remote desktop access | Accessing a Windows machine remotely | Sitting at someone else’s PC virtually |

***
