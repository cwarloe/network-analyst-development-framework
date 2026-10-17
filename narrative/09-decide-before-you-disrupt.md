# Decide Before You Disrupt

## At a glance

- **Part of:** [the narrative track](README.md) · read before [Lesson 09 Capstone: Encrypted Outbound Traffic](../lessons/09-capstone-encrypted-outbound-traffic/README.md)
- **Version:** 0.1 — draft
- **Date:** 2026-08-22
- **Time:** about 15 minutes
- **Requires:** nothing. No tooling, capture, or account.
- **Creates the question:** When an initially reasonable benign model is contradicted by new evidence during an active incident, how does an analyst visibly revise under operational pressure?

---

By the end of my fifth month at Harrowmere Equipment Group, I was no longer treated as the new junior who needed his terminal watched.

I had earned a quiet measure of autonomy. When a complex ticket arrived, Dana Shah no longer assigned herself as primary. Owen Kline would occasionally ask me to verify an anomalous TCP sequence on a trunk link. Priya Raman would pull me into switch port reviews, and Leah Moreno trusted my reports enough to adjust backend database queries without demanding a second opinion.

I felt comfortable. And in security operations, feeling comfortable is often the precursor to being humbled.

The incident began on a Friday afternoon, thirty minutes after a scheduled software deployment.

Harrowmere’s IT systems team had just rolled out a maintenance update to the fleet of engineering workstations, updating our internal client libraries and synchronizing package dependencies with Leah Moreno's HarrowSync application infrastructure.

At 15:42 UTC, an automated detection fired in the SOC console:
*Workstation `192.0.2.10`—an engineering desktop assigned to developer Marcus Vance—had established persistent, high-frequency encrypted outbound connections to an external destination, `198.51.100.24`, over TCP port 443.*

Nia Alvarez called an immediate stand-up at the operations desk.

“Marcus Vance is working on the next-generation machine controller firmware,” Nia said, her voice sharp. “If that workstation is exfiltrating proprietary design files, we have a major intellectual property breach. But if we sever his network connection mid-compile, we wipe out two days of uncommitted engineering builds. What does the network evidence say?”

I opened the evidence packet on my console.

Dana Shah stood at the far end of the row, leaning against the filing cabinet. She didn't come to my desk. She didn't look over my shoulder. She picked up a binder and began reading, leaving the entire incident floor between us.

I looked at the telemetry from `192.0.2.10`:
1. The workstation was connecting to `198.51.100.24` every 4.2 seconds with under 2% timing variation.
2. The TLS handshake negotiated TLS 1.3 using cipher suite `0x1302` (`TLS_AES_256_GCM_SHA384`).
3. The Server Name Indication in the `ClientHello` requested `sync-telemetry.harrowmere-cloud.example`.
4. Over forty minutes, the session had transferred a modest 48 kilobytes of client data and received 12 kilobytes of server responses.
5. The connection began at 15:14 UTC—precisely four minutes after the scheduled software update package finished installing on Marcus's machine.

Every instinct I had developed over the last five months pointed toward an authorized workflow.

“The timing aligns directly with the post-update reboot,” I told Nia and the gathered team. “The SNI belongs to our own cloud namespace—`sync-telemetry.harrowmere-cloud.example`. The data volume is under fifty kilobytes, which is entirely consistent with an update agent performing a license check or telemetry sync. I assess with **high confidence** that this is an authorized background telemetry service initiated by the new update package.”

Nia nodded, her hand resting on the network isolation button. “Can we let it continue while Marcus finishes his compile?”

“Yes,” I said. “The risk is low, and the behavior is expected after a package update.”

Nia stepped back from the console. “Okay. Staged operation permitted. Owen, keep an eye on bandwidth.”

I turned back to my terminal, feeling a surge of satisfaction. I had made a clear call, sized to the evidence, and prevented an unnecessary operational disruption.

Then Cal Rowan pulled up a chair beside my workstation.

“Ethan,” Cal said quietly. “Where does Harrowmere host its external cloud telemetry?”

“On AWS in the US-West region,” I answered, reciting the architecture spec Priya had shared weeks ago.

Cal pointed his stylus at the destination IP: `198.51.100.24`.

“That IP block isn't Amazon Web Services,” Cal said. “That netblock belongs to a budget hosting provider registered in Eastern Europe. We don't have any corporate infrastructure hosted in that autonomous system.”

The satisfaction drained out of me instantly.

I pulled up the registration data. Cal was right. The IP address had no connection to our cloud provider.

“Wait,” I said, my voice dropping. “The SNI said `sync-telemetry.harrowmere-cloud.example`. Why would a server in that hosting block answer to our corporate domain?”

“Anyone can send an SNI string requesting any domain they want,” Cal reminded me gently. “Remember Lesson 04? SNI is transmitted in the clear by the client before encryption begins. An adversary's implant can put whatever string it wants into the `ClientHello` to make the connection look like an authorized company service.”

My heart began to hammer against my ribs. 

I had just told the Security Operations Manager that this connection was safe. Nia had based an operational decision on my assessment.

