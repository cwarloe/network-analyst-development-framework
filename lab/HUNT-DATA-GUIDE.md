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
│                       Marcus Vance's Rust crate downloads (10.100.42.18).
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
```

### CLI Options:
* `--count, -n`: Total baseline events to synthesize (default: 100,000).
* `--days, -d`: Rolling time window in days (default: 14).
* `--format, -f`: Output target (`sqlite`, `ndjson`, or `all`).
* `--out-dir, -o`: Target output folder (default: `lab/hunt-data`).
* `--verify, -v`: Runs automated mathematical audits asserting needle detectability ($CV < 0.20$, entropy $H > 4.5$, cardinality == 1).

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
-- Hunt 03 Drill: Jittered Beacon Delta-Time Extraction
SELECT timestamp, source_ip, destination_ip, duration
FROM conn_log
WHERE source_ip = '10.100.14.88' AND destination_ip = '198.51.100.84'
ORDER BY timestamp ASC
LIMIT 20;
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

To ingest into an Elasticsearch / Security Onion cluster:

```bash
# Decompress and ingest into Elasticsearch
gunzip -c lab/hunt-data/conn.ndjson.gz | curl -s -H "Content-Type: application/x-ndjson" -XPOST "http://localhost:9200/so-zeek-conn-*/_bulk" --data-binary @-
```

---

## 4. The Three Embedded Adversary Needles

| Hunt Module | Target Telemetry | Adversary Behavior | Mathematical Signature |
|---|---|---|---|
| **Hunt 02 & Hunt 03** | `conn_log`, `http_log` | CAD workstation `10.100.14.88` running unmanaged client `python-requests/2.28.1` to VPS `198.51.100.84:8080`. | Host Cardinality = 1; Delta-time $\mu = 60.0\text{s}$, $CV = 0.116$ ($\pm 20\%$ jitter). |
| **Hunt 04** | `ssl_log`, `dns_log` | Accounting server `10.100.40.12` domain fronting over Cloudflare CDN (`104.16.248.112`) + DNS tunneling. | Go runtime JA4 `t13d190800_2a27b87c7a10_e68c9e54a0f8`; DNS TXT label Shannon entropy $H = 4.72\text{ bits/char}$. |
| **Hunt 05 Capstone** | Full Multi-Site Dataset | Chicago workstation `10.120.32.14` lateral movement via native SMB/RPC to Portland repository `10.110.16.5`, followed by recursive DNS exfiltration to `data-sync-telemetry.net`. | East-West IPsec SMB sessions; 2,500+ TXT queries to external apex with 62-char high-entropy subdomains ($H = 4.86\text{ bits}$). |
