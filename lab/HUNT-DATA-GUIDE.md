# Hunt Telemetry Engine Guide: Operating the Harrowmere Data Lake

This guide explains how to generate, explore, and query the **Book 2 (*The Hunter's Eye*)** enterprise threat hunting datasets using [`generate-hunt-telemetry.py`](generate-hunt-telemetry.py).

---

## 1. Overview & Architecture

In Book 1 (*Learning to See*), learners work with small, clean packet captures (20 to 100 packets) bounded to specific tickets. In Book 2 (*The Hunter's Eye*), the problem space fundamentally shifts: **the SIEM is silent, no tickets are open, and the hunter must isolate stealthy needles embedded inside millions of lines of authentic enterprise noise.**

[`generate-hunt-telemetry.py`](generate-hunt-telemetry.py) is a zero-dependency, standard-library Python engine that generates statistically authentic telemetry modeling **Harrowmere Equipment Group** across a 14-day observation window:

```
Enterprise Noise Distribution
▲
│ ████████████████  ◄── Head (90% Volume):
│ ████████████████      Microsoft 365, Google Workspace, AWS CloudFront,
│ ████████████████      Active Directory syncs, internal database queries.
│ █
│ █ ▂ ▂ ▂ ▂ ▂       ◄── Torso (9.99% Volume):
│                       Dave Henderson's 48 GB lathe maintenance videos (10.100.12.44),
│                       Priya's Sunday midnight Azure backup (10.100.1.25),
│                       Marcus Whitlock's Rust crate downloads (10.100.42.18).
│
│ ░░░░░░░░░░░░░░░░░ ◄── Long Tail & Adversary Needles (0.01% Volume):
└───────────────────►   - 2011 Portland basement heating boiler (Tuesdays at 03:00, 128 bytes)
                        - HP printer SNMP sweeps
                        - Three stealthy adversary campaigns (C2 jitter, domain fronting, DNS tunneling)
```

---

## 2. Generating the Dataset

Run the generator from the repository root. Zero third-party packages or virtual environments are required:

```bash
# Generate 100,000 events and run the verification audit
python lab/generate-hunt-telemetry.py --count 100000 --verify --out-dir lab/hunt-data

# Generate a fast 25,000-event practice slice for SQLite only
python lab/generate-hunt-telemetry.py --count 25000 --format sqlite --out-dir lab/hunt-data

# Replay exactly the same synthetic case in a different session
python lab/generate-hunt-telemetry.py --count 25000 --seed 42 --start-date 2026-09-01 --out-dir lab/hunt-data

# Reproduce the FULL Hunt 05 capstone's 142,890 DNS TXT queries (larger output)
python lab/generate-hunt-telemetry.py --count 100000 --days 14 --full-hunt05 \
  --seed 42 --start-date 2026-09-01 --format sqlite --verify --out-dir lab/hunt-data
```

The default is a **fast practice preview** with 2,500 Hunt 05 exfiltration queries; it does **not** reproduce the capstone's quoted DNS count. `--full-hunt05` generates the 142,890-query authored case. Both modes include 642 Hunt 03 TLS sessions, 3,840 Chicago Hunt 05 TLS sessions, and 22 Chicago-to-Portland SMB/RPC sessions. Simulated DNS labels are entropy-constrained to produce a mean near the authored 4.86 bits/symbol; they are **not real ciphertext**. `--count` sets the volume of *background* events, not the total count across all embedded campaigns; a 100,000-event baseline does not reproduce the narrative's 10M+ enterprise-wide corpus. Synthetic data is illustrative and should not be passed off as real observed telemetry.

### CLI Options:
* `--count, -n`: Total baseline events to synthesize (default: 100,000).
* `--days, -d`: Rolling time window in days (default: 14).
* `--format, -f`: Output target (`sqlite`, `ndjson`, or `all`).
* `--out-dir, -o`: Target output folder (default: `lab/hunt-data`).
* `--verify, -v`: Runs automated mathematical audits asserting needle detectability ($CV < 0.20$, entropy $H > 4.5$, cardinality == 1).
* `--seed`: Optional integer seed for the synthetic host and event choices.
* `--start-date`: Optional case start date (`YYYY-MM-DD`, UTC midnight). **Use both `--seed` and `--start-date` to reproduce the exact records and output files.** Without a start date, the default case window rolls forward with the clock.
* `--full-hunt05`: Generate the complete Hunt 05 DNS evidence instead of the 2,500-query preview (allow additional disk space/time).

The [Harrowmere network map](../assets/harrowmere-network-map.svg) is a reusable location reference for Book 2, not a diagram of the embedded campaigns or observed links.

---

## 3. Supported Formats & Analysis Workflows

### Option A: Lightning-Fast Local SQL (Zero Server Setup)
The generator builds an indexed SQLite database at `lab/hunt-data/hunt_telemetry.db` containing `conn_log`, `dns_log`, `http_log`, and `ssl_log`.

You can query it immediately using any SQLite client or Python:

```sql
-- Hunt 02 Drill: User-Agent Least-Frequency Stacking
SELECT user_agent, COUNT(*) as event_count, COUNT(DISTINCT source_ip) as host_cardinality
FROM http_log
GROUP BY user_agent
ORDER BY event_count ASC
LIMIT 10;
```

```sql
-- Hunt 03 Drill: distinct engineering workstation, 642 TLS sessions
SELECT timestamp, source_ip, destination_ip, duration
FROM conn_log
WHERE source_ip = '10.42.18.91' AND destination_ip = '198.51.100.84'
  AND destination_port = 443
ORDER BY timestamp ASC
LIMIT 20;
```

```sql
-- Hunt 05 Case Fidelity: 3,840 C2 TLS sessions, 22 east-west SMB/RPC sessions
SELECT COUNT(*) FROM conn_log
WHERE source_ip = '10.120.32.14' AND destination_ip = '198.51.100.84' AND destination_port = 443;
SELECT COUNT(*) FROM conn_log
WHERE source_ip = '10.120.32.14' AND destination_ip = '10.110.16.5' AND destination_port IN (445,135);
-- Full case: 142,890; practice preview: 2,500
SELECT COUNT(*) FROM dns_log
WHERE source_ip = '10.110.16.5' AND query LIKE '%.data-sync-telemetry.net' AND qtype = 'TXT';
```

```sql
-- Hunt 04 Drill: DNS High-Entropy Tunneling Detection
SELECT query, entropy, qtype, COUNT(*) as query_count
FROM dns_log
WHERE entropy > 4.2
GROUP BY query
ORDER BY entropy DESC
LIMIT 15;
```

### Option B: Security Onion / Elasticsearch / Kibana Import
The generator exports gzip-compressed Elastic Common Schema (ECS) formatted NDJSON files to `lab/hunt-data/`:
* `conn.ndjson.gz`
* `dns.ndjson.gz`
* `http.ndjson.gz`
* `ssl.ndjson.gz`

**Import caveat:** These are record-level NDJSON files, **not** Elasticsearch `_bulk` request bodies. `_bulk` needs an action/metadata line for each record, a concrete write target, and an authenticated endpoint configured for your lab. Piping these files directly to `_bulk` will fail. SQLite is the supported zero-setup learner workflow; do not claim a working Security Onion integration until a version-specific ingestion adapter is implemented and tested.

---

## 4. The Three Embedded Adversary Needles

| Hunt Module | Target Telemetry | Adversary Behavior | Mathematical Signature |
|---|---|---|---|
| **Hunt 02** | `conn_log`, `http_log` | CAD workstation `10.100.14.88` running unmanaged client `python-requests/2.28.1` to VPS `198.51.100.84:8080`. | Host Cardinality = 1; approximately 60-second jittered HTTP connections. |
| **Hunt 03** | `conn_log`, `ssl_log` | Engineering workstation `10.42.18.91` to `198.51.100.84:443`. | Exactly 642 TLS sessions; approximately 60-second jittered cadence within a seven-day investigation dataset. |
| **Hunt 04** | `ssl_log`, `dns_log` | Accounting server `10.100.40.12` domain fronting over Cloudflare CDN (`104.16.248.112`) + DNS tunneling. | Go runtime JA4 `t13d190800_2a27b87c7a10_e68c9e54a0f8`; DNS TXT label Shannon entropy $H = 4.72\text{ bits/char}$. |
| **Hunt 05 Capstone** | `conn_log`, `ssl_log`, `dns_log` | Chicago `10.120.32.14` to C2 `198.51.100.84:443`, then native SMB/RPC to Portland `10.110.16.5`, then DNS TXT exfil to `data-sync-telemetry.net`. | 3,840 roughly five-minute C2 sessions ($CV \approx 0.08$), 22 SMB/RPC sessions; 142,890 high-entropy 62-character TXT labels **with `--full-hunt05`** (otherwise 2,500). |
