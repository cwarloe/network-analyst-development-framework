# Chapter 13 — The Forest and the Trees

The third week of our proactive threat hunting sprint began not with an alert, but with an insurmountable wall of legitimate infrastructure.

On my primary console in the threat hunting pod, thirty-six hours of edge egress telemetry from Harrowmere’s financial operations and treasury subnet (`10.100.40.0/24`) sat rendered in the Security Onion interface. Cal Rowan’s Elasticsearch cluster had indexed just under four million outbound connections from the accounting wing over the weekend.

Following the outlier stacking routines Cal and Owen had drilled into me during the previous sprints, I had filtered out our documented SaaS providers and aggregated the remaining outbound traffic by destination IP address and connection volume.

A specific cluster of external destinations immediately stood out on my screen:

- `104.16.248.112`
- `104.16.249.112`
- `172.67.182.204`

Over twenty-two thousand outbound HTTPS connections had traversed our corporate firewalls to those three addresses in less than two days, originating almost entirely from a single internal host: `10.100.40.12`, an application staging server in the corporate accounting department.

My fingers hovered over my keyboard. After months of triage work in Tier-1, my muscle memory pulled toward the standard incident playbook. When an internal server generates persistent, unapproved outbound streams to external sockets, the protocol is straightforward: initiate immediate containment, copy the destination IPs into the perimeter firewall blocklist, and notify the server custodian.

I reached for the ticketing template, ready to submit an emergency firewall change request.

“Hold on, Ethan,” Dana Shah’s voice cut through the quiet hum of the pod.

Dana was standing behind my chair, a binder of architecture schematics tucked under her arm. She had been observing my monitor over my shoulder for the past two minutes.

“I’m submitting a containment ticket to block those three external destination IPs,” I said, turning to face her. “Server `10.100.40.12` has established over twenty thousand sessions to them since Saturday morning. That host only runs internal general ledger reconciliations. It has no operational business communicating with unapproved external hosting endpoints.”

Dana didn’t tell me I was wrong. Instead, she leaned forward and pointed at the three IP addresses in the Elasticsearch table.

“Before you touch the perimeter rules, open a terminal and run reverse lookups against those three addresses,” Dana instructed calmly. “Tell me what organizations own those netblocks.”

I opened a shell and queried our external resolver. The Autonomous System Number and registry allocation resolved in less than a second:

`AS13335 — Cloudflare, Inc.`

“It’s a commercial Content Delivery Network,” I said, looking back at her.

“Exactly,” Dana said. “Those three addresses are not private virtual private servers leased by an adversary in an unregulated hosting facility. They are anycast edge front-ends for a massive public CDN. Hundreds of thousands of different web applications, SaaS platforms, and enterprise services terminate their TLS sessions on those exact same IP sockets.”

She tapped the glass of my center monitor.

“If you push an emergency firewall block on those IP addresses right now, you will sever our connection to the external payment gateway our payroll team uses. You will kill our customer ticketing portal, and you will drop three cloud APIs that Leah Moreno’s logistics applications rely on every hour. When an adversary hides behind a modern content distribution network, destination IP addresses give you zero operational leverage. You cannot burn down the entire forest to cut down a single poisoned tree.”

I sat back, the initial rush of certainty draining away.

“If the IP address is shared by thousands of benign companies,” I asked, “how do we even know where the packets are actually going?”

“We look at the layers above the IP header,” a voice answered from the aisle.

Priya Raman, Harrowmere’s Senior Network Engineer, walked into the hunting pod holding a fresh telemetry printout from our edge core switches. She pulled over an empty rolling chair and sat down between Dana and me.

“Cal told me you were digging into edge egress from the accounting pool,” Priya said, sliding her reading glasses onto her nose. “What does the DNS telemetry tell you about that host?”

I shifted my console view from the Zeek connection log (`conn.log`) to the DNS query repository (`dns.log`), filtering on the source IP `10.100.40.12`.

The screen immediately updated, and my eyes widened at the result.

In the span of twelve hours, the accounting server had generated over forty-one thousand distinct DNS queries. Every single query targeted an identical root apex domain: `data-relay.example`.

However, no two query strings were alike. The subdomains looked like an avalanche of garbled noise:

- `a7f901b4c8e219.data-relay.example`
- `k83m90px12vz88.data-relay.example`
- `q901baef48209c.data-relay.example`
- `v7x9q2m184ca90.data-relay.example`

“It looks like an automated microservice,” I said, attempting to rationalize the flood of records. “Maybe Leah’s team deployed a distributed telemetry agent or an elastic cloud backup tool that uses randomized hostnames for regional load distribution.”

Priya let out a dry, quiet laugh.

