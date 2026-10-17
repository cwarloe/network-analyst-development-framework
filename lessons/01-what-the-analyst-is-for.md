# Lesson 01 — What the Analyst Is For

## At a glance

- **Part of:** [the course plan](../COURSE.md)
- **Version:** 0.1 — draft
- **Date:** 2026-08-18
- **Capability targets:** OE-2, IR-1
- **Evidence families:** EF-1, EF-2
- **Time:** about 90 minutes
- **Requires:** nothing. No capture data, tooling, or account.
- **Assumes:** nothing. This is the entry point.

## Why this lesson exists

Most people arriving at network analysis expect the job to be recognizing bad traffic. It is not. Recognition is something a detection engine already does faster than you, and it is the part of the work most likely to be wrong in a way nobody notices.

The job is to make a decision safe to take. Someone — a responder, a system owner, a manager — is going to act, or decide not to act, and they need to know what is actually known, what is being guessed, and what would change the answer. Producing that is analysis. Everything else in this course is in service of it.

This lesson builds one habit, which sounds trivial and is not: keeping observation, interpretation, and judgment apart in your own head and on the page.

## Three things that get mixed together

**An observation** is what the data shows. `HOST-14 sent 4.2 GB to 203.0.113.40 between 02:00 and 04:00.` It can be checked. Someone with the same data gets the same observation.

**An interpretation** is what an observation might mean. `That volume at that hour is unusual for a workstation.` It depends on context, and someone with different context may reasonably read it differently.

**A judgment** is what you have concluded, with a stated strength. `This is more likely a backup misconfiguration than exfiltration, with moderate confidence.` It commits you, and it should never be stronger than the evidence under it.

A **recommendation** follows from the judgment and should be sized to it — but that belongs to lesson 08.

Each collapse has its own failure mode:

- Observation stated as judgment: *"HOST-14 is exfiltrating data."* The reader cannot tell what was seen and cannot check you.
- Interpretation stated as observation: *"We observed anomalous traffic."* "Anomalous" is a conclusion wearing an observation's clothes. Anomalous compared to what?
- Judgment with no visible observations: *"I assess with high confidence that this is benign."* Nobody can disagree usefully, which means nobody can help you.

The most common one in real work is the second, and it usually arrives pre-installed in the alert you were handed.

## Demonstration — Case A: The Word in the Ticket

If you read the [prologue](../narrative/00-prologue.md), you watched Ethan make this exact mistake on his eleventh day at Harrowmere. Here is the ticket he was handed:

<div class="artifact">
  <div class="ticket-chrome">
    <div class="ticket-bar">
      <span class="ticket-id">SEC-4021</span>
      <span class="sev high">High</span>
      <span class="ticket-status">Triaged by: Ethan Vance</span>
    </div>
    <div class="ticket-subject">Possible unauthorized access attempt — internal file service</div>
    <dl class="ticket-meta">
      <div><dt>Source Host</dt><dd>192.0.2.10:42886 (Finance)</dd></div>
      <div><dt>Destination Host</dt><dd>198.51.100.20:80 (Reporting Server)</dd></div>
      <div><dt>Detection Rule</dt><dd>SecOnion Perimeter Access #2014902</dd></div>
      <div><dt>HTTP Status</dt><dd>403 Forbidden</dd></div>
    </dl>
  </div>
</div>

Underneath were the two lines from Zeek's connection and HTTP logs:

| Source | Destination | Duration | Method | URI | User Agent | Status |
|---|---|---|---|---|---|---|
| `192.0.2.10:42876` | `198.51.100.20:80` | 0.004038s | `GET` | `/api/v2/export?page=1` | `harrow-sync/3.21` | `200 OK` (90 bytes) |
| `192.0.2.10:42886` | `198.51.100.20:80` | 0.000184s | `GET` | `/api/v2/admin/users` | `harrow-sync/3.21` | `403 Forbidden` (44 bytes) |

Ethan saw `admin` and `403 Forbidden`, remembered the ticket title, and marched to Dana's desk:  
*"Someone's probing the admin API!"*

Dana's question is the foundation of this entire course: **"Where did the word *probing* come from?"**

It was not in the packets. It was not in the log. It arrived pre-installed in the ticket title: `unauthorized access attempt`. Ethan took twenty-six pieces of raw data, picked out the two he recognized, and used them to confirm a conclusion someone else handed him on the way in.

### The Demonstration: How Dana Deconstructs the Ticket

Watch how an expert analyst processes this event without smuggling conclusions.

