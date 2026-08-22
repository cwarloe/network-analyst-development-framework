# Reveal 2 — the work product

Open only after fields 1 to 5 are written. Leave them as they are.

## What the packets show

```
tshark -r assets/pcaps/e03-prediction.pcap -Y "tcp.stream==2" -T fields -e frame.number -e frame.time_relative -e ip.src -e tcp.dstport -e tcp.len
```

```
30	1.703133000	192.0.2.10	80	0
31	1.703245000	198.51.100.20	44102	0
32	1.703263000	192.0.2.10	80	0
33	1.703326000	192.0.2.10	80	135
34	1.703331000	198.51.100.20	44102	0
```

Handshake, a 135-byte request, and a bare acknowledgment from the server.

Then nothing.

## The fact that decides this

**Frame 34 is the last frame in the file.** The capture contains 34 packets in total:

```
capinfos -c assets/pcaps/e03-prediction.pcap
```

The conversation does not end in this capture. **The capture ends.**

That single fact reorganises everything else in the record:

- `server.bytes: 0` — no response bytes **were captured**. It does not say none were sent.
- `http.status_code` empty — Zeek recorded no status **within the file it was given**.
- `connection.state: S1` — established, not seen to close. Zeek is describing the file, not the conversation.

Every one of those fields is accurate. None of them is a statement about what the server did.

## Contradicted, or not tested?

This is the distinction the whole lesson is built around, and it is where most records go wrong.

If your prediction was *"the next application data comes from the server, if the application handles the request"* — **the evidence did not contradict that.** It did not test it. The capture stopped before the prediction's claim could be evaluated at all.

Writing *"my prediction was wrong"* in field 7 would be inaccurate. So would writing *"my prediction was confirmed."* The honest entry is that the evidence available cannot evaluate it, and that this is a property of the observation window rather than of the traffic.

**A prediction that cannot be evaluated is not a failed prediction.** It is an unfinished check, and knowing the difference is what stops an analyst reporting an absence as a finding.

## What the evidence does and does not support

Supported:

- A client opened a connection to `198.51.100.20:80`, sent a complete-looking `GET /v1/inventory/summary`, and the server's networking software acknowledged it.
- Within the captured window, no response bytes travelled back.

Not supported by anything here — and all of these remain live:

- The server never answered.
- The server answered and the response fell outside the capture.
- The application failed, hung, or was still working.
- Something on the path prevented a response.
- The connection was still open and healthy when the capture stopped.

**Silence at one observation point, for one window, is not evidence for any of these over the others.** It is the absence of evidence about all of them.

## What would distinguish them

Any of these would, and naming them is field 10's job:

- A capture covering a longer window.
- The server application's own logs for that request.
- A second observation point, closer to the server, showing whether a response was ever emitted.
- The client's own record of whether it received an answer.

## Compare with the worked example

Look at frame 5 and frame 34 side by side. Both are bare acknowledgments from the same server, on the same port, carrying zero bytes.

After frame 5, the client sent more.
After frame 34, the file ended.

**The same observable had two completely different continuations**, and nothing visible in either acknowledgment distinguished them at the time. That is why the prediction has to name a condition, and why the check has to distinguish an event from an absence.

## Now finish the record

Complete fields 6 to 10 without editing fields 1 to 5.

Field 7 is the one to be careful with: say which part of your prediction the evidence **engaged**, and which parts it **could not reach**. If the answer for every part is "could not reach," say that — it is a legitimate and complete result.

Then open the [review guide](review-guide.md).
