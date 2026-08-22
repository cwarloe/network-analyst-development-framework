# Review and Self-Review Guide

For the record produced in [Episode 3](README.md). Use it on your own work, or with a reviewer.

**This is not a rubric and there is no preferred prediction.** Two learners can write different predictions from the same record and both be reasoning well. What is being reviewed is whether the reasoning was *checkable* and whether the revision was *earned* — not whether the prediction matched what the evidence turned out to show.

Nothing here defines a score, a level, or a threshold. One record is one performance.

## Review the prediction, on the evidence available then

The only fair question about fields 1 to 5 is whether they were defensible **before** the reveal. Judge them against what was on the page at that point, not against the outcome.

- **Was the prediction recorded before the result?** If fields 1 to 5 were written or adjusted after opening the reveal, the record cannot show a revision, and nothing below can be assessed. This is the one condition the exercise genuinely depends on.
- **Was it specific enough for evidence to disagree?** A prediction naming a direction, a kind, and a condition can fail in three separable ways. *"Something will happen next"* cannot fail at all, and a prediction that cannot fail has told you nothing about your model.
- **Is the evidence basis visible?** Field 2 should name specific fields or frames. *"From the connection record"* is not a basis; `server.bytes: 0` and `connection.state: S1` are.
- **Was a material assumption identified, and is it actually material?** Field 3 should contain something that, if false, changes the prediction. *"I assume the network works"* usually is not material here. *"I assume the request was complete"* or *"I assume the side that opened the connection speaks first"* are.
- **Did they state what would weaken it?** Field 5 is where a model becomes falsifiable. If it is empty or generic, the prediction was probably a description of the expected outcome rather than a test of a model.

## Review the comparison

- **Did they distinguish contradiction from incomplete evidence?** This is the sharpest question in the exercise. Evidence that stops before a claim can be evaluated has not refuted it. A record that says *"my prediction was wrong"* about the work-product case has misread an absence as a result.
- **Did they identify which specific part the evidence engaged?** A prediction with three commitments rarely fails in all three. Naming the one that failed — and the ones that were never tested — is more useful than a verdict on the whole.
- **Did the original entry survive?** Compare fields 4 and 8. If field 4 has become broad enough to accommodate whatever field 6 says, the trace has been edited rather than written. Look for hedging that appeared after the fact: *"I expected a response or possibly other activity."*

## Review the revision

- **Does it explain why the model changed, or only restate the outcome?** *"The client sent more data"* is the observation. *"An acknowledgment does not establish that a request is complete, so I cannot use one to predict a response"* is the revision. Field 8 needs the second kind.
- **Is the revision proportionate?** Watch both directions. Replacing an entire working model because one assumption failed is over-correction. Changing nothing because the outcome was *"basically what I said"* is under-correction. In the worked example the model survived and a single assumption inside it did not — that is the usual proportion.
- **Was uncertainty the evidence did not resolve preserved?** Field 9 should still contain something. New evidence answers some questions and leaves others untouched; a record where everything resolved has usually absorbed the uncertainty rather than kept it.

## Review the learning need

- **Is field 10 specific enough to change a future performance?** *"Be more careful"* will not. *"Check whether the declared body length matches the bytes actually sent before predicting a response"* will, because it names a check that can be performed at a specific moment.
- **Does it come from the observed difference**, or is it a general resolution that could have been written before the exercise?

## Discussion questions

Useful with a reviewer, or as a second pass alone.

1. In the worked example, `Content-Length: 84` was visible in frame 4 before the prediction was made. What would have had to be true for you to look at it at that moment? What made it easy to skip?
2. The guided-practice record contained no field stating who would speak first. Where did your expectation about that come from, if not from the record?
3. Frame 5 and frame 34 are both bare acknowledgments from the same server on the same port. What, if anything, could have distinguished them **at the time**?
4. You have now written three predictions. Which of the three was most specific, and did being more specific make it more or less likely to survive?
5. If a colleague handed you the work-product record and said *"the server didn't respond,"* what would you ask them?

## For a reviewer

Two things to protect.

**Do not supply the prediction.** The value is in the learner committing to something they can be wrong about. A reviewer who suggests what to expect removes the only mechanism the exercise has.

**Do not treat a wrong prediction as a poor performance.** The worked example is built around a reasonable prediction that fails, precisely so the learner has seen that happen before it happens to them. A well-reasoned wrong prediction with a clean revision trace is a better outcome than a vague prediction that could not be wrong.

The one thing worth pushing on is field 7. Learners tend to compress it into a verdict — *right* or *wrong* — and the useful content is the part that says which commitment the evidence touched and which it left alone.

## What this review does not establish

That the learner can predict reliably, that they have understood TCP, or that they will transfer this to unfamiliar evidence. Three predictions on one synthetic capture is a single sample of one behaviour under favourable conditions, with the reveal a click away.
