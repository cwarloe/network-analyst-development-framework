# Initial Evidence Packet

## Operational context

At 09:20 local time, monitoring identifies sustained encrypted outbound traffic from workstation `WS-447` to `203.0.113.42:443`. The connection pattern begins shortly after a scheduled update to a fictional synchronization client named AcmeSync.

The immediate decision is whether current evidence supports continued monitoring and validation or a more disruptive containment response.

All organizations, systems, domains, addresses, and software names are fictional. The `.example` domain and `203.0.113.0/24` documentation address space are used intentionally.

## Available evidence

| ID | Source | Observation | Known limitation |
|---|---|---|---|
| E-01 | Change record | AcmeSync 4.8.2 deployment began at 09:00 for 40 workstations. | The record does not describe post-update telemetry destinations. |
| E-02 | DNS log | `WS-447` resolved `telemetry.acmesync.example` to `203.0.113.42` at 09:14:52. | DNS resolution alone does not establish who controls a destination or whether it is trustworthy. |
| E-03 | Network flow | `WS-447` began TLS connections to `203.0.113.42:443` at 09:15:03, transferred 18.4 MB outbound and 1.8 MB inbound over 42 minutes, and reconnected about every 60 seconds. | Flow data does not expose the encrypted content. |
| E-04 | TLS metadata | The observed server name and certificate subject reference `telemetry.acmesync.example`; the certificate chain validates in the collection environment. | A valid certificate protects a connection to a named service; it does not establish that the service or initiating process is authorized. |
| E-05 | Endpoint process record | Signed `AcmeSync.exe` launched signed `AcmeSyncUpdater.exe` at 09:14:39. The updater initiated the connections. | Loaded modules, effective binary provenance, and runtime behavior have not been independently reviewed. |
| E-06 | Peer comparison | 37 of 40 targeted workstations contacted the same destination after updating. Transfer volume ranged from 14 MB to 21 MB during the first hour. | Three systems were offline. Similarity may reflect expected deployment behavior, a shared fault, or a compromised distribution channel. |
| E-07 | Proxy categorization | The destination is newly observed and uncategorized. No policy block or known-malicious match exists. | Absence of a reputation match is not evidence of safety. |
| E-08 | User report | The user did not manually start AcmeSync and observed no visible prompt. | Background update activity may be expected; user awareness is not determinative. |
| E-09 | Software inventory | `WS-447` reports AcmeSync 4.8.2 installed successfully. The updater hash matches the hash reported by the 36 online peer systems. | The expected vendor hash, telemetry domain, and release behavior have not been independently confirmed. |

## Constraints and interfaces

- Isolation would interrupt the user's work and could disrupt 36 additional online systems if applied broadly.
- The software owner can validate release metadata and expected service behavior.
- The endpoint-response team can inspect binary provenance, loaded modules, persistence, and host behavior.
- The network analyst owns the observed communications evidence and must make it usable to those teams.

Return to the [learner instructions](README.md) and complete your initial work product before opening later evidence.
