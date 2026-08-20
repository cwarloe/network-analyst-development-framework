# Roadmap

All nine lessons are written. What matters now is whether they work.

## 1. Run a lesson with a real person

**Nothing in this repository has been used by anyone other than its author.** All nine lessons are written, which makes this the only item on the list that matters — everything below is refinement of material nobody has tried.

[`lessons/run-records.md`](lessons/run-records.md) has the operational detail: which lesson suits which reader, how to sit in the room without wrecking the data (the hard part is *not helping* — a rescued learner produces no data), the specific claims worth watching fail, and what to write down.

If you can only get one person for one hour, run [lesson 01](lessons/01-what-the-analyst-is-for.md). No dependencies, no tools, and every later lesson rests on the habit it builds.

Everything else here is guesswork until this happens once.

## 2. Rework lesson 07 against real adversary traffic — needs your connection, not mine

Lesson 07 uses lab-generated shapes and says so. Reworking it against genuine captured intrusion traffic is the natural next version.

**Retested 2026-08-19, by HTTP and by git including third-party mirrors.** CIC, Stratosphere, SecRepo and Netresec are all unreachable from the build environment. Stratosphere's GitHub mirrors carry code and CSV feature extracts, not captures. Wireshark's repository is reachable and holds 218 capture files, but they are protocol dissector tests rather than adversary traffic, and GPL-2.0 into a CC BY-NC-SA work raises the same copyleft problem [R004](docs/research/R004-pcap-and-telemetry-sourcing.md) flags for CC BY-SA.

The blocker is not download. **[R004](docs/research/R004-pcap-and-telemetry-sourcing.md)'s pre-flight requires re-reading the source's current terms page, and for every cleared source of adversary traffic that page is unreachable here.** Shipping regardless would mean asserting a licence position from a page nobody can open, which is the failure that record exists to prevent.

From a normal connection this is minutes of work: complete R004's pre-flight, download, trim to a small excerpt, run it through [the validation gate](lab/validate-captures.py), and cite the dataset and its paper.

## 3. Finish lesson 06 — packet loss and latency remain

Lesson 06 now covers five failure signatures: refused (`REJ`), dropped (`S0`), reset mid-transfer (`RSTR`), slow-but-correct (`SF` with a four-second application delay), and fragment loss. Those carry the discriminations that matter most — refused versus dropped are opposites producing the same complaint, the four-second delay gets reported as "the network is slow" when the network delivered in 0.2 milliseconds, and fragment loss is the only fault in the course that leaves no trace shaped like a fault.

Fragmentation was closed without privileges: EDNS0 padding inflates a legitimate DNS query past the interface MTU and the real stack does the splitting. The lesson uses it to show that a port-based filter cannot match non-initial fragments, which is why "drop non-initial fragments" is a common policy and why it silently breaks large DNS.

**What is still missing is packet loss and induced latency.** Both need `netem`, which needs `NET_ADMIN`, unavailable where the lab was built. So does a true path-MTU-discovery black hole, where an ICMP "fragmentation needed" message is filtered and the sender never learns to send smaller packets.

To close the rest, run [`lab/generate-captures.py`](lab/generate-captures.py) somewhere with `NET_ADMIN` and add `tc qdisc netem delay` and `loss` cases on a veth pair. Nothing existing needs redoing — it is additive.

## 4. Close the cheap design gaps — in R008's order

[R005](docs/research/R005-instructional-design-review.md) reviewed the design; [R006](docs/research/R006-literature-scan.md) scanned the literature it named and reordered the recommendations; [R008](docs/research/R008-longitudinal-judgment.md) asked how other fields develop judgment across time and **merged the two lists into one**. The current order:

