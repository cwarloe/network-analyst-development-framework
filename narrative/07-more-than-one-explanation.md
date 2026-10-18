# More Than One Explanation

## At a glance

- **Part of:** [the narrative track](README.md) · read before [Lesson 07](../lessons/07-when-its-suspicious.md)
- **Version:** 0.1 — draft
- **Date:** 2026-08-22
- **Time:** about 12 minutes
- **Requires:** nothing. No tooling, capture, or account.
- **Creates the question:** When recurring outbound network traffic exhibits periodic timing, how do competing explanations prevent premature indicator-first labeling?

---

By the middle of my fourth month at Harrowmere Equipment Group, I had traded my early overconfidence for a new and equally paralyzing habit: I was terrified of committing to a conclusion too soon.

In my first weeks, I had jumped at every anomaly, treating benign TCP retransmissions as outages and protocol upgrades as covert channels. Dana Shah and the senior engineers had systematically dismantled those impulses. They had taught me to inspect physical vantage points, respect caching lifecycles, and draw rigid boundaries around what encrypted sessions could prove.

The discipline had made me careful. But it had also made me hesitant. When presented with ambiguous evidence, I had developed a tendency to list four or five competing hypotheses and leave them all politely floating on the page, unwilling to eliminate any of them because technically, in some theoretical universe, each one remained possible.

Dana noticed.

On Wednesday afternoon, she dropped a printout of an internal security review onto my blotter. The ticket concerned an engineering workstation, `192.0.2.10`. An analyst on the morning shift had flagged the machine during a weekly sweep and added an urgent note in the ticketing queue:

> *“WS-10 exhibits recurring periodic outbound connections on an exact 4-second timer to external IP `198.51.100.60`. Jitter is under 1.5%. Pattern is characteristic of malware command-and-control beaconing. Recommend immediate host isolation.”*

“Look at the capture file—`07-suspicious.pcap`—and read the connection logs,” Dana said. “Tell me whether you agree with the isolation recommendation.”

I loaded the capture into our terminal and ran a summary over the hour of traffic:

```
count  destination.ip   destination.port  network.protocol  client.bytes  server.bytes
40     198.51.100.80    53                dns               96            125
11     198.51.100.60    80                http              139           116
9      198.51.100.70    80                http              134           116
1      198.51.100.90    80                http              61618         0
```

I checked the two periodic HTTP destinations first.

Destination `198.51.100.60` had 11 connections with a mean interval of 4.02 seconds and a standard deviation of 0.048 seconds—barely 1.2% variation. Every request was an HTTP GET for `/api/v1/tasks?id=8842` carrying a browser User-Agent string.

Destination `198.51.100.70` had 9 connections with a mean interval of 4.96 seconds and a standard deviation of 0.234 seconds—about 4.7% variation. Every request was an HTTP GET for `/hb`.

Then I looked at the DNS traffic to `198.51.100.80`. Forty queries, all requesting TXT records, each query string 78 characters long and starting with a unique 48-character high-entropy label.

Finally, there was a single connection to `198.51.100.90` transferring 61 kilobytes of client data outbound.

I took out my notepad and wrote down four possible explanations:
1. *Approved Telemetry Agent:* The host is running an authorized third-party application or enterprise monitoring tool performing periodic health checks and crash dump uploads.
2. *Configuration Error / Rogue Script:* A developer left a local automated testing harness or looping curl script running in the background.
3. *Unwanted / Adware Software:* A browser extension or unauthorized freeware utility is periodically checking for ad configurations or metrics.
4. *Active Malicious Intrusion:* A malware implant is maintaining an active [[c2_beaconing|C2 beacon]] check-in, using [[dns_tunneling|DNS tunneling]] for covert signaling and staging a data exfiltration channel.

I stared at my list. All four explanations could account for periodic HTTP requests. All four were technically compatible with the presence of outbound connections. I couldn't disprove any of them from the terminal.

