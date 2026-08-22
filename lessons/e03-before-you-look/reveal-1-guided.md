# Reveal 1 — the guided practice

Open only after your five entries are written.

## What the packets show

```
tshark -r assets/pcaps/e03-prediction.pcap -Y "tcp.stream==1 && frame.number<=22" -T fields -e frame.number -e frame.time_relative -e ip.src -e tcp.dstport -e tcp.len
```

```
13	1.001426000	192.0.2.10	9110	0
14	1.001583000	198.51.100.30	44103	0
15	1.001609000	192.0.2.10	9110	0
16	1.001802000	198.51.100.30	44103	36
17	1.001829000	192.0.2.10	9110	0
18	1.001888000	192.0.2.10	9110	17
19	1.001910000	198.51.100.30	44103	0
20	1.001946000	198.51.100.30	44103	25
21	1.001989000	192.0.2.10	9110	16
22	1.002047000	198.51.100.30	44103	1035
```

Frames 13 to 15 are the handshake. Then **frame 16 carries 36 bytes from `198.51.100.30` — the server — and the client has sent no application data at all.**

The 36 bytes are readable:

```
220 hsync-1.4 inventory sync ready
```

The client answers in frame 18 with 17 bytes (`HELLO agent/1.4`), the server acknowledges it in frame 20, the client asks for something in frame 21, and frame 22 returns 1,035 bytes.

**The server spoke first.**

## The assumption

Most predictions here get the *shape* right — a small ask, a large answer, and the 39-against-1,105 byte split makes that nearly unavoidable. The part that usually fails is direction, and it fails on an assumption almost nobody writes down until asked:

> **The side that opens the connection is the side that sends the first application data.**

That is true of HTTP. It is true of most traffic you have looked at. It is not true in general, and it was never stated by any field in the connection record.

Services that greet the client on connect are ordinary — mail transfer, file transfer, and remote shell protocols all do it. Nothing here is exotic. It is simply a family of protocols that the web has made easy to forget.

## What the port did not tell you

`destination.port` was `9110`. That number named nothing, and `network.protocol` was empty because Zeek did not recognise the protocol either.

An empty `network.protocol` is an observation about what Zeek could classify. It is not an observation about the traffic, and it is not a reason for suspicion.

## A confirmation you can check

Zeek's `connection.history` for this conversation reads `ShAdDafF`. In that string a lowercase letter is the responder and an uppercase letter is the originator, so `d` before `D` records that **the responder sent data before the originator did** — the same fact frame 16 shows directly.

You do not need the history string to answer this; the frames are enough. It is here because a second, independent way to check the same fact is worth knowing exists.

## Separating what was contradicted from what was not

If you predicted *"the client sends a request, the server returns a larger response"*, then:

- the **direction of the first application data** was contradicted;
- the **size relationship** was not — the server did send far more than the client;
- the **kind** was not tested in any strong sense, because you had no basis to name a protocol and correctly did not.

One named part failed. That is a more useful result than a prediction general enough to survive anything.

## What remains unresolved

What this service is *for* is not established. A banner, a greeting exchange, and a manifest of 28 inventory lines is what the conversation contains; whether it is an approved agent, how often it runs, and who owns it are not in this capture.

Go back to your five entries. Do not edit them. Then continue with [your work product](README.md#your-work-product--the-conversation-that-stops).