“Look at the resolver behavior, Ethan,” Priya said, pointing to the transaction IDs and response flags. “Harrowmere runs local caching recursive resolvers for a reason. When five hundred workstations look up `salesforce.com` or `github.com`, our internal resolver answers them from its local memory cache after the first query. The requests never leave our campus. But what happens when an endpoint queries `a7f901b4c8e219.data-relay.example`, and then three hundred milliseconds later queries `k83m90px12vz88.data-relay.example`?”

I stared at the sequence of queries, the realization hitting me like cold water.

“The resolver cache is completely useless,” I whispered.

“It isn’t just useless—it is being intentionally defeated,” Priya explained. “Because every single query string is globally unique, our corporate recursive resolver has never seen it before. The resolver is forced to query the authoritative nameserver for `data-relay.example` across the public Internet for every single packet. The adversary is using `[[dns_tunneling|DNS tunneling]]` to exfiltrate data directly through the query strings, bypassing our egress inspection by turning our own internal DNS infrastructure into a recursive proxy.”

“And when they need a high-capacity command channel,” Dana added, “they combine that covert signaling with `[[domain_fronting|domain fronting]]` across the CDN. On the wire, the client initiates a TLS connection to a reputable public domain hosted on the CDN. The Server Name Indication and the initial DNS lookup look completely benign. But inside the encrypted HTTP request headers, the inner `Host` header instructs the CDN edge router to forward the request to an entirely different, attacker-controlled origin server.”

I stared at the millions of records in the data lake. My earlier sense of control had vanished. If the destination IP belonged to a trusted CDN, if the Server Name Indication was a front, and if the DNS queries used tens of thousands of unique subdomains, the entire perimeter seemed like an illusion.

“So what is our discriminator?” I asked, looking between Dana and Priya. “If the IPs are shared, the hostnames are unauthenticated, and the payloads are encrypted, what does the adversary have that they cannot fake?”

A rolling stool squeaked against the raised floor behind us. Cal Rowan slid into position next to my console, setting down his ubiquitous ceramic mug.

“They cannot fake the mathematics of the data, Ethan,” Cal said. “And they cannot easily fake the cryptographic anatomy of their client software.”

Cal reached across my desk, pulled my keyboard toward him, and split my main display into two distinct analysis windows.

“First,” Cal said, “let’s address those forty-one thousand bizarre subdomains. You thought they might be legitimate cloud load balancing. But machine-encoded data does not look like natural human language, and it does not look like standard cloud infrastructure naming conventions. In computer science, we measure the randomness and information density of a string using `[[shannon_entropy|Shannon entropy]]`.”

Cal grabbed a marker and sketched a simple mathematical equation on the small whiteboard mounted to the side of my desk:

$$H(X) = -\sum_{i=1}^{n} P(x_i) \log_2 P(x_i)$$

“Shannon entropy measures the uncertainty or information content carried by each character in a sequence,” Cal explained, tapping the whiteboard. “In standard English words and common corporate hostnames like `mail.harrowmere.com` or `files-east.internal`, letters appear in predictable combinations—vowels pair with consonants, prefixes repeat, and character redundancy is high. Standard domain names exhibit an entropy score typically between 2.0 and 3.2 bits per character.”

He pointed to the garbled query strings on my screen.

“When an adversary uses an automated tunneling utility, they compress or encode binary files, shellcode, or stolen database records into Base64, hexadecimal, or Base32 strings and stuff them into the subdomain label. Because the data is compressed or encrypted before encoding, the character distribution is virtually uniform. Every character has an equal probability of appearing. The Shannon entropy jumps to 4.5 bits per character or higher.”

Cal opened an Elasticsearch scripted metric aggregation in Kibana, targeting the `dns.question.name` field from the accounting server. He calculated the entropy score across the forty-one thousand queries and plotted the results in a histogram.

A sharp, unmistakable spike appeared on the chart: while all standard Harrowmere DNS lookups clustered safely below 3.0, the lookups for `data-relay.example` formed an isolated plateau between 4.62 and 4.88 bits per character.

“The DNS queries aren't hostnames,” I said, looking at the mathematical separation. “They’re serialized payloads.”

“Exactly,” Cal said. “Now look at the TLS connections to the CDN IPs. If they’re using domain fronting, the adversary might send a clean SNI header in the cleartext `ClientHello` claiming to reach an innocuous website. But what software is actually sending those packets?”

“The User-Agent header is inside the encrypted payload,” I noted, recalling Lesson 04. “We can’t read it.”

