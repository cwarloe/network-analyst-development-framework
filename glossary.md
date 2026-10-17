# Master Analytical Glossary

A comprehensive reference of network telemetry concepts, transport mechanics, analytical disciplines, and operational failure modes used across the framework.

---

## Telemetry & Logging

| Term | Desk Translation | Operational Context |
|---|---|---|
| **Dropped Pipeline Fields** | Log fields that exist on network sensors like Zeek but are discarded during ingestion before reaching the SIEM search index. | Never confuse what the tool pipeline happens to store with what the network actually carried. |
| **Packet Capture (.pcap)** | A raw, byte-level file recording every frame that traversed a network interface or tap during the capture window. | Highest fidelity source available, but perishable due to high disk volume and rolling buffers. |
| **Rolling PCAP Buffer** | A finite disk ring buffer continuously recording raw packet bytes until storage limits force overwriting oldest files. | Retention is often 24–72 hours; always pull raw capture evidence against the shortest clock first. |
| **Sampled NetFlow** | A telemetry protocol exporting flow statistical summaries at a fixed sampling ratio (such as 1:100 packets). | Excellent for long-term volume trends; silence is weak evidence of absence for small, low-volume flows. |
| **Sub-millisecond Duration** | Session elapsed time recorded in seconds; sub-millisecond durations indicate automated programmatic execution. | A duration like 0.000184s (184 µs) proves automated software speed rather than human typing. |
| **Zeek conn.log** | The connection log in Zeek summarizing Layer 3/4 session facts (IPs, ports, protocol, duration, byte counts, and connection state). | Focuses on transport summaries. It does not carry application payloads or HTTP bodies. |

## Transport & TCP Mechanics

| Term | Desk Translation | Operational Context |
|---|---|---|
| **Client Demarcation** | Determining which host originated a conversation by identifying which socket sent the initial SYN frame. | Crucial for determining conversation initiator versus responder, regardless of port numbers. |
| **Connection Reset (RST)** | An abrupt termination frame sent by an endpoint indicating rejection, teardown, or abnormal closure. | A reset is an explicit event with an origin; silence is an absence of observation. |
| **connection.state: SF** | Normal SYN/FIN completion in Zeek; both sides cleanly opened and closed the connection. | Proves transport reachability and orderly socket teardown in both directions. |
| **Ephemeral Port** | A short-lived, high-numbered client source port (typically 49152–65535) dynamically assigned by the OS. | Identifies distinct client sockets; servers assign responses back to this port. |
| **Exponential Backoff** | Client TCP stack doubling retransmission delays across silence (1s, 2s, 4s) when packets are dropped. | A classic hallmark of silent path drops or dead-end firewall rules. |
| **Non-Initial Fragment** | Subsequent IP packet fragments (offset > 0) carrying only payload bytes and lacking Layer 4 transport headers. | Invisible to port-based firewall filters; policies dropping non-initial fragments cause silent timeouts. |
| **Path MTU** | The maximum transmission unit size in bytes that can traverse an end-to-end network path without fragmentation. | Exceeding Path MTU forces IP fragmentation; intermediate drops of fragments break reassembly silently. |
| **TCP 3-Way Handshake** | The SYN, SYN-ACK, ACK sequence establishing a reliable transport connection between client and server sockets. | Proves transport connectivity only; tells you nothing about application authorization or status. |
| **TCP Acknowledgment** | The receiver's TCP stack confirming receipt of bytes, independent of whether the application has processed or answered. | A bare ACK proves network delivery to the host OS; application think time happens after. |
| **TCP Stream** | The full bidirectional sequence of ordered TCP segments belonging to a single 4-tuple socket conversation. | In Wireshark, 'Follow TCP Stream' reconstructs payload bytes in chronological order. |

## Domain Name System (DNS)

