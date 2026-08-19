# Roadmap

All nine lessons are written. What matters now is whether they work.

## 1. Run a lesson with a real person

**Nothing in this repository has been used by anyone other than its author.** All nine lessons are written, which makes this the only item on the list that matters — everything below is refinement of material nobody has tried.

[`lessons/run-records.md`](lessons/run-records.md) has the operational detail: which lesson suits which reader, how to sit in the room without wrecking the data (the hard part is *not helping* — a rescued learner produces no data), the specific claims worth watching fail, and what to write down.

If you can only get one person for one hour, run [lesson 01](lessons/01-what-the-analyst-is-for.md). No dependencies, no tools, and every later lesson rests on the habit it builds.

Everything else here is guesswork until this happens once.

## 2. Rework lesson 07 against real adversary traffic

Lesson 07 is authored but uses lab-generated shapes — two beacons that are deliberately indistinguishable by shape, a DNS stream carrying entropy in the query, and a bulk upload, all converging on one domain. The reasoning it teaches is the right reasoning. The traffic is not real intrusion traffic and the lesson says so.

[R004](docs/research/R004-pcap-and-telemetry-sourcing.md) cleared CIC attack days and Stratosphere/CTU-13 for republication with citation. Running the same method against genuine captured traffic is the natural next version. Before shipping anything downloaded, run R004's pre-flight checklist **and** the [validation gate](lab/validate-captures.py) — the gate applies to third-party data exactly as it does to generated data.

## 3. Finish lesson 06 — packet loss and latency remain

Lesson 06 now covers five failure signatures: refused (`REJ`), dropped (`S0`), reset mid-transfer (`RSTR`), slow-but-correct (`SF` with a four-second application delay), and fragment loss. Those carry the discriminations that matter most — refused versus dropped are opposites producing the same complaint, the four-second delay gets reported as "the network is slow" when the network delivered in 0.2 milliseconds, and fragment loss is the only fault in the course that leaves no trace shaped like a fault.

Fragmentation was closed without privileges: EDNS0 padding inflates a legitimate DNS query past the interface MTU and the real stack does the splitting. The lesson uses it to show that a port-based filter cannot match non-initial fragments, which is why "drop non-initial fragments" is a common policy and why it silently breaks large DNS.

**What is still missing is packet loss and induced latency.** Both need `netem`, which needs `NET_ADMIN`, unavailable where the lab was built. So does a true path-MTU-discovery black hole, where an ICMP "fragmentation needed" message is filtered and the sender never learns to send smaller packets.

To close the rest, run [`lab/generate-captures.py`](lab/generate-captures.py) somewhere with `NET_ADMIN` and add `tc qdisc netem delay` and `loss` cases on a veth pair. Nothing existing needs redoing — it is additive.

## 4. Close the four cheap design gaps

[R005](docs/research/R005-instructional-design-review.md) reviewed the instructional design against the learning-science literature. Four changes are cheap, address the highest-confidence findings, and add no scoring, levels, or validity claims:

- **Same task twice.** Lesson 01's Case C at the start and again after the capstone, unaided both times, both kept. Nothing in the current design can detect that a learner improved; two artifacts to compare is the smallest thing that can.
- **Opening recall prompt** on lessons 03–09 — reconstruct something from an earlier lesson from memory, closed book, before reading on. Practice testing and distributed practice are the only two techniques Dunlosky et al. rated *high* utility, and neither appears anywhere in NADF.
- **Predict-then-check in every lesson**, as [lesson 06](lessons/06-when-it-breaks.md) already does. It is the only place in nine lessons that generates an error signal before showing the answer.
- **Paired review** in the run protocol — two reviewers, one work product, independently, then compare. Disagreement is the finding, and it is the cheapest validity evidence available.

Do these after the first run, not before. The run may show none of them is the binding constraint.

## 5. Map the capability model against an external role standard

The [Standing Qualifications](docs/architecture.md) admit that no external role standard has confirmed the capability model's completeness. The NICE Framework's Cyber Defense Analyst role publishes Task, Knowledge and Skill statements, free, and mapping 27 statements against them is about a day.

All three possible outcomes are useful: correspondence is the first external support the model has had; NADF statements with no counterpart are candidates for design judgment mistaken for role reality; NICE statements with no counterpart are coverage holes. The last is the one worth wanting.

## 6. Answer two remaining design questions

- **Who is the learner?** Currently assumed to be someone with no analysis experience and no tooling background. Working IT staff would compress lessons 02–04 considerably. [R005](docs/research/R005-instructional-design-review.md) notes this bites harder than it looks: guidance fades at fixed lesson boundaries, so the right fade point differs by audience and the design cannot detect it.
- **Self-guided or instructor-led?** This is not a delivery preference. Eight of nine lessons offer only self-review, so EF-8 — feedback, revision, transfer — is structurally unreachable without a second person. The choice decides whether a whole capability domain is in the course or not.

*How many hours* is settled: about 18. Sixteen and a half across lessons 01–08 plus 60–90 minutes for the capstone. If a delivery needs less, cut whole lessons rather than thinning all of them.

## Not doing

Recorded so they don't get relitigated: no proficiency levels, no scoring, no certification, no assessment-validity claims. No second course until the first one has been run. No new architecture documents — [docs/architecture.md](docs/architecture.md) is the only one.
