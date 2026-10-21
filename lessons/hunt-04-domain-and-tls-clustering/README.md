# Hunt 04 — Domain & TLS Clustering

## At a glance

- **Part of:** [Book 2 — The Hunter's Eye](/BOOK-2.md) · Proactive Network Threat Hunting Track
- **Follows:** [Chapter 13 (Story) — The Forest and the Trees](/narrative/13-the-forest-and-the-trees.md)
- **Version:** 0.1 — draft
- **Date:** 2026-08-26
- **Capability targets:** TH-7 (Shannon Entropy on DNS), TH-8 (JA4/JA3 Handshake Stacking), IR-4 (CDN Discrimination & Domain Fronting)
- **Time:** about 2.5 hours
- **Workbench:** Security Onion Hunt, Kibana, Elasticsearch (KQL / Lucene / ES|QL), Zeek `dns.log` & `ssl.log`
- **Dataset:** 41,000 DNS queries and 22,000 TLS sessions from Accounting Server `10.100.40.12`

---

## The Situation: The Perimeter Blind Spot

When adversaries operate in modern enterprise environments:
1. **IP addresses fail as indicators:** Threat actors terminate outbound HTTPS channels on shared commercial CDNs (Cloudflare, Fastly, CloudFront, Azure Front Door). Blocking CDN IP addresses disrupts dozens of vital business applications and third-party SaaS services.
2. **Cleartext SNI is decoyed:** Using **domain fronting**, an implant sends a benign hostname in the cleartext `ClientHello` and DNS query, while hiding the true attacker-controlled origin in the encrypted HTTP `Host` header.
3. **DNS caching is deliberately broken:** When tunneling data over DNS, adversaries generate millions of unique subdomains to force corporate recursive resolvers to bypass their memory cache and query attacker-controlled authoritative nameservers on every request.

To detect these campaigns without relying on brittle IP blocklists, threat hunters must apply **mathematical information metrics (Shannon entropy)** and **client cryptographic fingerprinting (JA4)**.

---

## 1. Information Theory on the Wire: Shannon Entropy ($H$)

In natural human languages and standard corporate hostnames (`portal.harrowmere.com`, `api.github.com`), character frequencies are highly redundant and predictable. In contrast, automated tunneling tools (e.g., `dnscat2`, `iodine`, `Cobalt Strike DNS`) pack Base64, Base32, or hexadecimal-encoded binary data into the subdomain labels.

The Shannon entropy of a string $X$ is calculated as:

$$H(X) = -\sum_{i=1}^{n} P(x_i) \log_2 P(x_i)$$

Where $P(x_i)$ is the probability of character $x_i$ appearing in the string.

```text
Entropy Score (Bits / Char)
▲
│              ┌───────────────┐
│              │ TUNNELED DATA │  ◄── H(X) > 4.5 bits/char
│              │ (Base32/64/Hex│      Uniform distribution,
│              └───────────────┘      no vowel/consonant grammar.
│ ─────────────┴───────────────┴────────────────
│ ┌───────────────┐
│ │ BENIGN LABELS │  ◄── H(X) 2.0 to 3.2 bits/char
│ │ (Human/Cloud) │      High redundancy, repeating patterns.
│ └───────────────┘
└──────────────────────────────────────────────►
  Low Entropy ────────────────────► High Entropy
```

### High-Volume Query Rate + Cache-Busting
A high entropy score becomes a definitive indicator of DNS tunneling when paired with **resolver cache-busting**:
- Unique subdomain count per apex domain: $> 5,000$ in 24 hours.
- Cache hit ratio on local recursive resolver: $0\%$.

---

## 2. Client TLS Fingerprinting: JA4

While an adversary can trivially spoof the HTTP `User-Agent` string, altering the cryptographic handshake requires modifying the underlying client software and TLS library.

The **JA4 fingerprint** formats client `ClientHello` parameters into an inspectable 36-character string:

$$\underbrace{\text{t13d190800}}_{\text{Transport / TLS / SNI / Ciphers / Exts}}\_\underbrace{\text{2a27b87c7a10}}_{\text{Cipher Hash}}\_\underbrace{\text{e68c9e54a0f8}}_{\text{Extension Hash}}$$

```
Field Breakdown (t13d190800):
- 't'  : TCP transport protocol
- '13' : TLS version 1.3
- 'd'  : Domain SNI present (cleartext destination name)
- '19' : Number of cipher suites offered (19 ciphers)
- '08' : Number of TLS extensions present (8 extensions)
- '00' : First and last ALPN extension values
```

### Stacking JA4 Against Enterprise Baselines
By aggregating `tls.ja4` counts across a subnet:
- 98% of traffic matches known browser signatures (`Chrome`, `Edge`, `Safari`).
- Anomalous low-cardinality JA4 hashes (e.g., standard `Go crypto/tls` or `Python requests`) immediately unmask unauthorized scripts operating from production servers.

---

## 3. Interactive Micro-Drills

### Drill H4.1: DNS Entropy Spotting Rep (30-Second Triage)

Evaluate the three domain query streams below. Which stream indicates active **DNS exfiltration / tunneling**, and why?

```
Stream 1:
- Queries: update-v1.prod.harrowmere.internal, update-v2.prod.harrowmere.internal
- Unique Subdomains: 2
- Shannon Entropy: 2.31 bits/char
- Resolver Cache Hits: 99.4%

Stream 2:
- Queries: 8492048201.us-east-1.elb.amazonaws.com, 1029482019.us-east-1.elb.amazonaws.com
- Unique Subdomains: 8
- Shannon Entropy: 3.12 bits/char
- Resolver Cache Hits: 65.0%

Stream 3:
- Queries: a7f901b4c8e219.data-relay.example, k83m90px12vz88.data-relay.example, q901baef48209c.data-relay.example
- Unique Subdomains: 41,200
- Shannon Entropy: 4.74 bits/char
- Resolver Cache Hits: 0.0%
```

<details class="reveal-gate">
  <summary>🔍 Check Evaluation Key</summary>
  <div class="reveal-content">
    <p><strong>Answer: Stream 3.</strong></p>
    <ul>
      <li><strong>Stream 1</strong> is internal operational traffic: very low entropy (2.31) with high cache utilization.</li>
      <li><strong>Stream 2</strong> is standard AWS Elastic Load Balancer dynamic addressing: moderate entropy (3.12), small cardinality (8 unique names), and legitimate cloud infrastructure.</li>
      <li><strong>Stream 3</strong> exhibits the undeniable signature of DNS tunneling: extreme entropy (4.74 bits/char indicating Base64/Base32 encoded payloads), massive query cardinality (41,200 unique subdomains under a single root apex), and complete cache-busting (0.0% hit rate).</li>
    </ul>
  </div>
</details>

---

## 4. The Covert Channel Discrimination Report (Deliverable)

When documenting an adversary leveraging domain fronting and DNS tunneling, submit a structured **Covert Channel Discrimination Report**:

```markdown
### COVERT CHANNEL DISCRIMINATION REPORT
1. Target System: 10.100.40.12 (Internal Accounting Staging Server)
2. Remote Infrastructure: AS13335 (Cloudflare CDN Edge IPs)
3. Apex Domain Under Tunneling: data-relay.example

TELEMETRY CONVERGENCE:
- DNS Tunneling Metric: 41,200 unique queries to apex; mean Shannon entropy = 4.74 bits/char (serialized payload).
- Resolver Impact: 100% cache-miss rate, turning internal recursive resolvers into external exfiltration relays.
- Client TLS Verification: Outbound HTTPS sessions generate JA4 fingerprint `t13d190800_2a27b87c7a10_e68c9e54a0f8` (Go crypto/tls library).
- Evasion Technique: Domain fronting across shared CDN; SNI header reflects benign SaaS domain while inner requests target unclassified origin.

CONTAINMENT & REMEDIATION:
- Sever 10.100.40.12 at switch port; preserve volatile RAM.
- Deploy RPZ (Response Policy Zone) sinkhole for apex domain `data-relay.example` at internal recursive resolvers.
- Author Sigma / Elastic rule alerting on JA4 fingerprint `t13d190800_2a27b87c7a10_e68c9e54a0f8` originating from server subnets.
```

---

<div class="bridge-card">
  <div class="bridge-label">Next Module in Book 2</div>
  <div class="bridge-title">Chapter 14 — The Hunter's Crucible</div>
  <p class="bridge-desc">The final test of Book 2: a 14-day unguided enterprise dataset across three physical campuses. No tickets, no hints, no alerts. Synthesize all five hunting disciplines to expose three concurrent adversary campaigns.</p>
  <a href="#/narrative/14-the-hunters-crucible" class="bridge-btn">Continue to Chapter 14 Story →</a>
</div>
