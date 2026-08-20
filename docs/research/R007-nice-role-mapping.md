# R007 — NADF's capability model against the NICE Defensive Cybersecurity role

**Status:** assessed · **Date:** 2026-08-19 · **Confidence:** High on the source data, Moderate on the mapping judgment

The [Standing Qualifications](../architecture.md) have said since the beginning that *no external role standard has confirmed the capability model's completeness*. This checks it.

## Where the data came from

**Verified against NIST's official file, 2026-08-19.** The workbook is committed at [`data/NICE_Framework_Components_v2.2.0.xlsx`](data/NICE_Framework_Components_v2.2.0.xlsx) so this mapping stays reproducible. NICE Framework content is US Government work.

The mapping was originally built from a community mirror, because `nist.gov`, `niccs.cisa.gov`, `catalog.data.gov` and `nvlpubs.nist.gov` are all unreachable from the build environment. That provenance gap is now closed, and the check was worth running:

| | Official v2.2.0 | Community mirror |
|---|---|---|
| Statements for PD-WRL-001 | 206 | 206 |
| Tasks / Knowledge / Skills | 43 / 125 / 38 | 43 / 125 / 38 |
| IDs present in one but not the other | **none** | **none** |
| Text differences | **1**, cosmetic — `K0844` reads "cyber attack" officially and "cyberattack" in the mirror | |

The version question that prompted the check also resolved. v2.2.0 (April 2026) flags 70 statements as new across the framework, and **none of them belong to PD-WRL-001** — this role was untouched by that release, which is why a mirror of uncertain vintage matched it exactly.

Reproduce the extraction from the official workbook:

```python
import openpyxl, re
ws = openpyxl.load_workbook("data/NICE_Framework_Components_v2.2.0.xlsx",
                            read_only=True, data_only=True)["PD-WRL-001"]
statements = {c[0]: c[1] for c in
              ([("" if x is None else str(x).strip()) for x in row]
               for row in ws.iter_rows(values_only=True))
              if re.fullmatch(r"[TKS]\d{4}", c[0])}
```

## The role

**PD-WRL-001, Defensive Cybersecurity** — *"Responsible for analyzing data collected from various cybersecurity defense tools to mitigate risks."* This is the current name for what earlier revisions called Cyber Defense Analyst.

It carries **43 Task and 38 Skill statements**. Knowledge statements (125) are excluded from this analysis: they describe content coverage, and NADF's capability model is explicitly about demonstrable performance rather than content.

## What corresponds — and it is the core

The overlap is not incidental. Several NICE statements read as though they were written for specific NADF lessons:

| NICE | NADF |
|---|---|
| **T1348** Distinguish between benign and potentially malicious cybersecurity attacks and intrusions | [Lesson 07](../../lessons/07-when-its-suspicious.md)'s entire thesis; IR-4, OC-3 |
| **T1112** Validate network alerts / **T1387** Validate intrusion detection system alerts | [Lesson 01](../../lessons/01-what-the-analyst-is-for.md)'s worked case, where the alert title smuggles in its own conclusion |
| **T1299** Determine causes of network alerts | [Lesson 06](../../lessons/06-when-it-breaks.md) |
| **S0712** Skill in evaluating data source quality | OE-4, OE-5, [lesson 05](../../lessons/05-vantage-point-and-evidence.md) |
| **S0600** Skill in collecting relevant data from a variety of sources | OE-3, lesson 05 |
| **S0859** Skill in performing event correlation | Lesson 07's convergence finding |
| **S0869** Skill in performing metadata analysis | [Lesson 04](../../lessons/04-what-encryption-hides.md) |
| **S0156 / S0875** Packet-level and packet analysis | Lessons 02, 04, 06 |
| **S0688 / S0874 / S0872** Network data, traffic, and flow analysis | Lessons 02–07 |
| **S0866** Skill in performing log file analysis | Every capture lesson's Security Onion half |
| **T1290 / T1349 / T1428** Communicate reports, alerts, notify managers | CT-1 to CT-4, [lesson 08](../../lessons/08-judgment-and-handoff.md) |
| **T1242** Escalate incidents | JU-3, CT-4, lesson 08 |

The analytical spine of the role — validate, distinguish, determine cause, evaluate sources, correlate, communicate — is well covered. **That is the first external support this capability model has ever had.**

## The holes

Roughly 40 of the 81 statements have no NADF counterpart. They cluster, and the clusters differ in what they mean.

### Declared out of scope, but NICE puts them in the role

**Signature and detection work** — T0020, T1406, S0566, S0567, S0627 (5 statements). Developing, deploying and reading detection signatures. [Lesson 07](../../lessons/07-when-its-suspicious.md) says explicitly that it does not teach detection engineering, and the Standing Qualifications call the boundary unsettled. NICE settles it: signature work is inside this role.

