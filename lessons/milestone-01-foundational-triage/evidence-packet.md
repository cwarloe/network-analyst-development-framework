# Milestone 1 Evidence Packet

## Incident Background
At 10:14 local time, an automated SIEM detection escalated alert `#10842` for Workstation `WS-108` (`192.0.2.108`) in the Finance subnet. 

An initial tier-1 analyst flagged the event as an *"Active Lateral Probe & DNS Exfiltration Leak"* and drafted an emergency containment order. Before the workstation is disconnected, you are handed the raw evidence packet below to produce an objective, defensible triage assessment.

---

## Item E-01: Change Repository & Asset Context
* **Change Record CR-991 (Applied 09:30):** Enterprise Applications deployed `harrow-sync/3.21` to 15 finance workstations, including `WS-108`.
* **Asset Database Record:**
  * `192.0.2.108`: Workstation assigned to Senior Financial Analyst (WS-108).
  * `198.51.100.20`: Internal Reporting Platform & Archive API managed by Leah Moreno.
  * `203.0.113.0/24`: IP address block assigned to AWS US-West region, utilized by Harrowmere's contracted document backup provider.
  * `192.0.2.2`: Internal Active Directory Domain Controller and primary DNS resolver.

---

## Item E-02: DNS Resolver Log (`dns.log`)
Captured from internal resolver `192.0.2.2` during the incident window:

| ID | Timestamp | Query Name | Type | Response Code | Answers / Resolved IPs | TTLs |
|---|---|---|---|---|---|---|
| D-1 | `10:11:02.104` | `cdn.harrowmere-cloud.example` | `A` | `NOERROR` | `203.0.113.15, 203.0.113.16` | `60, 60` |
| D-2 | `10:11:45.320` | `cdn.harrowmere-cloud.example` | `A` | `NOERROR` | `203.0.113.88, 203.0.113.89` | `60, 60` |
| D-3 | `10:11:50.012` | `telemetry.harrowsync-update.example` | `A` | `NOERROR` | *(Empty / 0 Answer RRs; Authority SOA present)* | `1800` |

---

## Item E-03: Network Connection Telemetry (`conn.log`)
Extracted from edge switch sensor monitoring the Finance VLAN:

| ID | Timestamp | Source Socket | Destination Socket | Duration | Protocol | State | State Description | Orig Bytes | Resp Bytes |
|---|---|---|---|---|---|---|---|---|---|
| C-1 | `10:11:15.012` | `192.0.2.108:49210` | `198.51.100.20:80` | `0.000192s` | `tcp` | `SF` | Normal SYN/FIN completion | 148 | 44 |
| C-2 | `10:11:22.400` | `192.0.2.108:49218` | `203.0.113.15:443` | `12.4102s` | `tcp` | `SF` | Normal SYN/FIN completion | 4,812,040 | 1,200 |

*(Note: No connection records exist from `192.0.2.108` to any IP associated with `telemetry.harrowsync-update.example`).*

---

## Item E-04: HTTP Application Transaction Log (`http.log`)
Extracted from Zeek protocol dissection for Connection `C-1`:

| Field | Value |
|---|---|
| `ts` | `10:11:15.012` |
| `uid` | `C8vK12a9m1QzL` |
| `id.orig_h` | `192.0.2.108` |
| `id.resp_h` | `198.51.100.20` |
| `method` | `GET` |
| `host` | `files.harrowmere-group.example` |
| `uri` | `/api/v2/admin/status` |
| `user_agent` | `harrow-sync/3.21` |
| `request_body_len` | 0 |
| `response_body_len` | 44 |
| `status_code` | `403` |
| `status_msg` | `Forbidden` |
| `resp_payload` | `{"error":"unauthorized_client_certificate"}` |

---

## Item E-05: Colleague's Escalation Handoff
Received from Tier-1 Analyst:
> *"WS-108 is infected. It ran two rapid DNS lookups to different IPs within 43 seconds (clearly DNS fast-flux or poisoning), then attempted to probe the internal file server admin portal which failed, and then dumped 4.8 MB of staged data out to an external cloud IP over encrypted port 443. Recommend immediate network isolation of WS-108."*
