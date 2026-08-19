# Roadmap

Eight of nine lessons are written. Here's what's actually in the way, in order.

## 1. Run a lesson with a real person

**Nothing in this repository has been used by anyone other than its author.** That is the biggest risk the project has, and it is a few hours of work to reduce.

[Lesson 01](lessons/01-what-the-analyst-is-for.md) needs no prerequisites and works with a complete beginner. The [capstone](lessons/09-capstone-encrypted-outbound-traffic/README.md) is the fuller test and works with anyone technical. Write down what happens in the [run records](lessons/09-capstone-encrypted-outbound-traffic/run-records.md) — coverage, what got noticed, where people got stuck, how long it took.

Everything else on this list is guesswork until this happens once.

## 2. Write lesson 07

The last unblocked lesson. [R004](docs/research/R004-pcap-and-telemetry-sourcing.md) cleared CIC attack days and Stratosphere/CTU-13 for republication with citation, and this is the lesson where a public corpus is the right call — realistic adversary behaviour matters more here than the lab control that made 02, 03 and 04 work.

Before shipping any third-party capture, run the pre-flight checklist in R004 **and** the [capture validation gate](lab/validate-captures.py). The gate applies to downloaded data exactly as it does to generated data: if Zeek won't parse it, it is not usable here regardless of where it came from.

## 3. Finish lesson 06 — it needs traffic impairment

Lesson 06 is written and covers four failure signatures: refused (`REJ`), dropped (`S0`), reset mid-transfer (`RSTR`), and slow-but-correct (`SF` with a four-second application delay). Those carry the discriminations that matter most — particularly refused versus dropped, which are opposites that produce the same user complaint, and the four-second delay that gets reported as "the network is slow" when the network delivered in 0.2 milliseconds.

**What it does not cover is packet loss, latency, and MTU or fragmentation problems.** Generating those requires `netem`, which needs `NET_ADMIN` and was not available in the environment where the lab was built. Everything else in lesson 06 was produced without privileges — a full accept queue drops SYNs exactly as a firewall does, and `SO_LINGER 0` produces a genuine RST.

To close it, run [`lab/generate-captures.py`](lab/generate-captures.py) somewhere with `NET_ADMIN` and add impairment cases: `tc qdisc netem delay` and `loss` on a veth pair, and a constrained-MTU path for fragmentation and PMTUD black holes. MTU black holes in particular are a classic failure class the lesson names and does not teach.

Nothing about the existing captures needs redoing — this is additive.

## 4. Answer three design questions

These change the shape of the remaining lessons and are cheap to settle:

- **Who is the learner?** Currently assumed to be someone with no analysis experience and no tooling background. Working IT staff would compress lessons 02–04 considerably.
- **Self-guided or instructor-led?** Decides whether feedback comes from a review guide or a person.
- **How many hours?** Currently drafted at roughly 20–30. Less means cutting lessons, not thinning all of them.

## Not doing

Recorded so they don't get relitigated: no proficiency levels, no scoring, no certification, no assessment-validity claims. No second course until the first one has been run. No new architecture documents — [docs/architecture.md](docs/architecture.md) is the only one.
