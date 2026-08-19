# R004 — Which packet captures NADF may publish

**Status:** assessed · **Date:** 2026-08-19 · **Confidence:** varies by source, stated per row

## The question

Which public capture and telemetry corpora may NADF lawfully embed in, or distribute alongside, training material published under CC BY-NC-SA 4.0 — and what must instead be generated in a lab?

Five lessons were blocked on this. It is answered enough to start writing four of them.

## Standing caution

**Verify the source's current terms page immediately before incorporating any file.** Terms change, and this record will go stale. Nothing below is legal advice.

Two license mechanics drive most of the outcomes:

- **CC BY-SA material is incompatible with this repository.** Adding the NonCommercial term violates BY-SA's "no additional restrictions" rule. There is no workaround.
- **Editing a capture is almost certainly an adaptation, not a collection.** Embedding a file unmodified is more likely a collection, with lighter obligations. Trimming, filtering, anonymizing, re-timing, or splicing triggers derivative rules — and NADF will do all of those. Treat every capture NADF touches as an adaptation and require upstream terms that permit modification.

## Cleared for use

| Source | Use it for | Confidence | Obligation |
|---|---|---|---|
| **CIC datasets** (CIC-IDS2017 and family) | Primary source. Normal-behavior baselines, labeled attacks, mixed traffic | **High** | Citation to the dataset **and** its research paper, in the lesson |
| **SecRepo** (their own hosted data only) | Supplementary samples | **High** | Attribution (CC BY 4.0) |
| **Stratosphere IPS / CTU-13** | Suspicious activity — botnet C2, beaconing | **Moderate** | Citation in the maintainers' specified format; confirm per-dataset that the PCAPs are public |
| **Wireshark wiki samples, tool-distributed PCAPs** | Single-protocol baselines only, file by file | **Low–Moderate** | Only where a permissive license is actually present. **Default to exclude.** |

Operative grant, CIC FAQ: *"With any of our datasets, you may redistribute, republish, and mirror our datasets in any form. However, any use or redistribution of the data must include a citation to the dataset and the research paper listed."*

That sentence is what unblocks this project. Redistribution, republication, and modification are all permitted, with no ShareAlike or NonCommercial conflict.

## Excluded

| Source | Why |
|---|---|
| **MAWI / WIDE** | *"You may use WIDE traffic data for only research purposes."* Research-only defeats public redistribution |
| **UNSW-NB15** | *"Free use … for academic research purposes … Use for commercial purposes is strictly prohibited."* Academic-only |
| **CAIDA** | The Public AUA grants a limited, non-transferable license with an access process and publication reporting. Not an open redistribution license |
| **Malware-Traffic-Analysis.net** | No license grant of any kind. Unknown rights disqualify it, despite the material being excellent |
| **Anything CC BY-SA** | ShareAlike incompatibility, as above |
| Anything requiring registration, a signed agreement, or marked research/academic use only | Same reason in each case |

Netresec's index is a discovery tool, not a source of rights — follow through to whatever it links.

## What this changes for the course

Four of the five blocked lessons are unblocked. One got harder, and that is the more useful finding.

| Lesson | Status after this research | Source |
|---|---|---|
| 02 — Reading a conversation | **Unblocked** | CIC benign traffic |
| 03 — Names and expectations | **Unblocked** | CIC benign traffic (DNS) |
| 04 — What encryption hides | **Unblocked** | CIC benign traffic (TLS) |
| 06 — When it breaks | **Still blocked — lab required** | No public source |
| 07 — When it's suspicious | **Unblocked** | CIC attack days, Stratosphere/CTU-13 |

**Lesson 06 is the finding.** Public corpora do not cleanly isolate documented network failures — induced latency, packet loss, MTU and fragmentation problems, policy drops. They are captured incidentally, unlabeled, mixed into other traffic. Producing them means building a lab.

This is worth noticing because lesson 06 is not a minor lesson. The course's design commitment is that troubleshooting precedes threat: *a misread firewall change and a covert channel look alike to someone who has only been taught to look for covert channels.* The lesson that makes lesson 07 honest is the one with no dataset available. Threat data is abundant and free; failure data has to be manufactured. That asymmetry is probably why so much network security training starts at the threat.

## Lab generation

Required for lesson 06, and for any modern suspicious pattern not cleanly present in the cleared sources — precise beaconing intervals, DNS tunneling variants, staging to cloud storage.

Conditions: isolated virtual network, synthetic or consented endpoints only, no real user traffic and no credentials, full capture with known ground truth, post-capture anonymization (Crypto-PAn or equivalent, plus payload scrubbing), the generation method documented, and the generation scripts retained. Release only the scrubbed, documented derivative under CC BY-NC-SA 4.0.

Ground truth is the real prize here, not just the license. A lab-generated failure has a known cause, which is exactly what a troubleshooting lesson needs and what an incidental public capture cannot supply.

## Before shipping any capture file

1. Re-read the source's current terms page.
2. Confirm the grant appears on **the specific dataset's page**, not only in a site-wide FAQ. The research flagged this as unverified for CIC's individual dataset pages.
3. Record the citation in the lesson that uses the file.
4. Inspect for residual identifiers before publishing, even where the source claims anonymization.
5. Trim to the smallest excerpt that teaches the point — good practice for repository size, and it narrows the redistribution surface.

Full datasets stay upstream. NADF ships small trimmed excerpts with citations, not mirrors.

## Open questions

- Per-file terms for individual Wireshark wiki samples and tool-distributed PCAPs. No central license statement exists. *Resolution:* inspect each file's origin; exclude when unclear.
- Whether the CIC grant appears verbatim on every individual dataset page and covers current releases equally. *Resolution:* check the specific download page before use.
- Scope of "use" versus "redistribute modified derivatives" for Stratosphere beyond the FAQ. *Resolution:* prefer CIC where either would serve; contact maintainers if Stratosphere becomes load-bearing.
- Whether any CAIDA dataset carries a more permissive grant than the AUA. *Resolution:* per-dataset catalog review. Low priority — CIC covers the same ground with clearer rights.
- Residual PII in older real-world malware captures despite claimed anonymization. *Resolution:* independent review before any use. Applies to Stratosphere.
- Collection versus adaptation characterization for heavily edited third-party captures. *Resolution:* NADF treats all edited captures as adaptations, which is the conservative reading and removes the question.

## Provenance

External LLM research brief commissioned by the maintainer, 2026-08-19, against a specification requiring cited URLs, quoted operative license sentences, and explicit Unknown ratings rather than inferred terms. License quotations are reproduced above as supplied. **Not independently re-verified against source terms pages** — step 1 of the pre-flight checklist exists for that reason, and confidence ratings here describe the brief's evidence, not confirmation by this project.
