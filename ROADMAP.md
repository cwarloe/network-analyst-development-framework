# Roadmap

Seven of nine lessons are written. Here's what's actually in the way, in order.

## 1. Run a lesson with a real person

**Nothing in this repository has been used by anyone other than its author.** That is the biggest risk the project has, and it is a few hours of work to reduce.

[Lesson 01](lessons/01-what-the-analyst-is-for.md) needs no prerequisites and works with a complete beginner. The [capstone](lessons/09-capstone-encrypted-outbound-traffic/README.md) is the fuller test and works with anyone technical. Write down what happens in the [run records](lessons/09-capstone-encrypted-outbound-traffic/run-records.md) — coverage, what got noticed, where people got stuck, how long it took.

Everything else on this list is guesswork until this happens once.

## 2. Write lesson 07

The last unblocked lesson. [R004](docs/research/R004-pcap-and-telemetry-sourcing.md) cleared CIC attack days and Stratosphere/CTU-13 for republication with citation, and this is the lesson where a public corpus is the right call — realistic adversary behaviour matters more here than the lab control that made 02, 03 and 04 work.

Before shipping any third-party capture, run the pre-flight checklist in R004 **and** the [capture validation gate](lab/validate-captures.py). The gate applies to downloaded data exactly as it does to generated data: if Zeek won't parse it, it is not usable here regardless of where it came from.

## 3. Build a lab for lesson 06

**Lesson 06 — When it breaks — is the one thing the research did not unblock,** and it turned out to be the more interesting finding. No public corpus cleanly isolates documented network failures: induced latency, packet loss, MTU and fragmentation problems, policy drops. They exist in public captures only incidentally, unlabeled, mixed into everything else.

So lesson 06 needs a lab that deliberately breaks things: traffic control for latency and loss, a constrained MTU path, a firewall dropping selectively, each captured with known ground truth. The [existing capture lab](lab/README.md) is the right place to add it — it already generates real traffic and validates the output, and impairment is the missing piece rather than a new mechanism.

Worth stating plainly, because it explains a pattern in the wider field: **threat data is abundant and free, failure data has to be manufactured.** That is probably why so much network security training skips straight to the threat. This course commits to the opposite order — troubleshooting before threat, because a misread firewall change and a covert channel look alike to someone taught only to hunt covert channels — and that commitment now has a real cost attached to it.

Lesson 06 is the last thing to be built, and it should not be quietly dropped when that becomes inconvenient.

Note that lessons 02, 03 and 04 turned out not to need public data at all — generating the traffic gave known ground truth, tiny files, and no licence surface. Lesson 06 is the same argument taken further: the failures have to be caused deliberately for the lesson to have a correct answer.

## 4. Answer three design questions

These change the shape of the remaining lessons and are cheap to settle:

- **Who is the learner?** Currently assumed to be someone with no analysis experience and no tooling background. Working IT staff would compress lessons 02–04 considerably.
- **Self-guided or instructor-led?** Decides whether feedback comes from a review guide or a person.
- **How many hours?** Currently drafted at roughly 20–30. Less means cutting lessons, not thinning all of them.

## Not doing

Recorded so they don't get relitigated: no proficiency levels, no scoring, no certification, no assessment-validity claims. No second course until the first one has been run. No new architecture documents — [docs/architecture.md](docs/architecture.md) is the only one.
