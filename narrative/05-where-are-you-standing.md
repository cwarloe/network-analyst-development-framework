# Where Are You Standing?

## At a glance

- **Part of:** [the narrative track](README.md) · read before [Lesson 05](../lessons/05-vantage-point-and-evidence.md)
- **Version:** 0.1 — draft
- **Date:** 2026-08-22
- **Time:** about 12 minutes
- **Requires:** nothing. No tooling, capture, or account.
- **Creates the question:** When multiple reputable telemetry sources provide conflicting accounts of the same event, how does sensor vantage reconcile the contradiction?

---

By the beginning of my third month at Harrowmere Equipment Group, I had convinced myself that adding more data sources was the cure for ambiguity.

If a single log left a question unanswered, two logs would corroborate each other. If two logs left a seam of doubt, pulling packet captures, firewall session tables, and endpoint event streams would triangulate the truth until only one conclusion remained. More telemetry, I assumed, equaled more clarity.

That assumption survived until Tuesday morning, when Dana handed me an escalation regarding our primary finance file server, `FS-FIN-01`.

The ticket had originated from an internal operations review. An automated script monitoring high-volume egress had flagged an apparent external file transfer from `FS-FIN-01` to an unclassified external IP address, `198.51.100.99`, occurring at 02:14 UTC over the weekend. 

I arranged four telemetry dashboards across my screens:
1. Screen 1 displayed our edge flow telemetry, configured for [[netflow_sampling|sampled NetFlow]] at a 1:100 packet ratio with 90-day retention.
2. Screen 2 showed Zeek connection logs from our perimeter network sensor, capturing unsampled connection metadata with 30-day retention.
3. Screen 3 held our perimeter firewall logs, recording connection decisions and translated NAT sessions.
4. Screen 4 showed the application log export provided by Leah Moreno’s team for the finance file service.

I spent forty-five minutes querying the timestamps. By the end of the hour, I had four separate accounts of the exact same thirty-second window, and they appeared to directly contradict one another.

Screen 1—the sampled flow collector—reported an outbound transfer of approximately 140 megabytes to `198.51.100.99`.
Screen 2—the perimeter Zeek sensor—showed three completed connections to that external IP, but recorded a total of only 42 kilobytes transferred.
Screen 3—the edge firewall—showed no outbound sessions to `198.51.100.99` originating from `FS-FIN-01`’s internal IP address at all.
Screen 4—the file service application log—recorded a status message stating: *“Backup synchronization completed successfully; 142 MB transferred.”*

I stared at the monitors, my jaw clenched. Either our firewall was dropping logs, our flow collector was hallucinating gigabytes of traffic, or our packet sensors were blind.

“Dana,” I said, unable to hide the irritation in my voice. “These sources don't match. Three of them are lying, or one of them is completely broken.”

Dana didn’t look up from her review queue. She simply turned her chair toward the engineering aisle.

“Priya,” Dana called out. “Cal. When you have a moment, Ethan has discovered that our sensors don’t agree.”

Priya Raman walked over first, holding a freshly printed network topology diagram. Cal Rowan followed shortly after, dragging his favorite rolling stool behind him.

“Which sensors are offending you today?” Cal asked, settling in beside my desk.

“All of them,” I said, pointing across the four monitors. “The application log and NetFlow say 140 megabytes left the finance server for an external host. Zeek says only 42 kilobytes left. And the firewall says `FS-FIN-01` never initiated an outbound connection to that destination during the entire two-hour maintenance window. How can four enterprise monitoring tools see the exact same machine at 02:14 UTC and give four completely irreconcilable numbers?”

Cal chuckled quietly. Priya stepped forward, her expression thoughtful and disciplined.

“Before you accuse the tools of lying, Ethan,” Priya said, “tell me where each sensor is standing relative to the traffic path.”

I hesitated. I had looked at IP addresses, port numbers, and byte counters. I had not looked at the physical topology.

