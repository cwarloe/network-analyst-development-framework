# What these fields are called in Security Onion

Every lesson that touches a log shows the field names **an analyst actually searches on in Security Onion** — in Hunt, in Kibana, in a dashboard. Those are not the names Zeek writes.

Zeek writes `id.orig_h`. Security Onion's ingest pipeline renames it to `source.ip` before it reaches Elasticsearch. An analyst working a case never types `id.orig_h` and has no reason to know it exists.

The lessons therefore use the Security Onion names. This page is the mapping, for two situations:

- **You are running Zeek yourself** against a capture from `assets/pcaps/`. You will see the native names in the TSV output, and this table tells you which lesson field they correspond to.
- **You are reading someone else's Zeek documentation or a blog post.** Almost all of it uses native Zeek names.

## Where these came from

Security Onion's Elasticsearch ingest pipelines, which are the authority — not documentation about them:

- [`zeek.common`](https://github.com/Security-Onion-Solutions/securityonion/blob/2.4/main/salt/elasticsearch/files/ingest/zeek.common)
- [`zeek.conn`](https://github.com/Security-Onion-Solutions/securityonion/blob/2.4/main/salt/elasticsearch/files/ingest/zeek.conn)
- [`zeek.dns`](https://github.com/Security-Onion-Solutions/securityonion/blob/2.4/main/salt/elasticsearch/files/ingest/zeek.dns)
- [`zeek.http`](https://github.com/Security-Onion-Solutions/securityonion/blob/2.4/main/salt/elasticsearch/files/ingest/zeek.http)
- [`zeek.ssl`](https://github.com/Security-Onion-Solutions/securityonion/blob/2.4/main/salt/elasticsearch/files/ingest/zeek.ssl)
- [`zeek.x509`](https://github.com/Security-Onion-Solutions/securityonion/blob/2.4/main/salt/elasticsearch/files/ingest/zeek.x509)

Read against the `2.4/main` branch on 2026-08-19. **Pipelines change between releases — check yours before relying on this.** On a live deployment they are at `/opt/so/conf/elasticsearch/ingest/`.

A note on standards: Security Onion is ECS-influenced but not strictly ECS. HTTP is the clearest case — it uses `http.method` and `http.status_code`, where strict ECS would be `http.request.method` and `http.response.status_code`. **The names below are what Security Onion actually produces**, which is what matters when you are searching it.

## Common to every Zeek log

| Zeek | Security Onion |
|---|---|
| `ts` | `event.ingested` (Kibana's time column is `@timestamp`) |
| `uid` | `log.id.uid` |
| `id.orig_h` | `source.ip` — also copied to `client.ip` |
| `id.orig_p` | `source.port` — also copied to `client.port` |
| `id.resp_h` | `destination.ip` — also copied to `server.ip` |
| `id.resp_p` | `destination.port` — also copied to `server.port` |
| `community_id` | `network.community_id` |
| *(log type)* | `event.dataset` — `conn`, `http`, `dns`, `ssl`, `x509` |

`log.id.uid` is the pivot. Every log Zeek wrote about one conversation carries the same value, so it is how you get from a connection to the HTTP request inside it.

## conn

| Zeek | Security Onion |
|---|---|
| `proto` | `network.transport` |
| `service` | `network.protocol` |
| `duration` | `event.duration` |
| `orig_bytes` | `client.bytes` |
| `resp_bytes` | `server.bytes` |
| `orig_pkts` / `resp_pkts` | `client.packets` / `server.packets` |
| `missed_bytes` | `connection.bytes.missed` |
| `conn_state` | `connection.state` |
| `history` | `connection.history` |
| — | `network.bytes`, computed as `client.bytes + server.bytes` |
| — | `connection.state_description`, plain English for the state code |

**`connection.state_description` has no Zeek equivalent** — Security Onion adds it. The values:

| `connection.state` | `connection.state_description` |
|---|---|
| `S0` | Connection attempt seen, no reply |
| `S1` | Connection established, not terminated |
| `SF` | Normal SYN/FIN completion |
| `REJ` | Connection attempt rejected |
| `RSTO` | Connection established, originator aborted (sent a RST) |
| `RSTR` | Established, responder aborted |
| `SH` | Originator sent a SYN followed by a FIN, we never saw a SYN ACK |
| `OTH` | No SYN seen, just midstream traffic |

## http

Note the departures from strict ECS.

| Zeek | Security Onion |
|---|---|
| `method` | `http.method` |
| `host` | `http.virtual_host` |
| `uri` | `http.uri` |
| `status_code` | `http.status_code` |
| `status_msg` | `http.status_message` |
| `user_agent` | `http.useragent` |
| `request_body_len` | `http.request.body.length` |
| `response_body_len` | `http.response.body.length` |
| `version` | `http.version` |
| `resp_mime_types` | `file.resp_mime_types` |

## dns

| Zeek | Security Onion |
|---|---|
| `query` | `dns.query.name` |
| `qtype_name` | `dns.query.type_name` |
| `qclass_name` | `dns.query.class_name` |
| `rcode` | `dns.response.code` |
| `rcode_name` | `dns.response.code_name` |
| `answers` | `dns.answers.name` |
| `TTLs` | `dns.ttls` |
| `trans_id` | `dns.id` |
| `rtt` | `event.duration` |
| `AA` / `TC` / `RD` / `RA` | `dns.authoritative` / `dns.truncated` / `dns.recursion.desired` / `dns.recursion.available` |
| — | `dns.resolved_ip`, the answers that are valid IP addresses |
| — | `dns.query.length`, the character length of the query name |

**`dns.resolved_ip` and `dns.query.length` have no Zeek equivalent.** Security Onion computes both. `dns.query.length` in particular turns "that name looks suspiciously long" into something you can actually search for.

## ssl

| Zeek | Security Onion |
|---|---|
| `version` | `ssl.version` |
| `cipher` | `ssl.cipher` |
| `curve` | `ssl.curve` |
| `server_name` | `ssl.server_name` |
| `established` | `ssl.established` |
| `resumed` | `ssl.resumed` |
| `validation_status` | `ssl.validation_status` |
| `cert_chain_fps` | `tls.server.hash.sha256` |
| `client_cert_chain_fps` | `tls.client.hash.sha256` |
| `ja3` / `ja3s` | `hash.ja3` / `hash.ja3s` |

**`sni_matches_cert` and `ssl_history` are not mapped.** Zeek writes them; the pipeline does not carry them across, so they are not searchable in Security Onion. That is worth knowing before you build anything on them — and it is a good small illustration of a point [lesson 04](04-what-encryption-hides.md) makes at length: what you can see is a property of your pipeline, not only of the wire.

## x509

| Zeek | Security Onion |
|---|---|
| `certificate.subject` | `x509.certificate.subject` |
| `certificate.issuer` | `x509.certificate.issuer` |
| `certificate.not_valid_before` | `x509.certificate.not_valid_before` |
| `certificate.not_valid_after` | `x509.certificate.not_valid_after` |
| `certificate.key_alg` | `x509.certificate.key.algorithm` |
| `certificate.key_length` | `x509.certificate.key.length` |
| `certificate.serial` | `x509.certificate.serial` |
| `san.dns` | `x509.san_dns` |
| `basic_constraints.ca` | `x509.basic_constraints.ca` |
| `fingerprint` | `hash.sha256` |
| `id` | `log.id.fuid` |

## Running Zeek yourself

The lessons tell you to run `zeek -C -r <capture>`. That produces the **native** names in the left column, not the Security Onion names in the right. Nothing is wrong; you are looking at the same data one stage earlier in the pipeline.

If you want output that is closer to what Security Onion indexes, `zeek -C -r <capture> LogAscii::use_json=T` gives JSON, which is the form the ingest pipeline consumes — though the field names are still Zeek's until the pipeline renames them.
