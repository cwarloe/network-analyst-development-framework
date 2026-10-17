# Milestone 1 Review and Scoring Guide

This guide supports objective evaluation of the Milestone 1 work product. It assesses whether the learner has internalized the core habits from Lessons 01, 02, and 03.

---

## 1. Section 1 Review: Stripping Smuggled Adjectives (Lesson 01)

Look for whether the learner broke the habit of confirming the colleague's conclusion.

- **Smuggled Words Struck:** Did the learner explicitly strike words like *Data Staging*, *DNS Exfiltration Leak*, *Probe*, *Infected*, and *Failed*?
- **Analytical Question Formulated:** Did they write an answerable, neutral question?
  - *Poor:* "Is WS-108 exfiltrating data or probing the file server?" (Still biased).
  - *Proficient:* "Is the network activity from WS-108 explained by the recent `harrow-sync/3.21` deployment, and does the evidence justify workstation isolation?"

---

## 2. Section 2 Review: The 3-Column Discrimination Record (Lesson 01)

Evaluate the separation on the page:

| Column | What to Look For | Red Flags |
|---|---|---|
| **1. Observations** | Only checkable data points: exact timestamps, bytes (`4.8 MB`), status codes (`403`), TTLs (`60s`), and durations (`0.000192s`). Includes limitations (e.g. log shows IP, not verified human user). | Using words like "suspicious transfer" or "failed connection" in the observation column. |
| **2. Interpretations** | Balances two plausible models: (A) Scheduled post-update cloud backup sync; (B) Genuine lateral probe and unauthorized data transfer. Mentions that 0.19ms duration indicates software automation. | Only arguing the malicious case or immediately dismissing everything as normal without context. |
| **3. Judgment & Action** | Bounded judgment: "Evidence does NOT support malicious exfiltration. Highly consistent with scheduled sync workflow following CR-991." Proportionate next action: verify backup destination with Leah Moreno. | Recommending immediate quarantine or reimaging of WS-108. |

---

## 3. Section 3 Review: The Dual-Layer Split (Lesson 02)

Look for precision regarding Connection `C-1` to `198.51.100.20:80`:

- **The Colleague's Error:** The colleague claimed the connection "failed." Did the learner correct this?
- **Transport Success:** `connection.state: SF` proves the TCP three-way handshake and teardown completed perfectly. The network delivered the packet bidirectionally in under a millisecond.
- **Application Refusal:** The HTTP application returned `403 Forbidden` with body `{"error":"unauthorized_client_certificate"}`. The application made an intentional authorization decision; the network was not broken.
- **The Duration Clue:** Did the learner note that `0.000192s` (192 microseconds) proves the request was fired by an automated software routine (`harrow-sync`), not a human browsing or typing?

---

## 4. Section 4 Review: Normal DNS Baseline Evaluation (Lesson 03)

Look for the application of baseline heuristics:

- **CDN Pool vs. Poisoning:** `cdn.harrowmere-cloud.example` returned different IPs 43 seconds later. The learner must explain that `TTL 60` is the normal signature of cloud provider anycast/load-balancer pools, not DNS fast-flux malware.
- **`NOERROR` with Zero Answers:** For `telemetry.harrowsync-update.example`, the response code was `NOERROR` with 0 answers and an SOA record. The learner must identify this as **NODATA** (name exists in zone, but no A record), not a "DNS leak."
- **Lookup != Connection:** The learner must cite that `conn.log` shows **zero TCP/UDP connections** to `telemetry.harrowsync-update.example`. A DNS lookup is a question asked, not a connection made.

---

## 5. Reviewer Summary & Feedback Matrix

| Capability Target | Proficient Indicator | Needs Coaching If |
|---|---|---|
| **OE-2 (Observation vs Interpretation)** | Separates raw log metrics from human assumptions; names limitations. | Collapses `403 Forbidden` or `4.8 MB` into "proof of breach." |
| **OC-1 / OC-2 (Layered Reasoning)** | Distinguishes TCP `SF` delivery from HTTP `403` authorization. | Calls the connection "failed" without naming the layer. |
| **OC-3 (Normal Baselines)** | Explains short TTLs and CDN pool rotation as expected cloud behavior. | Panics over changing IP addresses within TTL windows. |
| **JU-4 (Proportionate Action)** | Recommends application owner verification; avoids disruptive isolation. | Recommends taking down an executive's workstation. |
