# Network Analyst Development Framework

Training material for network analysts working in cyber defense. It teaches the reasoning — how to frame a question, weigh evidence, hold competing explanations open, and hand off a judgment someone else can act on — through network subject matter rather than alongside it.

**This is a work in progress. Four of nine lessons exist.** They are listed below and you can read them right now.

## The lessons

| | Lesson | What you do in it | Needs |
|---|---|---|---|
| 01 | **[What the analyst is for](lessons/01-what-the-analyst-is-for.md)** | Pull apart observation, interpretation, and judgment on three small cases | Nothing |
| 02 | Reading a conversation | *Not written yet — unblocked, next up* | Capture data |
| 03 | Names and expectations | *Not written yet — unblocked* | Capture data |
| 04 | What encryption hides | *Not written yet — unblocked* | Capture data |
| 05 | **[Vantage point and evidence](lessons/05-vantage-point-and-evidence.md)** | Build an evidence plan, and work out what your sources can't tell you | Nothing |
| 06 | When it breaks | *Not written yet — needs a lab* | Lab environment |
| 07 | When it's suspicious | *Not written yet — unblocked* | Capture data |
| 08 | **[Judgment and handoff](lessons/08-judgment-and-handoff.md)** | Turn one analysis into a peer handoff and a manager summary | Nothing |
| 09 | **[Capstone — encrypted outbound traffic](lessons/09-capstone-encrypted-outbound-traffic/README.md)** | Work a full case, revise when new evidence lands, then transfer to an unrelated one | Nothing |

The four bolded lessons are complete and self-contained: each supplies its own case inline, and none needs capture files, tooling, or an account. Lesson 08 assumes 01–07, so it lands best with someone who already has some analysis or IT-ops background.

Start with **[lesson 01](lessons/01-what-the-analyst-is-for.md)**. It takes about 90 minutes and needs nothing but a text editor.

Four of the five unwritten lessons are now unblocked — [R004](docs/research/R004-pcap-and-telemetry-sourcing.md) established which public capture corpora can lawfully be republished here. Lesson 06 is the exception: no public dataset cleanly isolates network *failures* with known causes, so it needs a lab. See the [roadmap](ROADMAP.md).

## Using this with a learner

Every lesson ends in a work product — a written assessment, a plan, a handoff — not a quiz. There are no scores, levels, or pass marks anywhere in this repository, deliberately: nothing here has been validated well enough to grade anyone.

If you run a lesson with someone, please write down what happened in the capstone's [run records](lessons/09-capstone-encrypted-outbound-traffic/run-records.md). No lesson here has yet been used by anyone other than its author, which is the single biggest gap in the project.

## The rest of the repository

- **[COURSE.md](COURSE.md)** — the nine-lesson plan and why it's ordered this way
- **[ROADMAP.md](ROADMAP.md)** — what happens next
- **[docs/architecture.md](docs/architecture.md)** — the design principles the lessons follow, and the honest limits on what this project has established
- **[docs/capability-model.md](docs/capability-model.md)** and **[docs/evidence-model.md](docs/evidence-model.md)** — the vocabulary lessons refer to (OE-2, EF-1, and so on)
- **[docs/research/](docs/research/)** — the research the design rests on
- **[docs/archive/](docs/archive/)** — superseded design documents and decision records, kept for history

## License

[CC BY-NC-SA 4.0](LICENSE). Share and adapt with attribution, noncommercially, under the same terms. Commercial use requires separate permission.
