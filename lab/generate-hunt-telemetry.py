#!/usr/bin/env python3
"""
generate-hunt-telemetry.py — Authentic Enterprise Telemetry Simulator for NADF Book 2

Generates realistic network telemetry modeling Harrowmere Equipment Group:
  1. Head (95% volume): Power-law Pareto distribution of corporate web/cloud traffic
     (Chrome/Edge browsers, Microsoft 365, Google Workspace, AWS CloudFront, internal Active Directory).
  2. Torso (5% volume): Legitimate administrative jobs (Dave Henderson's CAD video streams,
     Priya's Azure DB backup, Leah's ERP sync, Marcus Whitlock's Rust crate downloads).
  3. Long Tail (0.01% volume): Administrative weirdness (Portland 2011 basement boiler NTP checks,
     HP LaserJet SNMP sweeps).
  4. Three Embedded Adversary Campaigns:
     - Campaign 1 (Hunts 02 & 03): distinct CAD hosts 10.100.14.88 (HTTP 8080)
       and 10.42.18.91 (642 TLS sessions) with jittered 60-second beacons.
     - Campaign 2 (Hunt 04): Staging server 10.100.40.12 using domain fronting on Cloudflare CDN
       with Go JA4 fingerprint 't13d190800_2a27b87c7a10_e68c9e54a0f8' and 10,000+ high-entropy
       DNS tunneling queries (Shannon entropy H > 4.6 bits/symbol).
     - Campaign 3 (Hunt 05 Capstone): Chicago workstation 10.120.32.14 sends
       3,840 TLS beacons, then 22 SMB/RPC sessions across IPsec to Portland
       repository 10.110.16.5. Portland sends 62-character DNS TXT payloads;
       --full-hunt05 emits all 142,890 learner-case queries.

Zero external dependencies — standard library only (sqlite3, json, gzip, csv, math, random).
"""

import argparse
import csv
import datetime
import gzip
import io
import json
import math
import os
import random
import sqlite3
import sys

# -----------------------------------------------------------------------------
# Environmental Constants: Harrowmere Equipment Group
# -----------------------------------------------------------------------------
SUBNETS = {
    "corp_hq": "10.100.0.0/16",
    "portland_wh": "10.110.0.0/16",
    "chicago_mfg": "10.120.0.0/16",
    "cad_pool": "10.100.14.0/24",
    "engineering": "10.42.18.0/24",
    "accounting": "10.100.40.0/24",
}

RESOLVERS = ["10.100.1.10", "10.100.1.11"]

# Top-talker cloud and corporate destinations (Head)
HEAD_DESTINATIONS = [
    {"ip": "13.107.42.12", "domain": "login.microsoftonline.com", "port": 443, "proto": "tcp", "service": "ssl"},
    {"ip": "52.96.166.130", "domain": "outlook.office365.com", "port": 443, "proto": "tcp", "service": "ssl"},
    {"ip": "142.250.190.46", "domain": "mail.google.com", "port": 443, "proto": "tcp", "service": "ssl"},
    {"ip": "142.250.190.78", "domain": "drive.google.com", "port": 443, "proto": "tcp", "service": "ssl"},
    {"ip": "104.16.248.112", "domain": "cdnjs.cloudflare.com", "port": 443, "proto": "tcp", "service": "ssl"},
    {"ip": "104.16.249.112", "domain": "api.cloudflare.com", "port": 443, "proto": "tcp", "service": "ssl"},
    {"ip": "151.101.1.140", "domain": "reddit.map.fastly.net", "port": 443, "proto": "tcp", "service": "ssl"},
    {"ip": "10.100.1.20", "domain": "dc01.harrowmere.internal", "port": 88, "proto": "tcp", "service": "kerberos"},
    {"ip": "10.100.1.20", "domain": "dc01.harrowmere.internal", "port": 389, "proto": "tcp", "service": "ldap"},
    {"ip": "10.100.1.25", "domain": "files.harrowmere.internal", "port": 445, "proto": "tcp", "service": "smb"},
]

USER_AGENTS_HEAD = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.5 Safari/605.1.15",
]

JA4_HEAD = [
    "t13d1516h2_8daaf6152771_b5da04f6479a",  # Chrome
    "t13d1715h2_55b3f1e94112_c8da03f8191b",  # Edge
]