“We don’t care about the User-Agent header,” Cal said dismissively. “User-Agent strings are trivial to spoof. Any two-line Python or Go script can claim to be the latest version of Google Chrome. But when a piece of software initiates a TLS handshake, the operating system's cryptographic library assembles the `ClientHello` packet according to its own hardcoded implementation. It specifies a precise list of supported cipher suites, in a specific order, along with a specific set of TLS extensions, elliptic curve algorithms, and signature algorithms.”

Cal opened our Zeek `ssl.log` repository and highlighted a new field: `tls.ja4`.

“This is the `[[ja4_fingerprint|JA4 fingerprint]]`,” Cal said. “It is a modular, high-fidelity cryptographic signature of the client TLS implementation. The first four characters tell you the transport protocol, the TLS version, whether an SNI was present, and the count of ciphers and extensions. The remaining segments are deterministic hashes of the exact cipher suites and extension signatures sent on the wire.”

Cal ran a terms aggregation on the `tls.ja4` field across the entire accounting subnet.

The output was striking:

- Over 140,000 connections from employee laptops displayed standard enterprise browser fingerprints: `t13d1516h2_8daaf6152771_b5da04f6479a` (Google Chrome) and `t13d1715h2_55b3f1e94112_c8da03f8191b` (Microsoft Edge).
- But from server `10.100.40.12`, all twenty-two thousand connections to the Cloudflare CDN IP addresses shared a completely unique fingerprint:
  `t13d190800_2a27b87c7a10_e68c9e54a0f8`.

Cal pivoted that hash against our threat intelligence repository and internal software inventory.

“That hash does not belong to Chrome, Edge, Safari, or Leah’s ERP synchronization service,” Cal said, his eyes narrowing. “That exact JA4 signature matches the standard crypto/tls library compiled into custom Go binaries.”

Dana stepped back to my side, her gaze locked on the converged evidence.

“Look at the complete picture now, Ethan,” Dana said, challenging me to synthesize the hunt. “What is the difference between where you started twenty minutes ago and where you are standing right now?”

I looked at the three monitors.

“Twenty minutes ago, I was looking at three destination IP addresses,” I said. “I was ready to block a public CDN and break legitimate business operations because I couldn't separate the adversary from the cloud provider.”

“And now?” Dana asked.

“Now we have relational clustering across three independent dimensions,” I answered with complete certainty. “We have machine-encoded `[[dns_tunneling|DNS tunneling]]` proven by Shannon entropy exceeding 4.6 bits on recursive queries. We have `[[domain_fronting|domain fronting]]` disguising high-volume HTTPS sessions behind trusted CDN endpoints. And we have an unauthorized Go client identified by its unique `[[ja4_fingerprint|JA4 fingerprint]]` originating from an internal accounting server that should only be running automated ledger transactions.”

Dana offered a rare, approving nod.

“Don’t touch the perimeter firewall,” Dana instructed, turning toward the incident response channel on her phone. “Isolate host `10.100.40.12` at the switch port immediately to preserve the volatile memory on the machine. Then export the JA4 fingerprint and the entropy script into a permanent detection rule for Nia. That’s how you find the needle without burning down the haystack.”

I clicked into the network management console to issue the switch-port isolation command. The forest was as vast and crowded as it had been an hour ago, but the shadows between the trees were no longer dark.

---

### Vocabulary & Concepts

| Term | Desk Translation |
|---|---|
| [Domain Fronting](#term-domain_fronting) | An evasion technique where an adversary uses the cleartext SNI and DNS of a trusted domain hosted on a public CDN while using the encrypted HTTP Host header to route requests to an attacker-controlled origin server. |
| [DNS Tunneling](#term-dns_tunneling) | An evasion technique encoding non-DNS payloads or commands into subdomains and TXT response records, bypassing recursive resolver caching through unique query labels. |
| [Shannon Entropy](#term-shannon_entropy) | A mathematical measure of information density and randomness ($H(X)$); values above 4.5 bits per character in domain labels indicate machine-encoded data rather than natural language. |
| [JA4 Fingerprint](#term-ja4_fingerprint) | A standardized, modular cryptographic hash of a client's TLS ClientHello parameters (ciphers, extensions, algorithms) that identifies the underlying client software independent of spoofed headers. |

---

<div class="bridge-card">
  <div class="bridge-label">Next Step in Curriculum</div>
  <div class="bridge-title">Hunt 04 — Domain & TLS Clustering</div>
  <p class="bridge-desc">Enter the hunting pod with Cal Rowan and Priya Raman: calculate Shannon entropy across live DNS query labels, stack JA4 cryptographic handshakes to unmask unauthorized client runtimes, and cluster high-volume CDN egress to expose covert tunneling channels.</p>
  <a href="#/lessons/hunt-04-domain-and-tls-clustering/README" class="bridge-btn">Open Hunt 04 Workbench →</a>
</div>