Owen Kline walked past our row, carrying a cup of tea, and paused behind my monitor.

“What are you working on?” Owen asked.

“A beaconing escalation on `192.0.2.10`,” I said. “The ticket wants host isolation. I have four plausible explanations, but the traffic shape fits all of them.”

Owen leaned down, looking at my list of four possibilities. He made a low sound in his throat.

“If an explanation fits everything, it explains nothing,” Owen said. “Having four possibilities isn’t analysis, Ethan. It’s an inventory. Which two actually compete to explain the evidence in front of you?”

Dana turned her chair toward us.

“Owen is right,” Dana said. “Listing alternatives forever is just another way to avoid making an analytical commitment. An alternative is only useful if it generates an observable prediction that differs from the other explanations.”

She tapped my notepad with a pencil.

“Look at your four explanations,” Dana challenged. “Take Explanation 1—the approved corporate agent—and Explanation 4—the malicious implant. If Explanation 1 is true, what specific observable facts should exist on the network that would *not* exist if Explanation 4 is true?”

I paused, forcing myself to visualize the physical mechanisms behind the traffic.

“If it’s an approved corporate agent,” I said slowly, “the traffic should be present on more than one machine. An enterprise agent deployed by IT doesn’t sit on a single isolated workstation; it appears across the entire peer group or department.”

“Good,” Dana said. “What else?”

“If it’s an approved corporate agent, the destination domain should align with an established infrastructure vendor or internal service name. And the DNS queries shouldn't need to defeat local caching unless there’s a specific functional reason to bypass it.”

“Now reverse it,” Dana said. “If Explanation 4 is true—if this is an adversary implant—what does that model predict?”

“It predicts high domain isolation,” I answered. “The external destination should not appear across peer workstations. It predicts that the beaconing interval, the DNS queries, and the outbound upload are coordinated parts of the same operational footprint rather than unrelated background noise.”

Owen set his tea down on the edge of the filing cabinet.

“So look at the fields you already have on your screen,” Owen said. “Stop staring at the jitter calculations. Look at the names.”

I brought up the HTTP logs and the DNS query logs side by side.

For weeks, I had been trained to evaluate IP addresses and connection timing. But when I looked at the actual hostnames associated with the three external destinations, the pattern snapped into focus:

- Destination `198.51.100.60` (the 4-second HTTP beacon): `http.virtual_host` was `cdn-metrics.example`.
- Destination `198.51.100.80` (the 40 high-rate TXT queries): `dns.query.name` was formatted as `<unique-string>.sync.cdn-metrics.example`.
- Destination `198.51.100.90` (the 61KB outbound data transfer): `http.virtual_host` was `cdn-metrics.example`.

Three completely different IP addresses. Three completely different network protocols—HTTP polling, DNS TXT queries, and a bulk TCP data transfer.

All three converged on the exact same [[apex_domain|apex domain]]: `cdn-metrics.example`.

I looked at the fourth destination in the capture: `198.51.100.70`, the other periodic HTTP connection. Its `http.virtual_host` was `updates.harrowmere-group.example`. It had no high-entropy DNS queries. It had no bulk data uploads. It existed entirely within Harrowmere’s registered domain infrastructure.

“The two beacons aren't the same,” I said, the realization hitting me. “The colleague who flagged this ticket saw 1.2% jitter on `198.51.100.60` and jumped straight to C2. But the real discriminator isn't the jitter. It’s that `198.51.100.60`, the DNS queries, and the data transfer all share the same apex domain.”

“That is [[relational_convergence|relational convergence]],” Dana said approvingly. “Morphology—the visual shape of a single connection—is easy to mimic and easy to mistake. An adversary can add jitter to a beacon with three lines of code. What is far harder to disguise is the relational linkage between separate infrastructure components serving the same operation.”

Dana leaned closer to the screen.

“So,” she said, testing me, “now that you see convergence on `cdn-metrics.example`, does that prove it is malware? After all, a content delivery network or a third-party analytics SDK might use one domain for metrics polling, another for DNS routing, and a third for crash telemetry.”