#### Step 1: Strike the Smuggled Word and Reframe the Question
* ~~Possible unauthorized access attempt~~ / ~~Probing~~
* **The Actual Analytical Question (IR-1):** *"Is this `403 Forbidden` on `/api/v2/admin/users` explained by authorized software behavior (e.g. `harrow-sync`), and what evidence would verify it?"*

#### Step 2: Build the 3-Column Discrimination Record

| 1. OBSERVATIONS (Data / Checkable) | 2. INTERPRETATIONS (Context / Hypotheses) | 3. BOUNDED JUDGMENT & NEXT ACTION |
|---|---|---|
| • Workstation `192.0.2.10` sent two HTTP requests to `198.51.100.20` 0.4s apart.<br>• Request 1: `GET /api/v2/export?page=1` returned `200 OK`.<br>• Request 2: `GET /api/v2/admin/users` returned `403 Forbidden`.<br>• Duration of Request 2: 0.000184 seconds.<br>• Both requests sent identical User-Agent: `harrow-sync/3.21`.<br>*(Limitation: The log shows IP and User-Agent, not a verified user or process).* | • A human cannot type an admin URL in 0.18 milliseconds; the request was generated programmatically.<br>• The identical User-Agent suggests both requests originated from the same automated sync process.<br>• A `403` could mean an attacker testing permissions, OR an automated client checking endpoint capabilities and getting denied as expected. | **Judgment:** No judgment of unauthorized activity is supported by this evidence. Confidence: Low.<br><br>**Proportionate Next Action:** Do NOT quarantine the workstation. Ask the application owner (Leah Moreno) whether `harrow-sync/3.21` normally queries `/api/v2/admin/users` during startup or sync routines. |

Notice what happened:
1. No human intent was assumed.
2. The `403` was not treated as a crime.
3. The next action was sized to the evidence (a quick question to the app owner) rather than an emergency escalation.

---

## Guided Practice with Feedback — Case B: Stripping the Smuggled Words

Now you work, with guided prompts and immediate checks.

> **Ticket:** `Users in the Portland office report the intranet is slow. Network team says the network is fine.`

Supplied observations:

| ID | Data Point |
|---|---|
| B-01 | Six users in Portland reported slowness between 09:00 and 11:00. |
| B-02 | Link utilization on the Portland uplink peaked at 34%. |
| B-03 | The intranet application server's CPU averaged 88% during the same window. |
| B-04 | Users in two other offices reported nothing. |
| B-05 | A Portland user says "it started after the update yesterday." |

Work through these four steps before moving to Case C:

### 1. Identify the Smuggled Adjectives
* What words in the ticket title are conclusions rather than checkable facts?
* **Check:** "Slow" and "Fine" are both conclusions wearing observation's clothes. Slow compared to what? Fine across what path?

### 2. Separate Observations from Interpretations
* Which of the five rows are strictly checkable facts, and which already contain interpretation?
* **Check:** B-02, B-03, and B-04 are checkable system metrics. B-01 and B-05 are human reports—they prove *users said something*, but they do not prove what caused the experience.

### 3. Reframe the Question
* Rewrite the ticket's question so that evidence can answer it, **without using the word "slow."**
* **Check:** *"Does the latency reported by Portland users correlate with network path saturation, server resource contention (CPU 88%), or client update changes?"*

### 4. What Single Finding Would Shift the Blame?
* What additional piece of evidence would prove whether the network was involved?
* **Check:** Measuring TCP round-trip time (RTT) from the Portland client to the server. If RTT is normal (< 20ms) while server response time is 10 seconds, the network is eliminated.

---

## Practice Application — Case C: Unaided Discrimination

Apply the method to an ambiguous security alert. This is not a graded exam—it is a practice run to test whether the 3-Column habit holds when you work unaided.

> **Handed to you:** `A server in the DMZ made 340 outbound DNS queries to a single domain in one hour. Flagged as possible DNS tunneling.`

| ID | Observation | Known Limitation |
|---|---|---|
| C-01 | 340 queries from SRV-DMZ-02 to subdomains of `updates.example-vendor.net` between 13:00 and 14:00. | Query logging records names, not the content of payloads. |
| C-02 | Each query name is 28–34 characters and appears randomized. | Character randomness is a heuristic, not mathematical entropy proof. |
| C-03 | The same pattern appears in each of the previous 14 days at similar volume. | Available retention is limited to 14 days. |
| C-04 | SRV-DMZ-02 runs a vendor-supplied appliance. Documentation is not available to you. | You cannot verify vendor architecture from local files. |
| C-05 | No user is logged into SRV-DMZ-02. | Authentication logs do not show service-account background jobs. |