“The NetFlow collector receives flow exports from the core routing switch,” I said, tracing the topology in my head. “Zeek sits on a passive network tap on the edge DMZ link. The firewall is the boundary between the internal transit subnet and the external upstream provider.”

“And where does the finance file server live?” Priya asked, tapping the diagram in her hands.

“In the internal datacenter VLAN,” I answered.

“Good,” Priya said. “Now, when `FS-FIN-01` transmits a backup payload to an external staging destination, does it route directly across the edge DMZ?”

I looked at the diagram. A dotted line ran from the datacenter subnet, through an internal load balancer, and into a secure VPN concentrator.

“No,” I realized, the realization beginning to dawn. “Outbound backup transfers are tunneled through the [[vpn_hairpin|corporate VPN gateway]] to our offsite storage provider.”

“Right,” Priya explained. “The server establishes an IPsec tunnel to the backup vault. To the core routing switch, every packet between `FS-FIN-01` and the internal VPN gateway is visible in the clear before encapsulation—142 megabytes of raw file data. That is what your core switch exported to NetFlow.”

“Then what did Zeek see on the DMZ tap?” I asked.

Cal pointed to Screen 2. “Look at the destination port on those three Zeek connections. What port did you query?”

I checked the filter syntax: `destination.port: 443`.

“You filtered for HTTPS,” Cal said. “At 02:14 UTC, `FS-FIN-01` sent three small API health checks over HTTPS to the backup provider's management plane to verify authentication tokens. That transfer was 42 kilobytes. The actual 140-megabyte data payload didn’t travel over HTTPS; it traveled inside an encrypted IPsec tunnel on UDP port 4500. Because your Zeek query only searched for port 443, you filtered out the actual data transfer yourself.”

I swallowed hard. I looked over at Screen 3.

“What about the firewall?” I asked. “Why didn't the firewall show connections from `FS-FIN-01`?”

“Because `FS-FIN-01` is on a private RFC 1918 subnet,” Priya answered patiently. “When the VPN gateway routes outbound packets through the edge firewall to the Internet, it performs source network address translation. The firewall didn’t record `FS-FIN-01` because the packet header no longer carried that internal address. It recorded the public IP of our edge gateway interface. The traffic was right there in your firewall logs; you just queried the wrong source IP.”

The four monitors suddenly seemed to align, shifting from chaos into a coherent, layered system. The tools hadn't contradicted one another. Each sensor had reported the literal truth of what passed its physical interface under its specific configuration.

“So every source was accurate,” I said quietly.

“Within its observation boundary, yes,” Cal said. “A sensor is not an omniscient narrator. A sensor is a situated observer. It records what crosses its physical vantage point, after that traffic has been shaped, translated, filtered, or encapsulated by every network device that came before it.”

Dana stood up and stepped beside the desk, holding a dry-erase marker. She walked to the whiteboard on the partition wall and drew three horizontal lines, creating a structured table.

“Every time you open an investigation,” Dana said, “your first impulse is to ask: *What does this source say?* That is the novice’s question.”

She capped the marker and looked at me.

“What is the analyst’s question?”

I thought about what Priya and Cal had just demonstrated.

“The analyst’s question is: *Could this source have observed the thing I am asking about in the first place?*”

“Exactly,” Dana said. “If a sensor could not have observed the event—because of placement, translation, encapsulation, or logging configuration—its silence carries zero evidential weight. Writing *‘the firewall showed no traffic, therefore no connection occurred’* is not analysis. It is an assumption disguised as evidence.”

She drew four columns on the whiteboard: *Source*, *Vantage Point*, *Can Establish*, and *Blind Spots*.

“Let’s look at your four screens again,” Dana instructed. “Cal, walk him through retention.”

Cal leaned back on his stool. “Suppose this backup failure had happened four days ago instead of this morning. Which of your four screens would still be usable?”

I pointed at Screen 1 and Screen 2. “NetFlow retains 90 days. Zeek retains 30 days.”

“And full packet capture?” Cal pressed. “Suppose you wanted the raw payload bytes from that DMZ link?”