I looked at the evidence. Dana was giving me an easy way out, offering a plausible benign explanation to see if I would retreat back into indecision.

“It doesn't prove malice,” I said carefully. “A legitimate analytics library could exhibit this architecture. But here is why I rank the malicious explanation higher than the approved software explanation: the DNS channel is querying 78-character TXT records with 48 characters of high-entropy encoding, forty times an hour, with zero caching. That is not standard web browsing. That is an active bidirectional data channel.”

I turned to Owen. “What would settle it immediately?”

“A peer check across the SIEM,” Owen replied. “Query the logs for any other workstation resolving `cdn-metrics.example` over the last thirty days. If two hundred laptops talk to it, Leah’s team probably licensed a new performance monitoring widget. If only `192.0.2.10` talks to it, the benign explanation takes a direct hit.”

I opened our SIEM console and ran the query across the enterprise log repository for `cdn-metrics.example`.

The search returned exactly one host: `192.0.2.10`.

Zero other systems in the entire company had ever resolved that domain.

Dana leaned back in her chair and crossed her arms.

“Now,” Dana said, “look back at the ticket. The morning analyst recommended immediate host isolation. Do you isolate the workstation?”

I considered the reversibility of the action and the evidence we had gathered.

“No,” I answered firmly. “Not immediately. Isolating an engineering workstation disrupts ongoing work and alerts anyone with an active implant that their activity has been detected. The traffic is sending small periodic queries, not dumping customer databases. The appropriate next step is a calibrated triage: pull the process telemetry from the endpoint to identify the parent executable opening sockets to `cdn-metrics.example`, verify whether the binary is signed, and check whether other unmanaged devices share the traffic. If the endpoint telemetry reveals an unapproved binary running out of a user temp directory, then we isolate with full justification.”

Owen smiled, picked up his tea, and nodded toward Dana.

“He didn't say ‘it depends,’” Owen noted. “He ranked them, named the discriminator, and stated the breaker.”

Dana turned back to her desk with a nod of quiet satisfaction.

“Document the convergence in the ticket,” Dana said. “When you present evidence to an incident commander, don’t give them four equally weightless theories. Give them competing explanations, show them which evidence separates the models, and tell them exactly which observation would prove you wrong.”

I opened the ticketing system and began drafting my response. 

The shapes on the wire were no longer a confusing tangle of possibilities. They were clues in a deliberate competition, waiting for an analyst who knew how to ask the evidence to decide.

---

### Vocabulary & Concepts

| Term | Desk Translation |
|---|---|
| [C2 Beacon](#term-c2_beaconing) | A recurring, scheduled outbound network connection initiated by an implant or background process to check in with an external command-and-control server for new instructions. |
| [DNS Tunneling](#term-dns_tunneling) | An evasion and communications technique that encodes non-DNS application data or commands into the subdomains and payload fields of DNS queries and responses. |
| [Apex Domain](#term-apex_domain) | The root or base domain name (such as `example.com`) directly under the top-level domain, serving as the common administrative entity across multiple distinct subdomains and IP addresses. |
| [Relational Convergence](#term-relational_convergence) | An analytical finding where multiple superficially independent network behaviors (such as an HTTP poll, a DNS burst, and a file upload) converge upon the same external entity or infrastructure, providing far stronger evidence than any single behavior observed in isolation. |

<div class="bridge-card">
  <div class="bridge-label">Next Step in Curriculum</div>
  <div class="bridge-title">Lesson 07 — When It's Suspicious</div>
  <p class="bridge-desc">Dive into <code>07-suspicious.pcap</code> to evaluate beacon interval regularity, analyze DNS query entropy, and apply the SOC Triage Tri-Check to separate benign analytics software from true relational convergence.</p>
  <a href="#/lessons/07-when-its-suspicious" class="bridge-btn">Open Lesson 07 →</a>
</div>
