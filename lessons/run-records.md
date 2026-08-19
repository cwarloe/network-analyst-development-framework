# Running a lesson, and recording what happened

Nine lessons exist. **None has been used by anyone other than their author.** Until that changes, the sequence is a design proposal that reads well, and every judgment in it is untested.

This file is how a run becomes evidence instead of an impression. It covers any lesson, not just the capstone.

## Which lesson to run first

| If your reader is… | Run | Why |
|---|---|---|
| A complete beginner | [01](01-what-the-analyst-is-for.md) | 90 minutes, no tools, no prerequisites |
| Technical, no analysis background | [02](02-reading-a-conversation.md) | First lesson with a capture — tests whether the packet-plus-Zeek format works at all |
| An experienced analyst | [09 capstone](09-capstone-encrypted-outbound-traffic/README.md) | The fullest test, and it stages evidence so a first answer must be revised |
| Willing to give you a day | 01 → 02 → 09 | Tests the entry point, the format, and the endpoint |

If you can only get one person for one hour, run **lesson 01**. It has no dependencies and every later lesson rests on the habit it builds.

## How to be in the room

The hard part of facilitating is **not helping**. The lessons are designed so that being stuck is informative, and a facilitator who smooths the path destroys the only data the run can produce.

- **Say almost nothing.** Hand over the lesson, say roughly how long it should take, and be available for questions. Do not walk them through it.
- **When they ask a question, note it before answering.** The question is the finding. Answer it afterwards if you like — but write down what they asked, at what point, and whether the lesson should have answered it.
- **Let them be stuck for longer than is comfortable.** Two silent minutes on a hard question is normal and productive. Rescuing them at thirty seconds tells you nothing.
- **Do not defend the material.** If they say a section is confusing, the section is confusing. Write it down; do not explain what it really meant.
- **Do not tell them the answer is coming later.** If they resolve something the lesson meant to be irresolvable, that is a finding about the lesson.
- **Watch where their eyes go.** In the capture lessons, whether they open the file at all — and whether they reach for Wireshark or the Zeek log first — says a lot about whether the workflow framing landed.

If you cannot be present, self-guided is fine and is how the material is written. You lose the stall data and keep the work product.

## What a run is meant to tell us

Not whether the learner is any good. **Whether the material and the models behind it describe real analyst work.** Record against these signals:

1. **Coverage.** Did the work product fall inside the six capability domains, or did some of it have no home? Work with no home is the most useful finding here.
2. **Observability.** Which evidence families (EF-1 through EF-8) actually appeared? Which stayed invisible, and was that the task's fault or the model's?
3. **Discrimination.** Did the review questions distinguish stronger reasoning from weaker, or did every answer look the same through them?
4. **Scaffold use.** What did they reach for, when, and did it unblock their reasoning or replace it?
5. **Friction.** Where did they stall, misread the task, or ask a clarifying question? Task-design problems and model problems look different and should be recorded separately.
6. **Time.** Actual against the lesson's estimate.

### Things worth watching for specifically

These are the load-bearing claims in the sequence. If any fails in a real run, it matters more than a wording fix:

- **Lesson 02** — does anyone separate *the connection worked* from *the request worked* without being told twice? The whole layered-evidence idea rests on that landing.
- **Lesson 03** — does the point arrive that the strange-looking DNS is *normal*, or does it read as a trick question? If it reads as a trick, the lesson is teaching cynicism instead of baselines.
- **Lesson 04** — does anyone conclude that the TLS 1.3 stream is more suspicious because less is visible? That is the error the lesson exists to prevent, so seeing it happen is a success for the run and a problem for the lesson.
- **Lesson 06** — do `REJ` and `S0` get different owners, or do both go to "the network team"?
- **Lesson 07** — does the benign case get argued seriously, or does everyone skip to the verdict? If the benign section is consistently thin, the task is not forcing it hard enough.
- **Any lesson** — does the self-review section get done at all, or abandoned once the work product is written?

## How to record a run

Add a dated entry below. Roughly a page. Include the learner's work product, or a summary, **only with their agreement** — note which was used.

- **Date and context:** when, how they were recruited, rough background, observed or self-guided, which lesson.
- **What happened:** where they went, what they produced, where they stalled.
- **Signals:** findings against the six above.
- **Revisions indicated:** specific changes to the lesson, the capability model, or the evidence model — or explicitly none.
- **Claims not supported:** what this run does *not* establish. One run establishes neither proficiency nor curriculum validity.

A run that changes nothing is still a result worth recording. A run that exposes a gap should produce a specific revision, not a general intention to improve.

## Records

No runs recorded yet. Nothing in this repository has been used by anyone other than its author.
