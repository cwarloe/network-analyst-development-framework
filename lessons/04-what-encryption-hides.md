# Lesson 04 — What Encryption Hides

## At a glance

- **Part of:** [the course plan](../COURSE.md)
- **Version:** 0.1 — draft
- **Date:** 2026-08-19
- **Capability targets:** OC-2, OE-4
- **Evidence families:** EF-2, EF-5
- **Time:** about 2 hours
- **Requires:** [`assets/pcaps/04-tls.pcap`](../assets/pcaps/04-tls.pcap), and Wireshark or `tshark`. Zeek is useful but optional — its output is reproduced in the text.
- **Assumes:** [Lessons 02 and 03](02-reading-a-conversation.md). You can narrate a conversation and describe expected behavior.

## Why this lesson exists

Most of the traffic you will ever look at is encrypted, and the honest response to that is neither despair nor pretending otherwise. It is knowing exactly where the line falls.

There is a specific failure this lesson is built to prevent. An analyst learns which fields are visible in TLS, builds a working picture around them, and then those fields quietly stop being visible — not because of an attacker, but because a server operator upgraded a protocol version. The picture keeps returning results. It is just answering a different question than the analyst thinks it is.

This capture contains that exact situation, from a client that behaved identically both times.

## The capture

Two TLS connections, generated live by [`lab/generate-captures.py`](../lab/generate-captures.py). The same client, the same request, the same certificate, the same offered protocol versions — to two servers that answered differently.

**One thing to be clear about before you start.** That the two servers present the *same certificate* is something the lab knows because the lab configured it. It is not something this capture shows, and by the end of the lesson you will be able to say exactly why. Where the text below states it as fact, it is stating the lab's ground truth. Keeping that separate from what the evidence supports is the habit [lesson 01](01-what-the-analyst-is-for.md) started building, and this lesson is where it gets uncomfortable.

```
tshark -r assets/pcaps/04-tls.pcap -Y tls -T fields \
       -e frame.number -e tcp.stream -e ip.dst -e tls.handshake.type -e tls.record.length
```

Stream 0 goes to `198.51.100.20`. Stream 1 goes to `198.51.100.30`. Start by confirming the client did the same thing both times:

```
frame 4   ClientHello -> 198.51.100.20   supported_versions: 0x0304, 0x0303
frame 18  ClientHello -> 198.51.100.30   supported_versions: 0x0304, 0x0303
```

Identical offers. `0x0304` is TLS 1.3, `0x0303` is TLS 1.2, and the client offered both to both servers. **Whatever differs from here is the server's decision, not the client's.** Hold onto that.

## Connection one: TLS 1.2

The server at `198.51.100.20` chose `0x0303` and cipher `0xc030`. Frame 6 carries four handshake messages in the clear:

```
frame 6   ServerHello        65 bytes
          Certificate      1018 bytes
          ServerKeyExchange 300 bytes
          ServerHelloDone     4 bytes
```

That 1018-byte certificate is readable. Open frame 6 in Wireshark, or:

```
tshark -r assets/pcaps/04-tls.pcap -Y "tls.handshake.type==11" -V
```

```
issuer:  C=US, ST=Oregon, L=Portland, O=Contoso Ltd, CN=files.contoso-internal.example
subject: C=US, ST=Oregon, L=Portland, O=Contoso Ltd, CN=files.contoso-internal.example
notBefore: 2026-08-19 05:20:38 UTC
notAfter:  2027-08-19 05:20:38 UTC
```

(The validity window reflects the moment the lab generated this certificate. Regenerate the capture and it moves — see [the lab README](../lab/README.md).)

Read the issuer and the subject again. **They are the same.** This certificate is self-signed — no certificate authority vouches for it, the server is asserting its own identity, and the assertion is valid for exactly one year from the moment it was created.

Whether that matters depends entirely on context you do not have here. On a lab appliance it is unremarkable. On a service handling finance exports it is worth a question. Either way it is a **fact you can observe from a network sensor without decrypting anything**, and that is the point.

Against that, what stays hidden. Frames 10 and 11:

```
frame 10   Application Data   130 bytes
frame 11   Application Data   132 bytes
```