1. ~~**Make the existing continuity explicit.**~~ **Done.** It was stronger than R008 realised: lesson 02 and lesson 04's stream 0 are the same client (`192.0.2.10`), the same server (`198.51.100.20`), the same service and the same `GET /api/v2/export?page=1` — differing only in port 80 versus 443. Lesson 04 now says so, and contrasts the 90-byte JSON summary describing 1,284 rows against the two byte counts that replace it. Nothing about the conversation changed; the vantage point on it did.
2. **Cross-lesson judgment log with delayed verification.** Record the decision, the confidence and the expected horizon; reveal ground truth later; let a personal hit-and-miss record accumulate. This is R006's predict-then-check and same-task-twice unified into one mechanism, running across the course rather than inside one lesson — and it arrived from meteorology, not from learning science. About five minutes per lesson.
3. **Convert one or two incidents to multi-episode**, with an explicit revisit-your-own-judgment step. R006 wanted a second transfer exposure before the capstone; R008 wants continuity. Same move. Costs breadth.
4. **SPC-style trend tasks** — a short time series, one or two trend rules, an investigate-or-monitor decision, immediate feedback. The only item that adds a genuinely new capability rather than restructuring what exists, and also the one whose training-effect evidence is weakest. Five to ten minutes in three or four lessons.
5. **Paired review, with the bar set before the trial.** Ask whether two reviewers *notice the same things* — the same weak claim, the same missing alternative — not whether they reach the same verdict. The review guide is deliberately not a rubric, so low verdict agreement would be expected and would prove nothing. [R009](docs/research/R009-reviewer-agreement.md) sets the design and the thresholds.
6. **Closed-book recall prompts** — demoted twice and still demoted. Least reliable for procedural material, and NADF lacks the feedback that makes retrieval work.
7. *Change-detection micro-drills* — recommended by R008's brief and **declined** there. The transfer from perceptual discrimination to analytic judgment is unverified, and a decontextualized spot-the-difference drill is closer to what the capability model excludes than to what it measures.

Item 1 is nearly free and strengthens a lesson that already exists. Do it whenever. The rest wait on the first run.

Also watch, rather than change: **lessons 02–04 may be overloading novices with self-explanation.** If learners abandon the self-review sections there but complete them in 01, 08 and 09, cognitive load is the likely cause.

Do these after the first run. The run may show none of them is the binding constraint.

## 5. Act on the role-standard mapping

Done — [R007](docs/research/R007-nice-role-mapping.md) mapped the capability model against the NICE Defensive Cybersecurity role. The analytical spine corresponds, which is the first external support this model has had. What remains is acting on the gaps:

- **Name the excluded clusters in the Standing Qualifications.** Signature work, malware handling and incident resolution are deliberate exclusions. Vulnerability management and security-control evaluation — about a fifth of the role — are undeclared ones. Partly done; the boundary decisions themselves are still open.
- **Decide about longitudinal work.** The role includes trend analysis, posture reporting and continuous monitoring. Every lesson here is a single moment. [R005](docs/research/R005-instructional-design-review.md) reached the same gap from the instructional side, which is the strongest signal in either record. A trend or comparison element inside an existing lesson would test whether it matters, without a tenth lesson.
- **Revisit the basis labels** on LR-1 to LR-4 and JU-2/JU-4. No external role standard asserts them, so RS/AJ may be generous.
- ~~**Verify against NIST's own file.**~~ **Done.** The official v2.2.0 workbook matched the community mirror exactly for this role — 206 statements, identical IDs, one cosmetic wording difference. None of PD-WRL-001's statements changed in v2.2.0, which is why a mirror of uncertain vintage matched. The workbook is committed at [`docs/research/data/`](docs/research/data/).

## 6. Answer two remaining design questions

- **Who is the learner?** Currently assumed to be someone with no analysis experience and no tooling background. Working IT staff would compress lessons 02–04 considerably. [R005](docs/research/R005-instructional-design-review.md) notes this bites harder than it looks: guidance fades at fixed lesson boundaries, so the right fade point differs by audience and the design cannot detect it.
- **Self-guided or instructor-led?** This is not a delivery preference. Eight of nine lessons offer only self-review, so EF-8 — feedback, revision, transfer — is structurally unreachable without a second person. The choice decides whether a whole capability domain is in the course or not.

*How many hours* is settled: about 18. Seventeen across lessons 01–08 plus 60–90 minutes for the capstone. If a delivery needs less, cut whole lessons rather than thinning all of them.

## Not doing

Recorded so they don't get relitigated: no proficiency levels, no scoring, no certification, no assessment-validity claims. No second course until the first one has been run. No new architecture documents — [docs/architecture.md](docs/architecture.md) is the only one.