“Our [[rolling_pcap_buffer|rolling packet capture buffer]] on the DMZ only keeps 36 hours of continuous data,” I answered, recalling our storage limits. “Past 36 hours, the ring buffer overwrites the oldest files. If we don’t pull the capture immediately, the raw packets are gone permanently.”

“Right,” Cal said. “Retention runs a clock you do not control. And the clock is usually inverted against fidelity: the highest-detail evidence dies first. If you spend three days checking 90-day NetFlow logs before you decide whether you need full packet capture, the buffer has rolled over and your highest-fidelity evidence no longer exists.”

Leah Moreno walked over from the breakroom holding a notebook. Hearing the discussion, she leaned against my cubicle wall.

“Did you sort out the 02:14 backup run?” Leah asked.

“We did,” I said. “The core switch saw the raw backup payload, the DMZ saw the HTTPS management checks, and the edge firewall saw the NATed VPN tunnel.”

“And what about the application log?” Leah asked with a knowing smile. “Did you believe my log when it said *‘backup completed successfully’*?”

I hesitated. “Well, the NetFlow byte counts match your 140 megabytes. Doesn't that confirm it succeeded?”

“It confirms the file server transmitted 140 megabytes into the network socket,” Leah pointed out. “It does not prove the remote destination successfully committed those blocks to disk. On the application side, *‘success’* in that log line only meant the local client process finished reading the spool file and flushed its transmit buffer without catching an OS exception. To verify whether the destination vault actually accepted the archive, you need the remote vault’s receipt log.”

I let out a long breath. Every single source had an edge. Every single source had a frame beyond which it could not speak.

“So how do we decide which source to trust first?” I asked.

Dana wiped a section of the whiteboard clean.

“You don’t rank sources by which one is ‘best,’” Dana said. “You rank them by constructing a [[discriminating_pair|discriminating inquiry]]. You identify two competing explanations, ask which source can physically observe the difference between them, and collect against the shortest retention clock first.”

She pointed to my notepad.

“Write this down in your case notes before you touch Lesson 05: A log is not reality. A log is a partial projection of reality, recorded from a specific physical vantage point, through a specific configuration, over a finite retention window. If you do not know where your sensor was standing, you do not know what its silence means.”

I picked up my pen and wrote the rule at the top of a clean page.

Across my desk, the four monitors still displayed four different numbers. But they were no longer arguing with each other. They were simply telling their parts of the story, each waiting for an analyst who knew how to listen.

---

### Vocabulary & Concepts

| Term | Desk Translation |
|---|---|
| [Sampled NetFlow](#term-netflow_sampling) | A network telemetry protocol that exports flow summaries rather than packet payloads, often sampled at a fixed ratio (such as 1 out of every 100 packets) to reduce storage and processing overhead. |
| [Corporate VPN Gateway](#term-vpn_hairpin) | A network infrastructure boundary where traffic enters an encrypted tunnel, often undergoing address translation, encapsulation, or re-routing before exiting to external networks. |
| [Rolling Packet Capture Buffer](#term-rolling_pcap_buffer) | A finite storage disk array configured as a FIFO (First-In, First-Out) ring buffer that continuously captures raw packet bytes until disk capacity forces overwriting the oldest captures. |
| [Discriminating Inquiry](#term-discriminating_pair) | An analytical strategy that identifies a specific observation that must be present under one hypothesis and absent under another, allowing an analyst to decisively separate competing explanations. |

<div class="bridge-card">
  <div class="bridge-label">Next Step in Curriculum</div>
  <div class="bridge-title">Lesson 05 — Vantage Point and Evidence</div>
  <p class="bridge-desc">Put multi-vantage architectural reasoning into practice. Work out what a sensor can and cannot attribute across VPN hairpins, prioritize evidence collection against the perishability clock, and construct defensible evidence plans.</p>
  <a href="#/lessons/05-vantage-point-and-evidence" class="bridge-btn">Open Lesson 05 →</a>
</div>
