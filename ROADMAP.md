# Roadmap

Four of nine lessons are written. Here's what's actually in the way, in order.

## 1. Run a lesson with a real person

**Nothing in this repository has been used by anyone other than its author.** That is the biggest risk the project has, and it is a few hours of work to reduce.

[Lesson 01](lessons/01-what-the-analyst-is-for.md) needs no prerequisites and works with a complete beginner. The [capstone](lessons/09-capstone-encrypted-outbound-traffic/README.md) is the fuller test and works with anyone technical. Write down what happens in the [run records](lessons/09-capstone-encrypted-outbound-traffic/run-records.md) — coverage, what got noticed, where people got stuck, how long it took.

Everything else on this list is guesswork until this happens once.

## 2. Settle where the packet captures come from

Five lessons — 02, 03, 04, 06, 07 — are blocked on this and cannot be written without it.

The problem is that authentic capture data and redistributable capture data are frequently not the same data. This repository is published under CC BY-NC-SA 4.0, which constrains what can be embedded in it. The question to answer: which public capture corpora can lawfully ship inside published training material, and what has to be generated in a lab instead.

An AI research prompt for this exists and is being run separately. When the answer lands, captures go in `assets/pcaps/` and `assets/telemetry/`.

## 3. Write the remaining lessons

02, 03, 04, 06, 07 in that order, gated on item 2. See [COURSE.md](COURSE.md) for what each one covers.

## 4. Answer three design questions

These change the shape of the remaining lessons and are cheap to settle:

- **Who is the learner?** Currently assumed to be someone with no analysis experience and no tooling background. Working IT staff would compress lessons 02–04 considerably.
- **Self-guided or instructor-led?** Decides whether feedback comes from a review guide or a person.
- **How many hours?** Currently drafted at roughly 20–30. Less means cutting lessons, not thinning all of them.

## Not doing

Recorded so they don't get relitigated: no proficiency levels, no scoring, no certification, no assessment-validity claims. No second course until the first one has been run. No new architecture documents — [docs/architecture.md](docs/architecture.md) is the only one.