def shannon_entropy(data_str: str) -> float:
    """Calculate the Shannon entropy H(X) in bits per character."""
    if not data_str:
        return 0.0
    entropy = 0.0
    length = len(data_str)
    freq = {}
    for c in data_str:
        freq[c] = freq.get(c, 0) + 1
    for count in freq.values():
        p = count / length
        entropy -= p * math.log2(p)
    return entropy


# -----------------------------------------------------------------------------
# Telemetry Generation Engine
# -----------------------------------------------------------------------------
class HarrowmereTelemetryGenerator:
    def __init__(self, total_events=100000, days=14, seed=None, start_time=None,
                 full_hunt05=False):
        self.total_events = total_events
        self.days = days
        self.rng = random.Random(seed)
        self.full_hunt05 = full_hunt05
        # Explicit start + seed makes the same case replayable across sessions.
        # Otherwise the rolling window keeps the original default behavior.
        self.start_time = (
            start_time if start_time is not None
            else datetime.datetime.now(datetime.timezone.utc).replace(tzinfo=None) - datetime.timedelta(days=days)
        )
        self.conn_logs = []
        self.dns_logs = []
        self.http_logs = []
        self.ssl_logs = []
        
        # Internal hosts pool (~1,800 machines across 3 campuses)
        self.internal_hosts = []
        for _ in range(1200):
            self.internal_hosts.append(f"10.100.{self.rng.randint(10, 80)}.{self.rng.randint(2, 250)}")
        for _ in range(350):
            self.internal_hosts.append(f"10.110.{self.rng.randint(10, 30)}.{self.rng.randint(2, 250)}")
        for _ in range(250):
            self.internal_hosts.append(f"10.120.{self.rng.randint(10, 40)}.{self.rng.randint(2, 250)}")

    def generate_all(self):
        print(f"[*] Generating {self.total_events} events across {self.days}-day enterprise baseline...")
        self._generate_head_traffic()
        self._generate_torso_traffic()
        self._generate_long_tail_weirdness()
        self._embed_campaign_1_beacon()
        self._embed_campaign_2_domain_fronting()
        self._embed_campaign_3_capstone()
        print(f"[+] Total records synthesized:")
        print(f"    - conn.log: {len(self.conn_logs):,}")
        print(f"    - dns.log:  {len(self.dns_logs):,}")
        print(f"    - http.log: {len(self.http_logs):,}")
        print(f"    - ssl.log:  {len(self.ssl_logs):,}")

    def _random_timestamp(self, day_offset=None, hour=None):
        if day_offset is None:
            day_offset = self.rng.uniform(0, self.days)
        base = self.start_time + datetime.timedelta(days=day_offset)
        if hour is not None:
            base = base.replace(hour=hour, minute=self.rng.randint(0, 59), second=self.rng.randint(0, 59))
        else:
            # Business hours skew (Pareto during 08:00 - 18:00)
            if self.rng.random() < 0.85:
                base = base.replace(hour=self.rng.randint(8, 17))
            else:
                base = base.replace(hour=self.rng.choice(list(range(0, 8)) + list(range(18, 24))))
        return base.strftime("%Y-%m-%dT%H:%M:%S.%fZ")

    def _generate_head_traffic(self):
        head_count = int(self.total_events * 0.90)
        for _ in range(head_count):
            src_ip = self.rng.choice(self.internal_hosts)
            dest = self.rng.choice(HEAD_DESTINATIONS)
            ts = self._random_timestamp()
            duration = round(self.rng.expovariate(1.0 / 2.5) + 0.05, 4)
            orig_bytes = self.rng.randint(350, 4200)
            resp_bytes = self.rng.randint(1200, 85000)
            
            conn_entry = {
                "@timestamp": ts,
                "source.ip": src_ip,
                "source.port": self.rng.randint(49152, 65535),
                "destination.ip": dest["ip"],
                "destination.port": dest["port"],
                "network.transport": dest["proto"],
                "service": dest["service"],
                "duration": duration,
                "source.bytes": orig_bytes,
                "destination.bytes": resp_bytes,
                "conn_state": "SF"
            }
            self.conn_logs.append(conn_entry)

            if dest["service"] == "ssl":
                ja4 = self.rng.choice(JA4_HEAD)
                self.ssl_logs.append({
                    "@timestamp": ts,
                    "source.ip": src_ip,
                    "destination.ip": dest["ip"],
                    "destination.port": 443,
                    "server_name": dest["domain"],
                    "tls.ja4": ja4,
                    "tls.version": "1.3"
                })
            
            # Associated DNS query for destination domain
            if self.rng.random() < 0.35:  # Cache hit prevents lookup every time
                self.dns_logs.append({
                    "@timestamp": ts,
                    "source.ip": src_ip,
                    "destination.ip": self.rng.choice(RESOLVERS),
                    "dns.question.name": dest["domain"],
                    "dns.question.type": "A",
                    "dns.response.code": "NOERROR",
                    "dns.answers": [dest["ip"]],
                    "entropy": round(shannon_entropy(dest["domain"].split(".")[0]), 2)
                })

    def _generate_torso_traffic(self):
        # 1. Dave Henderson CAD video streaming (48.2 GB to AWS CloudFront)
        for day in range(3):
            ts = self._random_timestamp(day_offset=day, hour=14)
            self.conn_logs.append({
                "@timestamp": ts,
                "source.ip": "10.100.12.44",
                "source.port": 51240,
                "destination.ip": "52.84.120.45",
                "destination.port": 443,
                "network.transport": "tcp",
                "service": "ssl",
                "duration": 39600.0,
                "source.bytes": 1845000,
                "destination.bytes": 48200000000,
                "conn_state": "SF"
            })
            self.http_logs.append({
                "@timestamp": ts,
                "source.ip": "10.100.12.44",
                "destination.ip": "52.84.120.45",
                "user_agent.original": USER_AGENTS_HEAD[0]
            })

        # 2. Priya's Azure database replication (18.6 GB on Sunday midnight)
        ts_sunday = self.start_time.replace(hour=0, minute=0, second=10).strftime("%Y-%m-%dT%H:%M:%S.%fZ")
        self.conn_logs.append({
            "@timestamp": ts_sunday,
            "source.ip": "10.100.1.25",
            "source.port": 49820,
            "destination.ip": "20.42.112.90",
            "destination.port": 443,
            "network.transport": "tcp",
            "service": "ssl",
            "duration": 7200.0,
            "source.bytes": 18600000000,
            "destination.bytes": 420000,
            "conn_state": "SF"
        })

        # 3. Marcus Whitlock Rust crate package downloads (single connection, rare European IP)
        ts_marcus = self._random_timestamp(day_offset=2, hour=11)
        self.conn_logs.append({
            "@timestamp": ts_marcus,
            "source.ip": "10.100.42.18",
            "source.port": 54210,
            "destination.ip": "195.201.24.18",
            "destination.port": 80,
            "network.transport": "tcp",
            "service": "http",
            "duration": 0.42,
            "source.bytes": 312,
            "destination.bytes": 140,
            "conn_state": "SF"
        })
        self.http_logs.append({
            "@timestamp": ts_marcus,
            "source.ip": "10.100.42.18",
            "destination.ip": "195.201.24.18",
            "user_agent.original": "cargo/1.75.0 (x86_64-pc-windows-msvc)"
        })

    def _generate_long_tail_weirdness(self):
        # 1. Portland warehouse 2011 heating boiler controller (Tuesdays at 03:00, 128 bytes, no DNS)
        for t_day in [2, 9]:
            ts_boiler = (self.start_time + datetime.timedelta(days=t_day)).replace(
                hour=3, minute=0, second=self.rng.randint(2, 8)
            ).strftime("%Y-%m-%dT%H:%M:%S.%fZ")
            self.conn_logs.append({
                "@timestamp": ts_boiler,
                "source.ip": "10.110.4.99",
                "source.port": 1025,
                "destination.ip": "198.18.2.45",
                "destination.port": 123,
                "network.transport": "udp",
                "service": "ntp",
                "duration": 0.02,
                "source.bytes": 128,
                "destination.bytes": 128,
                "conn_state": "SF"
            })

        # 2. HP LaserJet printer SNMP sweeps (10.100.12.15 -> internal print server)
        for d in range(self.days):
            ts_snmp = self._random_timestamp(day_offset=d, hour=4)
            self.conn_logs.append({
                "@timestamp": ts_snmp,
                "source.ip": "10.100.12.15",
                "source.port": 161,
                "destination.ip": "10.100.1.5",
                "destination.port": 161,
                "network.transport": "udp",
                "service": "snmp",
                "duration": 0.01,
                "source.bytes": 84,
                "destination.bytes": 84,
                "conn_state": "SF"
            })

    def _embed_campaign_1_beacon(self):
        # Hunt 02: CAD Workstation 10.100.14.88, HTTP port 8080.
        # Jittered C2 Beacon: sleep = 60s, jitter = ±20% -> bounds: [48s, 72s], CV ~ 0.115
        base_time = self.start_time
        target_ip = "10.100.14.88"
        dest_ip = "198.51.100.84"
        dest_port = 8080
        
        # Bounded 60-second HTTP preview stream retained for Hunt 02.
        current_time = base_time
        end_time = base_time + datetime.timedelta(days=7)
        while current_time < end_time and len(self.conn_logs) < self.total_events + 700:
            jitter = self.rng.uniform(-0.20, 0.20)
            delta = 60.0 * (1.0 + jitter)  # 48.0 to 72.0 seconds
            current_time += datetime.timedelta(seconds=delta)
            ts = current_time.strftime("%Y-%m-%dT%H:%M:%S.%fZ")
            
            self.conn_logs.append({
                "@timestamp": ts,
                "source.ip": target_ip,
                "source.port": self.rng.randint(49152, 65535),
                "destination.ip": dest_ip,
                "destination.port": dest_port,
                "network.transport": "tcp",
                "service": "http",
                "duration": round(self.rng.uniform(0.18, 0.45), 4),
                "source.bytes": self.rng.randint(248, 312),
                "destination.bytes": self.rng.randint(140, 180),
                "conn_state": "SF"
            })
            self.http_logs.append({
                "@timestamp": ts,
                "source.ip": target_ip,
                "destination.ip": dest_ip,
                "user_agent.original": "python-requests/2.28.1"
            })

        # Hunt 03's authored case is a DIFFERENT engineering workstation.
        # Its 642 TLS sessions form a ~11-hour cluster within a seven-day
        # investigation window; do not confuse it with Hunt 02's HTTP stream.
        current_time = base_time + datetime.timedelta(days=2, hours=8)
        for _ in range(642):
            current_time += datetime.timedelta(seconds=60 * self.rng.uniform(0.8, 1.2))
            ts = current_time.strftime("%Y-%m-%dT%H:%M:%S.%fZ")
            self.conn_logs.append({
                "@timestamp": ts,
                "source.ip": "10.42.18.91",
                "source.port": self.rng.randint(49152, 65535),
                "destination.ip": dest_ip,
                "destination.port": 443,
                "network.transport": "tcp",
                "service": "ssl",
                "duration": round(self.rng.uniform(0.18, 0.45), 4),
                "source.bytes": self.rng.randint(248, 312),
                "destination.bytes": self.rng.randint(140, 180),
                "conn_state": "SF"
            })
            self.ssl_logs.append({
                "@timestamp": ts,
                "source.ip": "10.42.18.91",
                "destination.ip": dest_ip,
                "destination.port": 443,
                "server_name": "update-assistant.cdn-service.com",
                "tls.ja4": "t13d1516h2_8daaf6152771_b5da04f6479a",
                "tls.version": "1.3"
            })

    def _embed_campaign_2_domain_fronting(self):
        # Hunt 04: Accounting Server 10.100.40.12 -> Cloudflare Anycast CDN
        # Domain fronting with JA4 't13d190800_2a27b87c7a10_e68c9e54a0f8' (Go crypto/tls)
        # High-entropy DNS Tunneling to *.data-relay.example (H > 4.6 bits)
        target_ip = "10.100.40.12"
        cdn_ips = ["104.16.248.112", "104.16.249.112", "172.67.182.204"]
        ja4_go = "t13d190800_2a27b87c7a10_e68c9e54a0f8"
        
        # 1,200 TLS sessions over CDN
        for i in range(1200):
            ts = self._random_timestamp(day_offset=self.rng.uniform(10, 14))
            dest = self.rng.choice(cdn_ips)
            self.conn_logs.append({
                "@timestamp": ts,
                "source.ip": target_ip,
                "source.port": self.rng.randint(49152, 65535),
                "destination.ip": dest,
                "destination.port": 443,
                "network.transport": "tcp",
                "service": "ssl",
                "duration": round(self.rng.uniform(0.2, 0.8), 4),
                "source.bytes": self.rng.randint(450, 920),
                "destination.bytes": self.rng.randint(1200, 2400),
                "conn_state": "SF"
            })
            self.ssl_logs.append({
                "@timestamp": ts,
                "source.ip": target_ip,
                "destination.ip": dest,
                "server_name": "corporate-portal.cdn-service.com",  # Decoy front SNI
                "tls.ja4": ja4_go,
                "tls.version": "1.3"
            })

        # 3,500 DNS tunneling queries with Base32/Alphanumeric high entropy
        b32_chars = "abcdefghijklmnopqrstuvwxyz234567-0189"
        for i in range(3500):
            ts = self._random_timestamp(day_offset=self.rng.uniform(10, 14))
            # Serialized encrypted payload label (62 chars)
            subdomain = "".join(self.rng.choice(b32_chars) for _ in range(62))
            fqdn = f"{subdomain}.data-relay.example"
            ent = shannon_entropy(subdomain)
            self.dns_logs.append({
                "@timestamp": ts,
                "source.ip": target_ip,
                "destination.ip": self.rng.choice(RESOLVERS),
                "dns.question.name": fqdn,
                "dns.question.type": "TXT",
                "dns.response.code": "NOERROR",
                "dns.answers": ["v=spf1 ..."],
                "entropy": round(ent, 3)
            })

    def _embed_campaign_3_capstone(self):
        # Hunt 05 Capstone:
        # Step 1: Chicago 10.120.32.14 C2 beacon (300s sleep ± 15% jitter)
        # Step 2: Chicago -> Portland 10.110.16.5 lateral movement via native SMB (TCP 445)
        # Step 3: Portland 10.110.16.5 -> data-sync-telemetry.net DNS TXT exfil
        chicago_host = "10.120.32.14"
        portland_host = "10.110.16.5"

        # Exact case count and tight 300s rhythm from Hunt 05's narrative.
        # A fixed 14-day window holds this ~13.34-day series. A 14-day
        # baseline is required for the authored capstone; shorter synthetic
        # windows are useful for smoke tests, not full case reproduction.
        current_time = self.start_time + datetime.timedelta(minutes=5)
        for _ in range(3840):
            current_time += datetime.timedelta(seconds=300.2 + self.rng.uniform(-41.7, 41.7))
            ts = current_time.strftime("%Y-%m-%dT%H:%M:%S.%fZ")
            self.conn_logs.append({
                "@timestamp": ts,
                "source.ip": chicago_host,
                "source.port": self.rng.randint(49152, 65535),
                "destination.ip": "198.51.100.84",
                "destination.port": 443,
                "network.transport": "tcp",
                "service": "ssl",
                "duration": round(self.rng.uniform(0.15, 0.5), 4),
                "source.bytes": self.rng.randint(300, 420),
                "destination.bytes": self.rng.randint(120, 180),
                "conn_state": "SF"
            })
            self.ssl_logs.append({
                "@timestamp": ts,
                "source.ip": chicago_host,
                "destination.ip": "198.51.100.84",
                "destination.port": 443,
                "server_name": "telemetry.microsoft-cdn.example",
                "tls.ja4": "t13d1516h2_3d3c9e9a94fb_4c4d88d87933",
                "tls.version": "1.3"
            })
        
        # 22 distinct cross-campus sessions, beginning Day 4 at 02:14.
        # SMB and RPC are both represented rather than implied by comments.
        for i in range(22):
            ts_lat = (self.start_time + datetime.timedelta(
                days=4 + (i // 8), hours=2, minutes=14 + (i % 8) * 4
            )).strftime("%Y-%m-%dT%H:%M:%S.%fZ")
            port = 135 if i % 4 == 3 else 445
            self.conn_logs.append({
                "@timestamp": ts_lat,
                "source.ip": chicago_host,
                "source.port": self.rng.randint(49152, 65535),
                "destination.ip": portland_host,
                "destination.port": port,
                "network.transport": "tcp",
                "service": "rpc" if port == 135 else "smb",
                "duration": round(self.rng.uniform(12.5, 84.0), 2),
                "source.bytes": self.rng.randint(45000, 185000),
                "destination.bytes": self.rng.randint(120000, 4800000),
                "conn_state": "SF"
            })

        # Default preview is intentionally cheap; full-fidelity capstone
        # explicitly reproduces 142,890 DNS queries cited by the lessons.
        # Select high-entropy simulated payloads in a narrow, documented
        # band so the observed mean resembles the authored ~4.86 case.
        # This is synthetic case construction, NOT evidence of real exfil.
        b32_chars = "abcdefghijklmnopqrstuvwxyz234567-0189"
        dns_count = 142890 if self.full_hunt05 else 2500
        for i in range(dns_count):
            ts = self._random_timestamp(day_offset=self.rng.uniform(7, 14), hour=self.rng.randint(1, 4))
            while True:
                subdomain = "".join(self.rng.choices(b32_chars, k=62))
                ent = shannon_entropy(subdomain)
                if 4.82 <= ent <= 4.90:
                    break
            fqdn = f"{subdomain}.data-sync-telemetry.net"
            self.dns_logs.append({
                "@timestamp": ts,
                "source.ip": portland_host,
                "destination.ip": self.rng.choice(RESOLVERS),
                "dns.question.name": fqdn,
                "dns.question.type": "TXT",
                "dns.response.code": "NOERROR",
                "dns.answers": ["OK"],
                "entropy": round(ent, 3)
            })

    # -------------------------------------------------------------------------
    # Output Serializers: SQLite, NDJSON (Gzip), CSV
    # -------------------------------------------------------------------------
    def export_sqlite(self, db_path):
        print(f"[*] Exporting telemetry to SQLite: {db_path}...")
        if os.path.exists(db_path):
            os.remove(db_path)
        conn = sqlite3.connect(db_path)
        cur = conn.cursor()

        # Create Tables with proper Threat Hunting indexes
        cur.execute("""
            CREATE TABLE conn_log (
                timestamp TEXT,
                source_ip TEXT,
                source_port INTEGER,
                destination_ip TEXT,
                destination_port INTEGER,
                proto TEXT,
                service TEXT,
                duration REAL,
                orig_bytes INTEGER,
                resp_bytes INTEGER,
                conn_state TEXT
            )
        """)
        cur.execute("CREATE INDEX idx_conn_dest ON conn_log(destination_ip, destination_port)")
        cur.execute("CREATE INDEX idx_conn_src ON conn_log(source_ip)")
        cur.execute("CREATE INDEX idx_conn_time ON conn_log(timestamp)")

        cur.execute("""
            CREATE TABLE dns_log (
                timestamp TEXT,
                source_ip TEXT,
                resolver_ip TEXT,
                query TEXT,
                qtype TEXT,
                rcode TEXT,
                answers TEXT,
                entropy REAL
            )
        """)
        cur.execute("CREATE INDEX idx_dns_query ON dns_log(query)")
        cur.execute("CREATE INDEX idx_dns_entropy ON dns_log(entropy)")

        cur.execute("""
            CREATE TABLE http_log (
                timestamp TEXT,
                source_ip TEXT,
                destination_ip TEXT,
                user_agent TEXT
            )
        """)
        cur.execute("CREATE INDEX idx_http_ua ON http_log(user_agent)")

        cur.execute("""
            CREATE TABLE ssl_log (
                timestamp TEXT,
                source_ip TEXT,
                destination_ip TEXT,
                server_name TEXT,
                ja4 TEXT,
                version TEXT
            )
        """)
        cur.execute("CREATE INDEX idx_ssl_ja4 ON ssl_log(ja4)")

        # Batch Insert
        cur.executemany(
            "INSERT INTO conn_log VALUES (:timestamp, :source_ip, :source_port, :destination_ip, :destination_port, :proto, :service, :duration, :orig_bytes, :resp_bytes, :conn_state)",
            [{
                "timestamp": r["@timestamp"], "source_ip": r["source.ip"], "source_port": r["source.port"],
                "destination_ip": r["destination.ip"], "destination_port": r["destination.port"],
                "proto": r["network.transport"], "service": r["service"], "duration": r["duration"],
                "orig_bytes": r["source.bytes"], "resp_bytes": r["destination.bytes"], "conn_state": r["conn_state"]
            } for r in self.conn_logs]
        )

        cur.executemany(
            "INSERT INTO dns_log VALUES (:timestamp, :source_ip, :resolver_ip, :query, :qtype, :rcode, :answers, :entropy)",
            [{
                "timestamp": r["@timestamp"], "source_ip": r["source.ip"], "resolver_ip": r["destination.ip"],
                "query": r["dns.question.name"], "qtype": r["dns.question.type"], "rcode": r["dns.response.code"],
                "answers": ",".join(r.get("dns.answers", [])), "entropy": r["entropy"]
            } for r in self.dns_logs]
        )

        cur.executemany(
            "INSERT INTO http_log VALUES (:timestamp, :source_ip, :destination_ip, :user_agent)",
            [{
                "timestamp": r["@timestamp"], "source_ip": r["source.ip"], "destination_ip": r["destination.ip"],
                "user_agent": r["user_agent.original"]
            } for r in self.http_logs]
        )

        cur.executemany(
            "INSERT INTO ssl_log VALUES (:timestamp, :source_ip, :destination_ip, :server_name, :ja4, :version)",
            [{
                "timestamp": r["@timestamp"], "source_ip": r["source.ip"], "destination_ip": r["destination.ip"],
                "server_name": r["server_name"], "ja4": r["tls.ja4"], "version": r["tls.version"]
            } for r in self.ssl_logs]
        )

        conn.commit()
        conn.close()
        print(f"[+] SQLite database written successfully: {os.path.getsize(db_path):,} bytes")

    def export_ndjson_gz(self, out_dir):
        print(f"[*] Exporting compressed ECS NDJSON to directory: {out_dir}...")
        os.makedirs(out_dir, exist_ok=True)
        
        files = {
            "conn.ndjson.gz": self.conn_logs,
            "dns.ndjson.gz": self.dns_logs,
            "http.ndjson.gz": self.http_logs,
            "ssl.ndjson.gz": self.ssl_logs
        }
        for fname, dataset in files.items():
            fpath = os.path.join(out_dir, fname)
            # Suppress changing gzip timestamps and output-path names in the header.
            with open(fpath, "wb") as raw:
                with gzip.GzipFile(fileobj=raw, mode="wb", filename="", mtime=0) as compressed:
                    with io.TextIOWrapper(compressed, encoding="utf-8", newline="\n") as gz:
                        for record in dataset:
                            gz.write(json.dumps(record) + "\n")
            print(f"    - {fname}: {os.path.getsize(fpath):,} bytes ({len(dataset):,} records)")

    # -------------------------------------------------------------------------
    # Verification Test Suite: Mathematical Proof of Needle Detectability
    # -------------------------------------------------------------------------
    def run_verification(self):
        # Python -O strips bare assert statements. These are production
        # validation gates, so they must still run in optimized Python.
        def require(condition, message):
            if not condition:
                raise AssertionError(message)

        print("\n=======================================================")
        print("  HUNT TELEMETRY VERIFICATION & DISCRIMINATION AUDIT")
        print("=======================================================")
        
        # 1. Audit Hunt 02: User-Agent Least Frequency Cardinality
        ua_counts = {}
        ua_hosts = {}
        for r in self.http_logs:
            ua = r["user_agent.original"]
            ua_counts[ua] = ua_counts.get(ua, 0) + 1
            ua_hosts.setdefault(ua, set()).add(r["source.ip"])
        
        print("\n[Audit 1: Least-Frequency Analysis / User-Agent Stacking]")
        sorted_ua = sorted(ua_counts.items(), key=lambda x: x[1])
        for ua, count in sorted_ua[:5]:
            card = len(ua_hosts[ua])
            print(f"  - Count: {count:<6} | Host Cardinality: {card:<4} | UA: {ua[:60]}")
        
        top_rare_ua = sorted_ua[0][0]
        require(top_rare_ua == "cargo/1.75.0 (x86_64-pc-windows-msvc)" or
                "python-requests" in top_rare_ua, "Outlier UA not isolated!")
        require(len(ua_hosts[top_rare_ua]) == 1,
                "Host cardinality must be 1 for the rare User-Agent!")
        print("  -> PASS: Outlier User-Agent exhibits Cardinality == 1.")

        # 2. Audit Hunt 03: Beacon Delta-Time Distribution & Jitter
        print("\n[Audit 2: Beacon Timing Delta-Time & Jitter Profiling]")
        beacon_events = [r for r in self.conn_logs if r["source.ip"] == "10.100.14.88" and r["destination.ip"] == "198.51.100.84"]
        beacon_events.sort(key=lambda x: x["@timestamp"])
        require(len(beacon_events) >= 2, "Beacon events missing or insufficient for jitter audit!")
        
        deltas = []
        for i in range(1, len(beacon_events)):
            t1 = datetime.datetime.strptime(beacon_events[i-1]["@timestamp"], "%Y-%m-%dT%H:%M:%S.%fZ")
            t2 = datetime.datetime.strptime(beacon_events[i]["@timestamp"], "%Y-%m-%dT%H:%M:%S.%fZ")
            deltas.append((t2 - t1).total_seconds())

        if deltas:
            mean_delta = sum(deltas) / len(deltas)
            variance = sum((d - mean_delta) ** 2 for d in deltas) / len(deltas)
            std_dev = math.sqrt(variance)
            cv = std_dev / mean_delta
            min_d, max_d = min(deltas), max(deltas)
            print(f"  - Total Beacon Events: {len(beacon_events)}")
            print(f"  - Mean Interval (mean): {mean_delta:.2f} seconds (~60s)")
            print(f"  - Std Deviation (std):  {std_dev:.2f} seconds")
            print(f"  - Bounds:               [{min_d:.2f}s, {max_d:.2f}s]")
            print(f"  - Coeff of Variation:   {cv:.3f}")
            require(0.05 < cv < 0.20, f"Beacon CV {cv} out of expected jitter bounds!")
            print(f"  -> PASS: Jittered beacon is mathematically distinct from human browsing (CV = {cv:.3f} < 0.20).")

        # 3. Audit Hunt 04: Shannon Entropy on DNS Query Labels
        print("\n[Audit 3: Shannon Entropy on DNS Tunneling Queries]")
        normal_queries = [r["entropy"] for r in self.dns_logs if "data-relay" not in r["dns.question.name"] and "data-sync" not in r["dns.question.name"]]
        tunnel_queries = [r["entropy"] for r in self.dns_logs if "data-relay" in r["dns.question.name"]]
        require(normal_queries, "Benign DNS baseline missing; cannot verify entropy separation!")
        
        avg_normal_ent = sum(normal_queries) / len(normal_queries) if normal_queries else 0
        avg_tunnel_ent = sum(tunnel_queries) / len(tunnel_queries) if tunnel_queries else 0
        
        print(f"  - Benign Domains Mean Entropy:   {avg_normal_ent:.3f} bits/symbol (Expected < 3.2)")
        print(f"  - Tunneling Subdomains Entropy:  {avg_tunnel_ent:.3f} bits/symbol (Expected > 4.5)")
        require(avg_tunnel_ent > 4.5, "Tunneling entropy too low!")
        require(avg_normal_ent < 3.5, "Normal domain entropy too high!")
        print("  -> PASS: Shannon entropy clearly discriminates covert tunneling from benign hostnames.")
        print("\n[+] ALL AUDIT CHECKS PASSED: Needles are authentic and mathematically detectable.")
        print("=======================================================\n")


# -----------------------------------------------------------------------------
# Main CLI Entrypoint
# -----------------------------------------------------------------------------
def main():
    def start_date(value):
        try:
            return datetime.datetime.strptime(value, "%Y-%m-%d")
        except ValueError as exc:
            raise argparse.ArgumentTypeError("start date must be YYYY-MM-DD") from exc

    parser = argparse.ArgumentParser(description="NADF Book 2 Threat Hunting Telemetry Generator")
    parser.add_argument("--count", "-n", type=int, default=100000, help="Total events to generate (default: 100,000)")
    parser.add_argument("--days", "-d", type=int, default=14, help="Capture time window in days (default: 14)")
    parser.add_argument("--format", "-f", choices=["sqlite", "ndjson", "all"], default="all", help="Output format (default: all)")
    parser.add_argument("--out-dir", "-o", default="lab/hunt-data", help="Output directory (default: lab/hunt-data)")
    parser.add_argument("--verify", "-v", action="store_true", help="Run statistical discrimination test suite")
    parser.add_argument("--seed", type=int, help="Random seed for replayable host and event generation")
    parser.add_argument("--full-hunt05", action="store_true", help="Emit the exact 142,890 Hunt 05 TXT queries (default: 2,500-query fast preview)")
    parser.add_argument("--start-date", type=start_date, metavar="YYYY-MM-DD", help="First day of the synthetic case in UTC (pair with --seed to replay)")

    args = parser.parse_args()

    gen = HarrowmereTelemetryGenerator(
        total_events=args.count, days=args.days, seed=args.seed,
        start_time=args.start_date, full_hunt05=args.full_hunt05
    )
    gen.generate_all()

    os.makedirs(args.out_dir, exist_ok=True)

    if args.format in ["sqlite", "all"]:
        db_path = os.path.join(args.out_dir, "hunt_telemetry.db")
        gen.export_sqlite(db_path)

    if args.format in ["ndjson", "all"]:
        gen.export_ndjson_gz(args.out_dir)

    if args.verify:
        gen.run_verification()


if __name__ == "__main__":
    main()
