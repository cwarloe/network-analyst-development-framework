# Predict Before You Look

## At a glance

- **Part of:** [Book 1 — Learning to See](../BOOK-1.md), Episode 3
- **Version:** 0.1 — draft
- **Date:** 2026-08-22
- **Capability targets:** IR-3, LR-1, LR-2
- **Evidence families:** EF-3, EF-8
- **Time:** about 60–75 minutes
- **Requires:** nothing. No capture, tooling, or account.
- **Assumes:** [lesson 02](02-reading-a-conversation.md). You can narrate a simple conversation and keep transport success separate from application success.

## Why this lesson exists

It is easy to explain evidence after you have seen it. The result is sitting in front of you, making the path to it look inevitable.

Prediction removes that advantage. Before the next observation appears, you write what your explanation says should happen. The prediction does not have to be right. It has to be specific enough that reality can disagree with it.

That disagreement is useful. It tells you which part of your model, assumption, or explanation needs work.

The working move is:

> **Explain → predict an observable result → check → identify the difference → revise**

This is not guessing. A guess has no visible basis. A prediction says *because I currently think X, I expect to observe Y; if I observe Z instead, I will reconsider X.*

## Keep a prediction record

For each case, use four short fields:

1. **Current explanation:** What do you think is happening?
2. **Prediction:** What specific observation should appear next if that explanation is right?
3. **Result:** What appeared?
4. **Revision:** What changed in your explanation, and why?

Write the first two before continuing to the result. Do not repair them after the reveal. The difference between the before and after is the work product.

## Worked example — a connection that should complete

### What you have

A client sends a TCP SYN to a web server. The server returns SYN-ACK, and the client returns ACK. The client then sends an HTTP request.

### Current explanation

The client established a two-way TCP connection and delivered an HTTP request to a listening service.

### Prediction

If the service processes the request normally, the next application data should travel from server to client and contain an HTTP response. A successful response is plausible, but the completed handshake does not predict a `200` specifically.

That final sentence matters. The model predicts **direction and kind of event**, not an outcome the evidence does not support.

### Result

The server acknowledges the request immediately. Four seconds pass with no packets. It then returns `HTTP/1.1 200 OK`.

### Comparison and revision

The predicted response appeared, but not on the expected timescale. The immediate TCP acknowledgment shows that the request arrived. The four-second silence occurred after delivery and before the application response.

Revised explanation: the network delivered the request promptly; the observed delay is consistent with time spent in or behind the application before it generated a successful response.

Notice what did not happen. The explanation was not replaced with “the server is slow.” That would outrun the evidence. The observation located the delay more precisely; it did not reveal the internal cause.

## Guided case — two reasonable predictions

### Evidence packet A

At 09:14:22, a managed workstation completes a short HTTP request to an internal file service. The response is `200 OK`. Four tenths of a second later, the same source IP opens a new connection to the same server and service port.

Stop here. Write:

- one current explanation;
- one assumption your explanation depends on; and
- the next application event you predict.

Do not make your prediction “there will be traffic.” Name its direction and purpose as far as the evidence supports.

### Evidence packet B

The second connection completes its handshake. The client uses the same user-agent string as the first connection and sends:

```text
GET /api/v2/admin/users HTTP/1.1
```

The server returns:

```text
HTTP/1.1 403 Forbidden
```

Record the result before reading on.

Now compare:

1. Which part of your prediction was supported?
2. Which part was unsupported or contradicted?
3. Did you predict a person, a process, or only a client? Which evidence justified that choice?
4. Does the `403` require you to revise an explanation of the **network connection**, the **application request**, or both?

Two predictions could have been reasonable from packet A:

- another request related to the completed export, because the same client reconnects almost immediately; or
- an unrelated request, because source IP, destination, and timing do not establish one process or workflow.

What distinguishes a prediction from a guess is not whether it matched. It is whether its basis and assumptions were visible before the result.

### Your revision

Write a replacement explanation in no more than three sentences. It must preserve all of these:

- two separate TCP connections completed;
- the same user-agent string appeared in both HTTP requests;
- the second request was refused by the application;
- the evidence does not establish a person, intent, authorization, or whether the two requests are one workflow.

## Independent case — the missing response

This case is staged. Stop at each line marked **Commit before continuing**.

### Stage 1 — report and first observation

> A user reports that an internal service “refuses every connection.”

The client sends a SYN to the service.

**Commit before continuing:**

- Separate the user's report from the packet observation.
- Write two plausible explanations.
- For each explanation, predict the next packet or absence that would support it.

### Stage 2 — one second later

No packet has returned. The client retransmits the SYN.

**Commit before continuing:**

- Record the result.
- Rank your two explanations.
- Predict what should happen next under the leading explanation.
- Name one assumption that keeps you from ruling out the other explanation.

### Stage 3 — eleven seconds later

The client has sent eight SYNs with widening intervals. No response appears in the available capture.

**Commit before continuing:**

- Record the result.
- Write your current explanation.
- State what the capture proves and what it does not prove.
- Name the next evidence that would best distinguish outbound delivery failure, return-path failure, silent policy drop, and an observation-point gap.

### Stage 4 — evidence from another source

A firewall on the path records the first SYN arriving and a policy rule silently dropping it. No reject packet was configured or sent.

Complete the revision record:

- Which initial explanation survived?
- Which prediction was most useful?
- Which claim became supportable only after the firewall record arrived?
- Why was “the service refused the connection” inconsistent with the packet evidence even before Stage 4?

## Your work product

Submit the prediction record for the independent case. Keep the original entries intact and add revisions beneath them.

Then add a short reflection:

1. Where did your observed result differ from your prediction?
2. Was the error in technical knowledge, an unstated assumption, or a claim that was too specific?
3. What would you predict earlier or more precisely in the next case?

Do not write that you should “study TCP” or “look more carefully.” Name the model or assumption that needs attention.

## Reviewing your own work

- Were predictions written before their results appeared?
- Could another reader tell what observation would have counted against each explanation?
- Did you preserve a reasonable initial explanation even when later evidence changed the answer?
- Did the revision explain the change, or merely replace the old answer?
- Did you treat no response as proof of a firewall drop before the firewall record existed?
- Is the learning need specific enough to change what you do on the next case?

There is no preferred wording and no score. The evidence is the visible before-and-after reasoning.

## Carry this into the rest of the course

When a later lesson says **before you look**, make a real commitment:

> I currently think ___ because ___. If that is right, I expect to observe ___. If I observe ___ instead, I will reconsider ___.

You will use that move in DNS, TLS, troubleshooting, suspicious traffic, and the capstone. The technology changes. The method does not.

## What this lesson does not do

It does not teach every cause of an unanswered SYN or establish that you can diagnose path failures. [Lesson 06](06-when-it-breaks.md) develops that technical subject with captures. This lesson uses a small case to make prediction and revision visible before later problems become more complex.

One prediction record does not establish proficiency, consistency, or transfer.