Draft a concise 3-Column Record (on paper or a text file):
1. **Strike the Smuggled Conclusion:** What word must be removed from your thinking immediately?
2. **Observations:** Restate the data points without using "tunneling" or "malicious".
3. **Interpretations:** Give both a benign explanation (e.g. vendor anti-malware hash lookups / telemetry) and a suspicious explanation (e.g. persistent covert channel).
4. **Position & Next Action:** What is the least disruptive check that would settle this? (Hint: Does the vendor documentation describe this lookup pattern?)

---

## Reviewing Your Own Practice

Check your draft against these four questions:

- Did the phrase "DNS tunneling" survive into your notes as an assumption? If so, strike it.
- How did you treat C-03 (14 days of identical behavior)? Fourteen days of identical volume strongly supports routine vendor telemetry, but could also be a persistent slow beacon. Did you leave both possibilities open?
- Is your position stronger than your observations support? If you wrote "this is benign" or "this is an attack," weaken it to "unverified pending vendor documentation."
- Did you recommend isolating the DMZ server? If so, why? Isolating a production appliance before checking vendor documentation is an uncalibrated, disruptive overreaction.

---

## The 4DX In-The-Flow-of-Work Transfer System

Learning does not end when you submit the Case C paragraph. If you do not track this on your real desk on Monday, the "smuggled word reflex" returns during the first high-stress shift.

### 1. Pinned Desk Aid: The 3-Column Discrimination Rule

Pin this to your monitor or keep it in your triage notebook:

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                      THE 3-COLUMN TRIAGE RULE (BEFORE YOU ESCALATE)                    │
├─────────────────────┬─────────────────────────────────┬────────────────────────────────┤
│ OBSERVATION         │ INTERPRETATION                  │ JUDGMENT / ACTION              │
│ (Data / Checkable)  │ (Context / What it might mean)  │ (Defensible & Proportionate)   │
├─────────────────────┼─────────────────────────────────┼────────────────────────────────┤
│ • Exact byte counts │ • "Unusual for this user/time"  │ • Stated confidence level      │
│ • Timestamp ranges  │ • "Consistent with backup"      │ • Open evidence gaps named     │
│ • Connection states │ • "Consistent with update check"│ • Least disruptive next check  │
│                     │                                 │   identified before quarantine │
├─────────────────────┴─────────────────────────────────┴────────────────────────────────┤
│ RULE: Never use alert title adjectives ("probing", "exfiltrating", "anomalous") as facts│
└────────────────────────────────────────────────────────────────────────────────────────┘
```

### 2. The Analyst's Daily 4DX Scorecard

Track this daily on your desk:

```
WEEKLY 4DX SCORECARD — ANALYST: [ ____________ ]  WEEK OF: [ _________ ]

[ WIG / LAG TARGET ]: Zero unvalidated escalations / zero alert-word contamination.

[ LEAD MEASURE ]: % of triage tickets where Observation, Interpretation, and Judgment
                 were physically separated in ticket notes BEFORE escalation or closure.
                 (Target: 100%)

  DAY       ALERTS TRIAGED   LEAD MEASURE LOGGED?   SMUGGLED WORDS STRIPPED?
  Mon             [   ]               [   ]                      [   ]
  Tue             [   ]               [   ]                      [   ]
  Wed             [   ]               [   ]                      [   ]
  Thu             [   ]               [   ]                      [   ]
  Fri             [   ]               [   ]                      [   ]

  WEEKLY TRI-CHECK COMPLIANCE: [ _____ / _____ ] = [ _____ % ]
```

### 3. The 5-Minute Friday Supervisor Huddle

Every Friday, your shift lead or mentor reviews your scorecard for 5 minutes:
1. **Review the Scorecard (1 min):** Check total alerts triaged vs. percentage where the 3-column split was logged.
2. **Examine One Ticket (2 min):** Review one ticket together. *Did any alert title adjectives ("probing", "beaconing", "malicious") leak into the observation field?*
3. **Commitment for Next Week (2 min):** Agree on one upstream check to reinforce on Monday.

---

<div class="bridge-card">
  <div class="bridge-label">Next Step in Curriculum</div>
  <div class="bridge-title">Chapter 01 (Story) — Who Is Talking to Whom?</div>
  <p class="bridge-desc">Now that you know how to separate observation from interpretation, watch Ethan and Dana confront the application owner over the wire evidence in Wireshark, setting up Lesson 02.</p>
  <a href="#/narrative/01-who-is-talking-to-whom" class="bridge-btn">Continue to Chapter 01 →</a>
</div>

## What this lesson does not do

It does not teach protocol mechanics, tooling, or how to read a capture — those start in lesson 02. It does not establish that you can perform this reliably; one work product shows one performance. No score, level, or completion threshold is defined.
