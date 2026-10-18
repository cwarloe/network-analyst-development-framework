# What Encryption Leaves Behind

## At a glance

- **Part of:** [the narrative track](README.md) · read before [Lesson 04](../lessons/04-what-encryption-hides.md)
- **Version:** 0.1 — draft
- **Date:** 2026-08-22
- **Time:** about 12 minutes
- **Requires:** nothing. No tooling, capture, or account.
- **Creates the question:** When transport encryption conceals application payloads and certificates, what claims can network evidence still legitimately support?

---

By the middle of my second month at Harrowmere Equipment Group, I had developed an unhealthy attachment to plaintext.

Plaintext was honest. In unencrypted traffic, if an application requested a finance report, the URI string sat right there in the packet payload. If the server returned an error, the response headers told you why. You could trace a conversation from the opening SYN packet through every data segment to the closing FIN handshake, and whatever the machines said to each other was available for anyone with a network tap to inspect.

Then Dana Shah assigned me to monitor an application test on our internal file repository.

The file server—`files.harrowmere-group.example` at `198.51.100.30`—was being evaluated by Leah Moreno’s enterprise applications team for automated synchronizations. To evaluate new transport configurations, Leah had generated two live test connections from an internal host at `192.0.2.10`. Both used port 443. Both targeted the same internal service.

I opened our terminal dashboard and queried the [[zeek_conn_log|Zeek connection log (`conn.log`)]]. Both connections were present. Both showed normal establishment and clean teardowns. But when I inspected the protocol logs and packet captures, the two sessions looked completely different.

Connection 1, using ephemeral port 51000, had negotiated TLS 1.2. In Wireshark, the handshake laid its cards on the table. In Frame 4, the client sent a `ClientHello` advertising the [[server_name_indication|Server Name Indication (SNI)]] for `files.harrowmere-group.example`. In Frame 6, the server replied with a `ServerHello`, selected cipher suite `0xc02f`, and then—in plain view—handed over its full cryptographic certificate. 

I opened Zeek’s `x509.log` and saw the certificate parsed into structured fields. The subject was `files.harrowmere-group.example`. The issuer was also `files.harrowmere-group.example`. It was an unverified [[self_signed_cert|self-signed certificate]], generated locally for internal staging.

Then I examined Connection 2, initiated from port 51002.

The client sent a `ClientHello`. The server answered with a `ServerHello`. And then, immediately following Frame 24, all visible structure stopped. The server certificate was gone. The handshake exchange was gone. Every subsequent record in Wireshark was labeled as an opaque `Application Data` frame with Content Type 23. 

I switched over to Zeek. In `ssl.log`, Connection 2 had a record, but in `x509.log`, there was nothing. The document did not exist.

I sat back from my desk, my pulse picking up.

“Dana,” I called over. “Something went wrong on the second file transfer. The server stopped sending its certificate.”

Dana didn’t leave her seat. She turned her head slightly. “Did the connection terminate?”

“No,” I said, pointing at the screen. “The TCP connection established, exchanged several kilobytes of data, and closed cleanly. But the server certificate is missing from the wire. Either the host bypassed authentication entirely, or someone is tunneling uninspected traffic over port 443.”

A dry voice spoke from the aisle behind me.

“Or Leah’s server negotiated TLS 1.3, and the wire did exactly what the standard told it to do.”

I turned around. Cal Rowan, our telemetry and detection lead, was leaning against the partition, holding a fresh mug of black coffee. He glanced at my monitors, then looked at Dana.

“Is he trying to hunt covert channels in the morning lab traffic again?” Cal asked.

“He is discovering that protocols evolve without consulting our alert rules,” Dana said mildly.

Cal pulled a rolling stool over to my desk and sat down. “Show me the `ServerHello` for Connection 2.”

I clicked on Frame 23 in Wireshark and expanded the TLS record layer.

“Look at the version field,” I said, pointing to the hex display. “The record layer says TLS 1.2, version `0x0303`. The handshake layer also says TLS 1.2, version `0x0303`. It’s claiming to be TLS 1.2, but the certificate frame is missing.”

Cal took a slow sip of coffee and shook his head.

“You’re reading the legacy version field,” Cal said. “When the TLS working group drafted version 1.3, they discovered that thousands of broken firewalls and middleboxes across the Internet were programmed to drop any packet with a `[[version_freeze|version number higher than 0x0303]]`. If they had stamped `0x0304` into that header, half the corporate networks in the world would have severed the connections on sight.”

He pointed his pen toward the bottom of the `ClientHello` packet detail tree.