| Term | Desk Translation | Operational Context |
|---|---|---|
| **Apex Domain** | The base root domain (e.g. example.com) directly under a TLD, common across subdomains and distinct IPs. | Reveals relational convergence across seemingly independent IPs and protocols. |
| **CNAME Record** | A Canonical Name DNS record that maps an alias hostname to another true domain name in a lookup chain. | Common in CDNs; lookups follow the chain until reaching an A or AAAA address record. |
| **DNS Cache** | Temporary local memory where an operating system or browser stores recent DNS answers to avoid repeat queries. | Absence of a DNS query on the wire during a connection window is frequently explained by local cache hits. |
| **DNS TTL (Time to Live)** | A 32-bit field in a DNS resource record defining how many seconds a client or resolver may cache the answer. | Clients reuse cached entries until TTL expires, so subsequent connections generate no observable network queries. |
| **Recursive DNS Resolver** | A DNS server that accepts queries from clients and queries authoritative nameservers recursively to find the IP address. | Workstations query resolvers; an edge sensor sees only traffic leaving or entering that resolver boundary. |

## Encryption & TLS 1.3

| Term | Desk Translation | Operational Context |
|---|---|---|
| **Content Type 23 (Application Data)** | TLS record type that encapsulates all post-ServerHello handshake messages and application payloads in TLS 1.3. | In TLS 1.3, certificates and extensions are encrypted under Content Type 23. |
| **Decoy SNI** | Crafting cleartext Server Name Indication fields requesting trusted company hostnames to fool egress monitoring. | SNI is unauthenticated on the wire; an adversary's client can send any string in ClientHello. |
| **Self-Signed Certificate** | An X.509 certificate whose digital signature is created by its own private key rather than a trusted CA. | Subject equals issuer; common in lab and staging environments, but unverified by public trust stores. |
| **Server Name Indication (SNI)** | A TLS extension in ClientHello where the client sends the destination hostname in cleartext before encryption begins. | Visible on the wire unless Encrypted Client Hello (ECH) is deployed; client-controllable and can be decoyed. |
| **supported_versions Extension** | TLS Extension 43 that communicates the true negotiated TLS version (0x0304 for TLS 1.3), bypassing legacy fields. | Outer TLS version fields are frozen at 0x0303 (TLS 1.2) for middlebox compatibility. |
| **TLS Version 0x0303 Freeze** | The legacy outer record layer version field frozen at TLS 1.2 to prevent legacy middleboxes from dropping connections. | Negotiated TLS 1.3 versions are carried inside the supported_versions extension. |

## Application Layer & Web

| Term | Desk Translation | Operational Context |
|---|---|---|
| **200 OK** | HTTP status code indicating the web server successfully accepted and processed the request. | Confirms the HTTP exchange succeeded; does not prove whether the payload was the full dataset or just a metadata summary. |
| **403 Forbidden** | HTTP status code where the server understood the request but actively refused to authorize it. | Proves the network path and web server are operational; the refusal originates in application authorization. |
| **API Endpoint** | A specific URI or path on a web server where client software sends structured requests to consume backend services. | Reaching an API endpoint verifies network delivery; it does not indicate whether authorization succeeded. |
| **JSON Payload** | A lightweight, text-based data format used to structure application responses between web servers and clients. | Contained inside the HTTP application body; completely unobservable when sessions are encrypted. |
| **User-Agent String** | An HTTP header string sent by the client identifying its software application, version, and operating system. | Client-controlled and trivially spoofed; never use User-Agent alone as an indicator of authenticity. |

## Conversation Failures & Anomalies

| Term | Desk Translation | Operational Context |
|---|---|---|
| **[RST, ACK] Packet** | A transport refusal packet indicating the destination host received the SYN, but rejected the socket attempt. | Proves the path and host are 100% reachable bidirectionally; points to host policy or closed ports. |
| **connection.state: REJ** | Zeek connection state indicating active transport refusal; server OS responded immediately with an RST packet. | Proves bidirectional reachability; the server host is alive and actively refusing the connection. |
| **connection.state: RSTR** | Zeek connection state indicating established session aborted by responder; server returned partial data then sent reset. | Common when application workers crash or timeouts sever the server-side socket. |
| **connection.state: S0** | Zeek connection state where an opening SYN was observed, but zero response bytes or ACKs ever returned. | Indicates delivery failure (silent firewall drop or routing dead-end), resulting in client timeout. |

