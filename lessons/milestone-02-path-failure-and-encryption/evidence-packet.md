# Milestone 2 Evidence Packet — Path Failure, Evidence Vantage, and Encryption

## Incident Context: Ticket #12094
- **Reported:** 14:15 Local Time
- **Affected Systems:** Portland Branch Workstations, Chicago Plant Terminals, Core ERP Backend, SaaS Document Vault (`vault-saas.harrowmere-cloud.example`).
- **Initial Ticket Summary:**
  > *"SEV-1 OUTAGE / SUSPECTED COVERED ATTACK: Core ERP degraded, external Vault TLS sessions dropping, and network latency reported across branches."*

---

## Item E-01: Zeek Connection Summary (`conn.log`)
Captured at the HQ Edge Sensor between 14:00 and 14:10:

| Timestamp | Source Socket | Destination Socket | Proto | Service | Duration | Orig Bytes | Resp Bytes | Conn State | State Description | History |
|---|---|---|---|---|---|---|---|---|---|---|
| `14:02:11.102` | `192.0.2.14:51201` | `198.51.100.30:80` | `tcp` | — | `0.000012` | `0` | `0` | `REJ` | Connection attempt rejected | `Sr` |
| `14:02:15.340` | `192.0.2.14:51202` | `198.51.100.20:80` | `tcp` | — | `4.081100` | `0` | `0` | `S0` | Connection attempt seen, no reply | `S` |
| `14:02:19.422` | `192.0.2.14:51202` | `198.51.100.20:80` | `tcp` | — | `2.012400` | `0` | `0` | `S0` | Connection attempt seen, no reply | `S` |
| `14:02:22.010` | `192.0.2.14:51204` | `198.51.100.50:80` | `tcp` | `http` | `5.001200` | `112` | `140` | `SF` | Normal SYN/FIN completion | `ShADadfF` |
| `14:02:30.150` | `192.0.2.14:51208` | `203.0.113.50:443` | `tcp` | `ssl` | `1.120400` | `1,420` | `4,850` | `SF` | Normal SYN/FIN completion | `ShADadfF` |

---

## Item E-02: TCP & HTTP Frame Dissection (From HQ Edge Full PCAP)

### Stream for `198.51.100.50:80` (Connection `14:02:22.010`):
```
Frame 101  14:02:22.0101  192.0.2.14 -> 198.51.100.50  TCP 51204 -> 80 [SYN]
Frame 102  14:02:22.0103  198.51.100.50 -> 192.0.2.14  TCP 80 -> 51204 [SYN, ACK]  (Delta: 0.0002s)
Frame 103  14:02:22.0104  192.0.2.14 -> 198.51.100.50  TCP 51204 -> 80 [ACK]
Frame 104  14:02:22.0106  192.0.2.14 -> 198.51.100.50  HTTP GET /api/v2/finance/ledger (112 bytes)
Frame 105  14:02:22.0108  198.51.100.50 -> 192.0.2.14  TCP 80 -> 51204 [ACK]        (Delta: 0.0002s)
[ ... NO PACKETS ON WIRE FOR 5.0001 SECONDS ... ]
Frame 106  14:02:27.0109  198.51.100.50 -> 192.0.2.14  HTTP/1.1 200 OK (140 bytes)
Frame 107  14:02:27.0111  192.0.2.14 -> 198.51.100.50  TCP 51204 -> 80 [ACK]
Frame 108  14:02:27.0113  198.51.100.50 -> 192.0.2.14  TCP 80 -> 51204 [FIN, ACK]
```

### Stream for `203.0.113.50:443` (`vault-saas.harrowmere-cloud.example`):
```
Frame 201  14:02:30.1500  ClientHello (SNI: vault-saas.harrowmere-cloud.example, Supported: 0x0304, 0x0303)
Frame 202  14:02:30.1820  ServerHello (version: 0x0303, supported_versions ext: 0x0304, Cipher: TLS_AES_256_GCM_SHA384)
Frame 203  14:02:30.1825  Application Data (Encrypted Handshake & Cert: 1,280 bytes)
Frame 204  14:02:30.2100  Application Data (Encrypted Request: 420 bytes)
Frame 205  14:02:30.4500  Application Data (Encrypted Response: 3,570 bytes)
```

---

## Item E-03: DNS Telemetry & Packet Fragmentation
Query from Portland branch workstation `192.0.2.14` for internal record `cluster-sync.harrowmere.internal`:
- **Resolver Log:** Internal resolver `192.0.2.2` logs response sent via UDP, response size 1,740 bytes.
- **Client Experience:** Workstation reports `DNS query timed out (server failure)`.
- **Edge Wire Capture (`tshark -T fields -e ip.id -e ip.flags.mf -e ip.frag_offset -e udp.dstport`):**
  ```
  Frame 501: ip.id=0x78ab  MF=1  frag_offset=0    udp.dstport=—   ip.len=1400
  Frame 502: ip.id=0x78ab  MF=0  frag_offset=170  udp.dstport=53  ip.len=380
  ```
- **Network Path Config:** Portland traffic hairpins over IPSec VPN tunnel to HQ. Tunnel interface MTU is set to 1400 bytes. Intermediate perimeter security policy: `"Drop non-initial IP fragments"`.

---

## Item E-04: Available Evidence Sources & Retention Clocks

| Source System | Location / Scope | Logging Configuration | Retention Clock |
|---|---|---|---|
| **HQ Edge Full PCAP** | Core Egress Switch | Rolling ring buffer (all packets unsampled) | **36 Hours** |
| **Edge Zeek Logs** | HQ Sensor | `conn.log`, `ssl.log`, `dns.log`, `x509.log` | **30 Days** |
| **Perimeter Firewall** | HQ Edge | **Configured to log DENIED connections only** | **90 Days** |
| **Branch Switch NetFlow** | Portland Branch Router | Sampled 1:100 flow records | **14 Days** |
| **Workstation EDR** | Portland Workstations | Process creation, socket connect/listen | **30 Days** |
| **SaaS Admin Console** | Cloud Vendor Portal | Server-side request log and processing time | **7 Days** |

---

## Item E-05: Colleague's Escalation Handoff Note
Appended to Ticket #12094 by Junior Admin:
> *"The external SaaS vault is dropping connections or failing with TLS errors. The edge PCAP shows TLS 1.3 connections where we can't see the certificates or HTTP statuses, so this might be encrypted data exfiltration or a man-in-the-middle attack. Also, connection to the internal reporting server (198.51.100.20) is completely down—we ran a firewall search for denies and found nothing, so the core router must be dropping packets. And the database query interface is taking 5 seconds, so the network team needs to fix their WAN latency immediately."*