**Malware handling** — T1388, T1389, T1391, S0651, S0857 (5). Isolate, remove, reconstruct, analyze. Arguably incident response, but NICE assigns it here.

**Incident resolution** — T1616, S0593, S0863 (3). NADF stops at handoff by design, and lesson 08 is explicit about role boundaries. NICE expects the analyst to resolve.

These are defensible exclusions. What they are not is *silent* exclusions any more — the Standing Qualifications should name them.

### Not declared, and not covered

**Vulnerability management** — T0292, T1119, T1603, T1615, S0543, S0544, S0614, S0839 (8 statements). Scanning, recognizing, categorizing vulnerabilities; recommending and advising on remediation. Entirely absent from NADF and not mentioned anywhere as a boundary.

**Security control and product evaluation** — T1176, T1177, T1548, T1583, S0509, S0574, S0578, S0667 (8). Whether controls and products actually reduce risk; adequacy of access controls; effectiveness of implementation and testing. Also entirely absent, also undeclared.

Sixteen statements — roughly a fifth of the role — in two clusters the project has never considered. Whether they belong in NADF is a real question. That they were never named as a decision is the finding.

### The hole that is not a scope disagreement

**Trend and longitudinal analysis** — T0164, T1539, T1540, T1541, S0892, plus continuous monitoring in T1350 and S0846 (7 statements). Cyber defense trend analysis and reporting. Organizational and system posture trend reports. Continuous monitoring of system activity.

**Every NADF lesson is a single situation at a single moment.** Nine lessons, nine episodes, each self-contained. Nothing in the course asks a learner to look at anything across time, compare this week to last, or describe a trajectory rather than a state.

This is the same finding [R005](R005-instructional-design-review.md) reached from the instructional side — that the architecture has no time dimension — arriving independently from the role side. R005 was about *when learning happens*. This is about *what the work is*. They share a root: NADF's unit of analysis is the incident, and the role's unit of analysis includes the period.

That convergence is the most useful thing in this mapping. Two unrelated methods pointing at the same structural gap is worth more than either finding alone.

### Smaller, specific

Topology reconstruction (S0490, S0755), interpreting traceroute results (S0722), establishing intrusion set procedures (T1384), maintaining currency of threat conditions (T1582), using cyber defense service provider information (S0809).

## What NADF has that NICE does not

Reading it the other direction is equally informative. These NADF statements have **no NICE counterpart at all**:

- **The entire LR domain** — LR-1 through LR-4, comparing expected against observed, revising models under evidence, transferring reasoning to changed situations, identifying one's own learning needs. NICE enumerates no statement about an analyst revising their own mental model.
- **JU-2, calibrated confidence with a stated basis**, and **JU-4, knowing when to stop investigating.**
- **IR-1, problem framing** — NICE has tasks that presuppose a framed question but none about framing it.
- **The observation / interpretation / judgment separation** that lesson 01 exists to build, and that every subsequent lesson rests on.

This is NADF's actual contribution, and it is worth being clear-eyed about what the absence means. It does not prove NICE is incomplete. It means these are **NADF's thesis rather than role coverage** — architectural judgment supported by R001–R003, not requirements any role standard has asserted.

The capability model already labels statements RS, AJ, or RS/AJ for exactly this reason. This mapping suggests the LR domain and the judgment statements sit further toward AJ than their current labels imply.

## Recommendations

1. **Name the excluded clusters in the Standing Qualifications.** Signature work, malware handling and incident resolution are deliberate exclusions; vulnerability management and control evaluation are undeclared ones. Both kinds should be visible. Cheap, and it converts a silent gap into a stated boundary.
2. **Treat the longitudinal gap as real.** It is corroborated from two directions and it is not a scope preference — the role includes work across time and the course contains none. This does not require a tenth lesson; a trend or comparison element inside an existing lesson would test whether it matters. [R008](R008-longitudinal-judgment.md) surveyed how six other fields do it and proposes concrete candidates, of which SPC-style trend tasks are the cheapest.
3. **Revisit the basis labels on LR-1 to LR-4 and JU-2/JU-4.** If no external role standard asserts them, RS/AJ may be generous.
4. ~~**Verify against NIST's own file.**~~ **Done** — the official v2.2.0 workbook matched the mirror exactly for this role and is committed alongside this record.

## What this does not establish

One role, one reviewer's judgment about what corresponds. The source data is now verified; the *mapping* is not. Mapping capability statements to task statements is interpretive — reasonable people would sort several of these differently, and no inter-rater check was done on the mapping itself, which is precisely the weakness [R006](R006-literature-scan.md) raised about NADF's own review instruments.

It also does not establish that matching NICE is the goal. A framework that covered all 81 statements and taught none of them well would be worse than this one.