## Network Architecture & Vantage

| Term | Desk Translation | Operational Context |
|---|---|---|
| **Corporate VPN Gateway** | A network boundary where traffic enters an encrypted tunnel, often undergoing address translation and routing changes. | Edge firewalls see the gateway's public IP rather than the true internal workstation RFC 1918 address. |
| **Layer Independence** | The principle that transport success (TCP) says nothing about application authorization (HTTP), and vice versa. | Avoid conflating layer statuses: a successful handshake does not mean an authorized request. |
| **Middlebox** | An inline network appliance (proxy, legacy firewall, or traffic shaper) that inspects or manipulates traffic. | Legacy middleboxes dropping unknown version numbers forced TLS 1.3 to freeze legacy version headers. |

## Investigation & Relational Analysis

| Term | Desk Translation | Operational Context |
|---|---|---|
| **DNS Tunneling** | An evasion technique encoding non-DNS payloads or commands into subdomains and TXT response records. | Characterized by high-entropy subdomain strings, long query lengths, and caching bypass. |
| **Immediate TCP ACK** | Immediate TCP ACK confirming instant network delivery before application think time begins. | Separates network latency (< 1ms) from application latency (4+ seconds). |
| **Relational Convergence** | Superficially independent network behaviors (HTTP poll, DNS bursts, uploads) connecting to a common entity. | Much harder for adversaries to disguise than timing jitter; far stronger evidence than isolated shapes. |
| **Staged C2 Channel** | A multi-phase connection where initial check-ins use decoy domains or small payloads before exfiltration begins. | Designed to blend into normal post-update telemetry traffic. |

## Alert Triage & Discipline

| Term | Desk Translation | Operational Context |
|---|---|---|
| **C2 Beaconing** | Recurring, scheduled outbound network connections initiated by an implant to check in with a command server. | Shared by legitimate software (updates, NTP, NTP, telemetry); timing regularity alone is never proof of malice. |
| **Discriminating Inquiry** | An analytical method identifying an observation that must be present under one hypothesis and absent under another. | Separates competing explanations without gathering unnecessary, expensive data. |

## Analytical Judgment & Handoff

| Term | Desk Translation | Operational Context |
|---|---|---|
| **3-Column Bounded Claim** | Analytical method separating what is directly observable, what is inferable, and what cannot be determined without host telemetry. | Prevents overreaching and identifies exactly which external data source to consult next. |
| **Action Reversibility** | The ease with which an operational intervention (like route rollback vs host reimage) can be safely undone. | High reversibility enables swift operational remediation under uncertainty. |
| **Confidence Breaker** | A specifically named observation or test result that would immediately falsify the leading hypothesis. | Ensures an assessment is falsifiable and safe to be wrong in. |
| **Falsifiable Prediction** | An explicit, written commitment stating what specific network behavior must occur next if a hypothesis is true. | Writing down predictions before checking subsequent packets prevents hindsight bias. |
| **Immediate Containment** | Network isolation of an endpoint to stop egress communication while preserving volatile memory (RAM). | Crucial distinction: sever network access, but do not reboot or power off the endpoint. |
| **Model Revision Out Loud** | The professional capability to publicly discard a previous hypothesis when contradictory evidence appears. | The antidote to cognitive anchoring and defending failed models under management pressure. |
| **Proportionate Action** | A response whose severity and disruption match the strength of evidence and reversibility of the decision. | Prevents overreacting (unnecessary reimaging) while maintaining containment of genuine risks. |
| **Reasoned Revision** | Updating an analytical model based on contradictory evidence rather than rationalizing surprise or defending the previous model. | Distinguishes disciplined investigation from guessing or defending ego. |
| **Two-Audience Handoff** | Delivering identical evidence claim strength to technical peers and managers while tailoring operational depth. | Never adapt the certainty of a claim to leadership's appetite for a simple answer. |