“To keep legacy equipment from panicking, TLS 1.3 freezes the outer version field at TLS 1.2. If you want to know what version was actually negotiated, you have to scroll down past the ciphers to the extensions. Look for the [[tls_supported_versions|`supported_versions` extension]].”

I scrolled down through the extension list in Frame 21. There it was: Extension 43, `supported_versions`. Inside, the client had listed `0x0304`—TLS 1.3.

I checked Frame 23, the server’s response. In its own extensions list, the server had returned Extension 43 with a single value: `0x0304`.

“The server accepted TLS 1.3,” I realized.

“Right,” Cal said. “And in TLS 1.3, cryptographic key derivation happens immediately after the `ServerHello`. Everything that follows—the server’s encrypted extensions, its identity, its certificate, its handshake verification—is encapsulated inside encrypted records. To a network sensor sitting on the wire, the server certificate doesn’t look like a certificate anymore. It looks like random binary noise. It looks like `[[content_type_23|Type 23 application data]]`.”

I looked from the Wireshark screen back to our terminal.

“So the certificate wasn’t skipped,” I said. “It was encrypted.”

“Exactly,” Cal said. “Leah’s server sent the exact same self-signed staging certificate it sent in Connection 1. But in Connection 1, it arrived in cleartext, so Zeek extracted the fields and wrote them into `x509.log`. In Connection 2, Zeek saw only encrypted bytes. It couldn’t parse the certificate because it couldn’t decrypt the session.”

I felt a cold sensation in my stomach.

“If the certificate is encrypted,” I said, “how do we know whether the server presented the right identity? What if an attacker stood in the middle and presented a spoofed certificate?”

“From this packet capture alone?” Cal asked. “You don’t. You can’t.”

Before I could answer, Leah Moreno walked past our row carrying a sheaf of inventory printouts. Hearing her name, she paused and leaned over my monitor.

“Are you two diagnosing my staging syncs?” Leah asked.

“Ethan is trying to figure out if your file transfer was compromised,” Cal told her.

Leah looked amused. “It wasn’t compromised. That was our planned integration run for HarrowSync. Workstation `192.0.2.10` initiated an authenticated sync session to `files.harrowmere-group.example` using the new client build. It verified the server’s public key against its local trust store, downloaded two inventory manifests, and disconnected. The entire run completed in four seconds with zero errors.”

I looked at Leah, then down at my notes. “So it was an authorized workflow.”

“It was,” Leah affirmed. “I can show you the application audit log on the server if you need to verify the job ID.”

“Wait,” Dana intervened from across the desk. She stood up and walked over, her eyes fixed on my notepad.

“Leah just gave you an explanation,” Dana said to me. “She told you what the application intended to do, and she told you what the workflow recorded on the host. But what did your network evidence actually prove?”

I looked back at my screens. “Well, the destination IP matches her server. The SNI matches her server name. The port is 443. And the connection happened during her test window.”

“Does any of that prove that Leah’s script was the software running on the client?” Dana asked.

I stopped.

“No,” I said slowly. “Any process on that workstation could have opened a socket to `198.51.100.30`.”

“Does the SNI string in the `ClientHello` prove that the client only requested files from Leah’s approved service?”

“No,” I admitted. “The SNI is sent by the client before encryption begins. It tells the server which certificate to offer, but once the encrypted tunnel is established, an HTTP client could request any path or resource it wanted.”

“And does the presence of encryption prove that the data inside was benign?”

“No.”

“And does the absence of a visible certificate in `x509.log` prove that an attack took place?”

“No,” I said, thinking of Cal’s explanation. “It only proves that TLS 1.3 was negotiated.”

Dana rested her hand on the back of my chair.

“When you analyze encrypted traffic, you will always be tempted by two opposite errors,” she said. “The first error is despair: assuming that because the payload is encrypted, the network is completely blind and you know nothing. The second error is complacency: assuming that because the port is 443 and the handshake looks tidy, the activity must be legitimate.”

She tapped the paper beside my keyboard.

“An analyst does not swing between panic and blind trust. An analyst draws boundaries. When you look at an encrypted session, your job is to separate three distinct categories: what is directly observable, what is reasonably inferable from context, and what cannot be determined without another source.”

Cal nodded in agreement. He pointed at the terminal where our Security Onion dashboard was running.

“Here’s another boundary you’d better learn early,” Cal said. “Zeek writes an internal field in its raw `ssl.log` called `sni_matches_cert`. In TLS 1.2, it checks whether the requested hostname matches the certificate common name and sets the field to true or false. It’s a handy shortcut.”

“Can we alert on that field?” I asked.

