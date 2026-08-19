# Optional Just-in-Time Scaffolds

Use only the sections you need. These are reasoning supports, not a checklist and not the task's answer.

## Flow metadata

Flow records can show endpoints, ports, timing, duration, direction, volume, and repetition. They can establish that communication occurred and reveal patterns, but encrypted flow records generally cannot show the application content or its intent.

Ask: Which explanations predict this timing, volume, and peer pattern? What can the flow not distinguish?

## DNS and TLS names

A DNS response connects a queried name to an address at a point in time. TLS server-name and certificate metadata can connect a session to a presented identity. Neither proves that the identity is approved, benign, or controlled by the party you expect.

Optional technical references: [TLS 1.3](https://www.rfc-editor.org/info/rfc8446/) and [TLS server-name extensions](https://www.rfc-editor.org/info/rfc6066).

## Certificate validation

A validating certificate chain supports encrypted communication with the identity represented by the certificate under the trust configuration in use. Attackers and unauthorized services can also obtain valid certificates. Treat validation as one fact, not a verdict.

## Process lineage and signatures

Process lineage connects an initiating process to parent or child processes. A signature can identify a signer and indicate whether signed bytes changed after signing. Neither alone proves that the process was expected, uncompromised, or safely distributed.

Ask: What provenance, path, hash, module, or runtime comparison would discriminate between expected software and a shared compromise?

## Peer comparison

Similarity across peers can strengthen an expected-behavior explanation. It can also reveal a shared deployment error or supply-chain problem. The value of the comparison depends on whether the peers are meaningfully independent and what common mechanism they share.

## Confidence and action

Confidence describes how strongly the available evidence supports an assessment; it is not a substitute for explaining why. A proportionate action considers both security risk and operational cost.

Ask:

- What evidence supports the leading explanation?
- What credible alternative remains?
- What finding would change the decision?
- What is the least disruptive action that still manages the current risk?

## Documentation values

The `.example` namespace and `203.0.113.0/24` address block are reserved for documentation. They keep the exercise from identifying or sending learners toward a real service. See the [IANA special-purpose address registry](https://www.iana.org/assignments/iana-ipv4-special-registry/iana-ipv4-special-registry.xhtml) for address status.