I looked across the room. Dana was still reading her binder. She had seen Cal walk over, but she had not moved. She was not going to step in.

Leah Moreno rushed over from the application wing, holding a printed manifest.

“Ethan, I just checked the software update package we deployed at 15:10,” Leah said, breathing heavily. “Marcus’s machine pulled the update from our internal repository, but the SHA-256 hash on the installed sync binary doesn’t match our signed release build. The binary on Marcus's machine has an extra 42-kilobyte compiled module injected into the runtime directory.”

The room seemed to shrink.

The initial model had completely collapsed. The destination was unverified. The SNI was a decoy. The binary was tampered with. The modest 48-kilobyte transfer wasn't a benign health check; it was a staged [[staged_c2_channel|command-and-control channel]] establishing persistence.

I sat frozen for three seconds. 

The most dangerous impulse in security analysis flashed through my mind: *I already told Nia this was fine. If I change my mind now, I'll look incompetent. Maybe I should wait another twenty minutes for more packet data.*

Then I remembered Dana’s voice from my very first week: *“A mentor who is never wrong teaches that experts are oracles. An analyst who cannot revise in front of their team is dangerous.”*

I pushed my chair back, stood up, and walked straight to Nia’s desk.

“Nia,” I said clearly, loud enough for the operations room to hear. “I need to formally revise my assessment.”

Nia looked up from her screen, her expression instantly alert. “What changed?”

“My earlier assessment that this traffic was an authorized telemetry check has failed,” I stated, keeping my voice level and controlled. “Cal verified that the destination IP belongs to an unauthorized overseas hosting provider, not our corporate cloud. Leah confirmed that the client binary on `192.0.2.10` does not match our signed release hash. The `sync-telemetry` SNI string was used as a decoy to mimic legitimate infrastructure.”

Nia’s eyes narrowed. “What is the revised claim?”

“We have **high confidence** that Workstation `192.0.2.10` is compromised by an unauthorized implant injected during or immediately following the 15:10 update window,” I answered. “The leading explanation is a software supply-chain or repository tampering event. The [[immediate_containment|immediate containment action]] is to sever `192.0.2.10` from the network now.”

“What about Marcus’s uncommitted compile?” Nia asked.

“The risk of code loss is outweighed by the risk of an active persistent channel into our engineering subnet,” I replied without hesitation. “Isolate the machine from the network, but do not reboot or reimage it. We need the volatile RAM intact so Incident Response can dump the unencrypted process memory and recover Marcus’s work.”

Nia hit the network isolation trigger on her console.

“Host isolated,” Nia confirmed. “Owen, block `198.51.100.24` at the perimeter firewalls. Leah, lock the software update repository and halt the deployment pipeline across the rest of the company. Cal, pull the memory dump from Marcus’s desktop.”

The SOC erupted into disciplined, rapid response.

I stood by the operations desk, my hands trembling slightly from the rush of adrenaline, but my head clear. I had made an incorrect initial call. But I had not clung to it, I had not hidden the evidence, and I had corrected the course before damage occurred.

A hand rested on my shoulder.

I turned around. Dana was standing beside me. She closed her binder and looked at me with a steady, quiet pride that I had never seen from her before.

“You didn’t defend the mistake,” Dana said.

“I was wrong about the SNI,” I said.

“You formed a reasonable hypothesis from the initial evidence, named your assumptions, and when contradictory evidence arrived, you reversed out loud without flinching,” Dana said. “That is what separates an analyst from someone who merely operates software.”

She nodded toward the whiteboards where the incident response team was mapping the supply-chain investigation.

“You don’t need me to look over your shoulder anymore, Ethan,” Dana said quietly. “You’re ready for the Capstone.”

She turned and walked back toward the engineering pod, leaving me at the center of the floor.

Across the room, the monitors were still active, the alerts were still tracking, and the incident was only beginning. But I was no longer afraid of the dark. I had learned to see.

---

### Vocabulary & Concepts

| Concept / Identifier | Desk Translation |
|---|---|
| [[staged_c2_channel|staged C2 channel]] | A multi-phase command-and-control connection where initial check-ins use legitimate-looking domain names or small payloads to test egress filtering before escalating to active exfiltration. |
| [[immediate_containment|immediate containment]] | The rapid network isolation of an endpoint to sever active adversary communication while preserving volatile system memory (RAM) for forensic investigation. |
| [[model_revision|model revision out loud]] | The professional capability of an analyst to explicitly and publicly abandon a previous analytical hypothesis when new contradictory evidence invalidates its baseline assumptions. |
| [[decoy_sni|decoy SNI]] | The adversary practice of crafting cleartext Server Name Indication fields in a `ClientHello` that spoof trusted corporate or vendor hostnames to blend into ordinary egress monitoring. |

---

**What happens next.** [Lesson 09 — Encrypted Outbound Traffic Capstone](../lessons/09-capstone-encrypted-outbound-traffic/README.md) puts you in the analyst's seat for this full performance: analyzing initial encrypted outbound packets, committing to an initial assessment, receiving contradictory endpoint and network telemetry, and executing a defensible model revision under operational pressure.