Cal smiled faintly. “Security Onion’s `[[dropped_pipeline_fields|ingest pipeline drops that field]]` before indexing. It never gets written to Elasticsearch. If you build a detection that relies on `sni_matches_cert`, your query will return zero results forever, not because the traffic didn't have it, but because the pipeline threw it away.”

He tapped the screen. “Never confuse what the tool pipeline happens to store with what the network actually carried.”

I took a clean sheet of paper and divided it into `[[bounded_claim|three columns]]`.

In the first column—*Directly Observable*—I wrote:
- Client IP `192.0.2.10` contacted Server IP `198.51.100.30` on TCP port 443.
- Handshake negotiated TLS 1.3 via the `supported_versions` extension using cipher suite `0x1302`.
- Client presented cleartext Server Name Indication for `files.harrowmere-group.example`.
- Connection lasted 4.09 seconds and transferred 1,280 client bytes and 4,820 server bytes.

In the second column—*Inferable from Context*—I wrote:
- Timing and endpoint match Leah Moreno’s scheduled HarrowSync integration test.
- Packet byte counts and duration are consistent with a small manifest download rather than large bulk data exfiltration.

In the third column—*Cannot Determine from Network Evidence*—I wrote:
- Identity of the executing client process or user account on `192.0.2.10`.
- Specific HTTP request URIs, query parameters, or response payloads transmitted inside the TLS tunnel.
- Validity of the server certificate presented inside the encrypted TLS 1.3 session.
- Whether the data transferred was authorized under corporate policy.

I looked at the third column. It took up half the page. A week ago, writing down that many unanswered questions would have felt like an admission of failure.

I turned the page toward Dana.

She read through the three columns without speaking. When she reached the bottom of the page, she looked up at Cal.

“What would be the single most efficient source to resolve the third column?” Dana asked him.

Cal shrugged casually. “Endpoint telemetry from the client host. An audit log from the workstation showing the process ID, the binary hash, and the parent process that opened the socket to port 443. If the executable is Leah’s signed sync binary, the case is closed in thirty seconds.”

Dana turned back to me.

“Add that to your notes,” she instructed. “An analyst who knows what network evidence cannot say also knows exactly which door to knock on next.”

She walked back to her station. Cal pushed his stool back and headed down the aisle toward the engineering pod, leaving me alone with the two captures.

I looked at the opaque Type 23 records on my screen. They were still dark, and the application bytes were still hidden. But they were no longer a threat. They were simply a protocol boundary, clearly marked and understood.

---

### Vocabulary & Concepts

| Term | Desk Translation |
|---|---|
| [Server Name Indication (SNI)](#term-server_name_indication) | An extension in the opening `ClientHello` packet where the client requests the hostname it wants to reach in cleartext, before any encryption keys are established. |
| [supported_versions Extension](#term-tls_supported_versions) | The TLS extension (Extension 43) that communicates the true negotiated TLS version (such as `0x0304` for TLS 1.3), bypassing frozen legacy version fields. |
| [Middlebox](#term-middlebox) | An intermediate network appliance (such as an inspecting proxy, legacy firewall, or traffic shaper) that inspects or manipulates traffic along the network path. |
| [Self-Signed Certificate](#term-self_signed_cert) | A cryptographic public key certificate whose digital signature is generated by its own private key rather than by a recognized, trusted Certificate Authority (CA). |
| [Content Type 23 (Application Data)](#term-content_type_23) | TLS record type that encapsulates all post-ServerHello handshake messages and application payloads in TLS 1.3. |
| [Version 0x0303 Freeze](#term-version_freeze) | The legacy outer record layer version field frozen at TLS 1.2 to prevent middleboxes from dropping connections. |
| [Dropped Pipeline Fields](#term-dropped_pipeline_fields) | Zeek log fields that exist on the sensor but are discarded during ingestion before reaching the SIEM/search index. |
| [3-Column Bounded Claim](#term-bounded_claim) | Method separating what is directly observable, what is inferable, and what cannot be determined without host telemetry. |

<div class="bridge-card">
  <div class="bridge-label">Next Step in Curriculum</div>
  <div class="bridge-title">Lesson 04 — What Encryption Hides</div>
  <p class="bridge-desc">Open <code>04-tls.pcap</code> to inspect the TLS 1.3 handshake, verify the <code>supported_versions</code> extension, compare SNI against certificate SANs, and construct rigorous three-column bounded claims when payloads go dark.</p>
  <a href="#/lessons/04-what-encryption-hides" class="bridge-btn">Open Lesson 04 →</a>
</div>
