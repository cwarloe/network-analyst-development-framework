# Later case: the export that never arrived

Try this about 7–14 days after the capstone and its immediate transfer case. Allow 20 minutes. The interval is a practical pilot choice, not a proven optimum. Record the actual gap and any related work or practice in between.

Start without earlier lesson answers, review guides, search, or AI assistance. If you need help, save your initial attempt, then consult it and record what you used. You may write in any clear format. No particular table, label, or vocabulary is required.

This is a fictional written case. All evidence is supplied; no environment, packet capture, or live lookup is needed. It samples reasoning after a delay, not hands-on tool use or workplace performance.

## The decision

An operations manager reports that a stock export requested at 14:00 has not arrived. A ticket says, "The network dropped the export while the workstation was uploading stolen data." The manager wants to know whether to isolate the workstation or let the clerk retry. No containment has been authorized.

You have 20 minutes to give the shift lead an assessment and a next step. The export supports tomorrow's stock allocation. Isolation would stop that workstation's packing-label work as well.

## What is available

| ID | Source and observation | Limits |
|---|---|---|
| L-01 | Browser request record: `POST /exports` at 14:00 received HTTP `202 Accepted`, job ID `J718`. | In this application's documented contract, 202 means queued, not completed. The response is not an export file. |
| L-02 | Packet summary between the workstation and the export service: TCP connection established, TLS session established, bidirectional bytes, orderly connection close. | Payload is encrypted. These observations do not show the request's content, successful job completion, or what was in any response body. |
| L-03 | Job service log for `J718`: queued at 14:00; worker started at 14:01; database access denied at 14:01; job failed. | The record addresses this job. It does not establish why permission was denied or what happened on the workstation. |
| L-04 | A second office submitted `J719` at 14:03 through a different network path. Its job service log shows the same database denial and failed state. | This comparison favors a shared application dependency but does not prove every network path is healthy. |
| L-05 | A database-role change was applied at 13:55. The application owner has not checked its effective permissions. | Timing alone does not establish that this change caused the failures. |
| L-06 | An egress sensor saw the workstation exchange 28 MB over TLS with `storage.partner.example` between 13:50 and 14:05. | The sensor cannot identify the process or payload. There is no peer comparison or earlier baseline in the packet supplied. |
| L-07 | The asset register says this workstation is permitted to use an approved cloud backup client. The endpoint team has a process-to-connection record covering this time, retained for only another two hours. | Permission to run a client does not establish which process made L-06 or approve every destination or transferred file. The endpoint record has not yet been retrieved. |

## Your work

Write a short handoff that tells the shift lead what you think happened, what remains unresolved, and what to do next. Support it with the evidence above. Include the checks most likely to change your recommendation, who should perform them, and what would justify changing the operational action. State how confident you are and why.

Save this first version before opening [the discussion and follow-up evidence](later-case-review.md). Do not replace the first version with your revision.