`Application Data` is TLS record type 23, and its contents are opaque. From lesson 02's plaintext conversation you could read `GET /api/v2/export?page=1` and the JSON that came back. Here you get two numbers. The request and the response happened; what they said is gone.

## Connection two: TLS 1.3

Same client, same certificate on the server, same offer. The server at `198.51.100.30` chose `0x0304` and cipher `0x1302`. Frame 18 is a ClientHello that looks like frame 4. Then frame 20:

```
frame 20   ServerHello                    122 bytes
           ChangeCipherSpec                 1 byte
           Application Data              1038 bytes
           Application Data               281 bytes
           Application Data                69 bytes
```

Count the handshake message types. There is a ServerHello, and after it there is nothing but opaque records.

Confirm it directly:

```
$ tshark -r assets/pcaps/04-tls.pcap -Y "tcp.stream==0 && tls.handshake.type==11" | wc -l
1
$ tshark -r assets/pcaps/04-tls.pcap -Y "tcp.stream==1 && tls.handshake.type==11" | wc -l
0
```

**The certificate is gone.** It is still being sent — it is inside that 1038-byte record — but from TLS 1.3 onward everything after the ServerHello is encrypted, including the server's identity. The self-signed certificate you found so easily in stream 0 is present, unchanged, and completely invisible in stream 1.

Nothing was attacked. Nobody hid anything from you deliberately. A server chose a newer protocol version, which is the correct and recommended thing for it to do, and a category of evidence you were relying on ceased to exist.

## The same two connections, in Security Onion's logs

Everything above came from the packets. Now run Zeek over the same file and look at what an analyst in Hunt or Kibana would actually have:

```
zeek -C -r assets/pcaps/04-tls.pcap
```

`ssl.log`, two rows — one per connection:

```
id.resp_h       version  cipher                                  server_name                      cert_chain_fps      sni_matches_cert
198.51.100.20   TLSv12   TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384   files.contoso-internal.example   a2ff156e37cff8c6…   T
198.51.100.30   TLSv13   TLS_AES_256_GCM_SHA384                  files.contoso-internal.example   -                   -
```

Read the last two columns. For the TLS 1.2 connection, Zeek recorded a certificate fingerprint and was able to check that the requested hostname matched the certificate. For the TLS 1.3 connection, both fields are `-`. Not false. **Absent.** Zeek could not see a certificate to fingerprint, so there was nothing to match against.

Then count the rows in each log:

```
conn.log    2 rows
ssl.log     2 rows
x509.log    1 row
```

`x509.log` is where certificate detail lives — subject, issuer, validity, key length, whether the cert is a CA. It is what almost every certificate-based detection and dashboard is built on. Two TLS connections went past the sensor, both presenting the same certificate, and **one of them produced a row**:

```
certificate.subject   CN=files.contoso-internal.example,O=Contoso Ltd,L=Portland,ST=Oregon,C=US
certificate.issuer    CN=files.contoso-internal.example,O=Contoso Ltd,L=Portland,ST=Oregon,C=US
certificate.key_alg   rsaEncryption   2048 bits
san.dns               files.contoso-internal.example
basic_constraints.ca  T
```

Subject equals issuer, right there in a searchable field. Anyone hunting for self-signed certificates finds this in one query.

And finds nothing at all for `198.51.100.30`, which is presenting the identical certificate.

This is the practical shape of the problem. It is not that TLS 1.3 makes analysis impossible. It is that **an entire log source silently thins out**, while every query you run against it keeps returning confident, correct, incomplete results. `conn.log` still has both connections. `ssl.log` still has both. `x509.log` has half of what you would expect, and nothing anywhere reports a gap.

## What survives

Not nothing. Compare the two ClientHellos:

```
frame 4    server_name: files.contoso-internal.example
frame 18   server_name: files.contoso-internal.example
```

**SNI is in the clear in both.** The client has to tell the server which host it wants before encryption is negotiated, so the hostname leaks in TLS 1.3 exactly as it did in TLS 1.2. Encrypted Client Hello exists to close this and is not in use here.

So from a sensor watching stream 1, with no decryption, you can still state:

- which host was requested, by name
- when, and for how long
- how many bytes travelled in each direction, and in what pattern
- that TLS 1.3 was negotiated, and which cipher
- the characteristics of the client's hello — its version list, extension ordering, cipher preferences — which fingerprint the client software

And you cannot state:

- what was requested or returned
- who the server claimed to be
- whether the certificate was valid, expired, or self-signed
- whether the response was a success or an error

The last one deserves emphasis. In lesson 02 you distinguished a 200 from a 403 inside an otherwise identical conversation. In stream 1 you cannot. A successful export and a refused one look the same from here, separable only by size and timing — which is inference, not observation.

## Your work product

Write **one page** assessing the two connections in this capture, for a reader who has not seen it.

Structure it in three parts, and keep them genuinely separate:

**1. What you observed.** Both streams. Facts only, each traceable to a frame.

**2. What you can reasonably infer, and on what basis.** Inference is allowed here — it is most of the job — but each one carries its evidence and its confidence. "Probably the same service" is fine if you say why and how sure.

**3. What cannot be determined from this capture, and what would be needed to determine it.** This is the section being assessed. For each item, name the source that would answer it. "Endpoint telemetry on the server would identify the process" is an answer. "More data" is not.

Address all of these inside that structure:

1. You have been told both connections carry the same certificate. **Prove it from the capture, or explain precisely why you cannot.** Then say what a reader of your assessment should conclude about any other claim you make that rests on the same kind of evidence.
2. A colleague says stream 1 is more suspicious than stream 0, because "we can't see anything in it." Respond.
3. The certificate in stream 0 is self-signed. State what that does and does not tell you, and what you would want to know before treating it as a finding.
4. Your organization has a detection that alerts on self-signed certificates, built on `x509.log`. Describe exactly what it does against this capture — how many of the two connections it evaluates, and what it reports. Then describe what happens to it as the estate moves to TLS 1.3, and say what you would monitor to notice that happening.
5. Stream 0 has 130 and 132 bytes of application data; stream 1's opaque records are 1038, 281 and 69 bytes. Can you conclude the requests differed? Justify carefully.
6. Name the one field that leaks the destination hostname in both streams, say why it must, and say what would remove it.

## The habit this is building

Lesson 05 is about choosing evidence sources, and this lesson is the argument for why that is a skill rather than a preference.

Your visibility is not a property of your sensors. It is a property of **other people's configuration choices**, changing continuously, without notification, made for good reasons that have nothing to do with you. A TLS version upgrade is a security improvement and a monitoring regression at the same time, and both are true.

The analyst who says "we have full packet capture, so we can see everything" has confused *having the packets* with *being able to read them*. You have every byte of stream 1. You cannot tell who the server said it was.

## Reviewing your own work

- Count the sentences in your "cannot determine" section. If it is shorter than your observation section, you have probably under-declared. This capture hides more than it shows.
- Did you state anywhere that stream 1 is encrypted and stream 0 is not? Both are fully encrypted. If you wrote that, work out where the idea came from — it is a common and expensive confusion.
- On question 2, did you actually answer it, or did you agree with your colleague? Reduced visibility is not evidence of wrongdoing. If it were, every well-configured server on the internet would be suspicious.
- On question 4, did you describe the detection as *broken*? It is not broken. It runs, it produces no false positives, and its coverage silently shrinks toward zero. That is worse than broken, because broken things get noticed.
- On question 5, did you distinguish what the byte counts *permit* you to say from what they *establish*? The two connections did carry different-sized handshakes, which is not the same as different requests.
- Would a reader of your assessment know which parts they could act on and which parts they could not?

## What this lesson does not do

It does not cover decryption, TLS interception, or key logging — all of which change this picture entirely and none of which are always available.

It does not cover Encrypted Client Hello, which removes the SNI leak this lesson relies on. When it is widespread, the observable set shrinks again, and lesson 05's reasoning is what carries you through that.

Two connections to two servers is a demonstration, not a survey. Real TLS deployments vary in ways this capture does not show.

It does not define proficiency, scoring, or completion. One assessment of one capture is a single sample.
