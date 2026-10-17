# Names Have Behavior

## At a glance

- **Part of:** [the narrative track](README.md) · read before [Lesson 03](../lessons/03-names-and-expectations.md)
- **Version:** 0.1 — draft
- **Date:** 2026-08-22
- **Time:** about 10 minutes
- **Requires:** nothing. No tooling, capture, or account.
- **Creates the question:** Why does name resolution appear differently across two otherwise identical client interactions?

---

By the end of my first month at Harrowmere Equipment Group, I believed I was finally developing an instinct for network evidence.

I had spent weeks working under Dana Shah’s exacting supervision. I had learned to stop treating ticket descriptions as facts. I had practiced reading packet handshakes from the transport layer up to the application payload. Most importantly, I had begun writing down predictions before inspecting raw captures, forcing myself to commit to what healthy traffic ought to look like before the terminal revealed the outcome.

Because of that practice, I felt confident when Dana handed me two packet captures collected from the second-floor engineering wing.

Both captures recorded workstations connecting to the internal file repository that Leah Moreno’s team maintained, reachable across the corporate network at `files.harrowmere-group.example`. The captures had been taken from the same network access switch during the same ten-minute maintenance window.

On Workstation A, everything lined up with the diagrams I had studied for my certification exams. In the Zeek DNS log (`dns.log`), the client sent a query to the Harrowmere [[dns_resolver|recursive resolver]] on UDP port 53. The resolver answered with a [[cname_record|CNAME record]] pointing to an internal storage cluster, followed by an address record pointing to `10.14.120.15`. Three milliseconds later, the Zeek connection log (`conn.log`) recorded the opening TCP handshake from Workstation A to `10.14.120.15` on port 443, followed by a standard TLS exchange and steady application throughput.

The second capture, taken from Workstation B, looked completely broken to me.

Four seconds into the file, Workstation B initiated a TCP handshake to `10.14.120.15` on port 443. The three-way handshake completed cleanly. The TLS negotiation succeeded. The file transfer proceeded without retransmissions or resets.

However, in the Zeek `dns.log` file for Workstation B, there was nothing. I opened the raw packet capture in Wireshark and filtered specifically for DNS traffic. The display was blank. There was not a single query packet, not a single response frame, and not a single UDP datagram addressed to port 53.

I stared at the screen, comparing the two windows. The conceptual model I had carried from training was clear: before a computer can open a socket to a hostname, it must resolve that hostname to an IP address. Workstation A had followed the rules. Workstation B appeared to have bypassed them entirely.

I pulled out my notebook and drafted a concise three-sentence summary for Dana:

> Workstation A resolved `files.harrowmere-group.example` normally via the corporate resolver before establishing a TLS session. Workstation B bypassed corporate name resolution entirely and connected directly to the destination IP address. This suggests manual hostfile modification or a hardcoded address in an unauthorized script.

Dana walked past my desk carrying a fresh cup of tea. She stopped, glanced down at the open terminals, and then read the lines on my pad.

“You’ve made an accusation,” she said calmly.

“I made an observation,” I replied. “Workstation B didn’t do DNS.”

“Show me where the capture says that.”

I gestured toward the blank Wireshark screen. “Right there. Zeek recorded zero queries in `dns.log`. Wireshark shows zero packets on UDP port 53. If the machine never queried the resolver, it didn’t resolve the name.”

Dana did not argue with me. Instead, she turned toward the row of desks behind us.

“Priya,” Dana called across the low partition. “Do you have three minutes?”

Priya Raman, Harrowmere’s Senior Network Engineer, turned around in her task chair. Her desk was flanked by two widescreen monitors displaying real-time interface telemetry and routing topologies. She had been with Harrowmere long enough to have designed much of the core infrastructure herself.

“What do you have?” Priya asked, rolling her chair over to my station.

“Ethan has found a workstation that he believes is evading company policy,” Dana said, stepping back just far enough to leave Priya and me looking at the display.

Priya looked at the two terminal windows. “Walk me through the evidence, Ethan.”

I felt a sudden tightness in my chest. Dana was intimidating because she questioned my logic, but Priya was intimidating because she actually owned the physical wires and switches.

“Workstation A and Workstation B are on the same subnet,” I began, pointing to their source addresses. “Both are reaching Leah’s file service at `files.harrowmere-group.example`. Workstation A performs a standard lookup against our resolver at `10.14.10.5`. It gets back the CNAME and the A record, and then it initiates the TCP connection. Workstation B makes the exact same TCP connection to `10.14.120.15`, but there is no DNS lookup anywhere in the capture. It skipped resolution.”

Priya did not nod or shake her head. Instead, she reached into her pocket, pulled out a pair of reading glasses, and leaned in toward my keyboard.

“Where was this capture taken?” she asked.

“From the span port on the access switch for engineering,” I said.

“And what is the duration of the capture file?”

“Five minutes.”

Priya looked at the secondary monitor where I had Wireshark open, then reached over to her own laptop on the mobile cart beside her. I expected her to deliver an immediate technical verdict based on memory. Instead, she opened an engineering repository, navigated to the VLAN mapping documentation, and verified the DHCP lease configurations for the engineering pool.

I watched her check the documentation. It was a subtle action, but it struck me immediately. I had assumed senior engineers possessed an encyclopedic mental catalog of every port, lease, and server address across the entire company. Seeing Priya verify the authoritative records before speaking made me realize that technical expertise was not about memorizing the state of every switch; it was about knowing which records to verify before drawing a conclusion.

“What does an operating system do when an application asks for a hostname?” Priya asked, turning back to me.

“It queries the resolver,” I answered.

“Does it query the resolver immediately, every single time?”

I hesitated. A half-remembered paragraph from an operating systems manual flickered through my mind.

“No,” I said slowly. “It checks its local [[dns_cache|DNS cache]] first.”

“Exactly,” Priya said. Her tone was patient and unhurried. “If an operating system already has a valid address mapped to that name in memory, it doesn’t need to ask the network. It uses the answer it already has.”

She pointed at the terminal displaying Workstation A’s DNS answer.

“Look at the answer record returned to Workstation A,” Priya said. “What is the value in the TTL field?”

I looked at the record in Zeek’s `dns.log`. Next to the resolved address `10.14.120.15`, the output displayed a numeric value: `300`.

“It says three hundred,” I replied.

“Three hundred seconds,” Priya explained. “That is the [[dns_ttl|TTL (Time to Live)]] assigned by the authoritative zone. It tells every client and resolver that once they receive this answer, they are permitted to cache and reuse it for five minutes without asking again.”

She turned her attention back to the capture from Workstation B.

“Now,” Priya continued, “suppose the user at Workstation B opened a document from Leah’s file share four minutes before your capture started. What happened on the network during that earlier exchange?”

“Workstation B would have queried the recursive resolver,” I said, the pieces beginning to connect.

“Right. And the operating system would have received the answer with a five-minute TTL and stored it in its local cache. Four minutes later, your five-minute packet capture begins. Workstation B initiates another file transfer. The application asks the operating system to resolve `files.harrowmere-group.example`. The operating system inspects its memory, sees that the cached record still has sixty seconds of valid life remaining, and hands the IP address straight to the application socket.”

Priya straightened up and gestured to my blank Wireshark filter.

“Did a packet ever touch the physical network interface for that second lookup?”

“No,” I admitted. “The operating system resolved it internally.”

“So the client did perform name resolution,” Priya said. “It just didn’t perform a *visible network transaction* during your five-minute capture window. The absence of evidence on your switch port was not evidence of a policy bypass. It was the expected consequence of standard client caching.”

The room felt very quiet for a moment. I looked down at the three accusatory sentences in my notebook. They were entirely wrong, not because the packets had lied to me, but because I had equated what was visible on the wire with what had occurred inside the system.

Dana stepped back into view, resting her hands on the back of my chair.

“What did you actually observe, Ethan?” Dana asked again.

I picked up my pen, crossed out the paragraph I had written, and drafted a new statement:

> Over a five-minute capture window, Workstation B established a TCP connection to `10.14.120.15` without an observable DNS query on the local access segment. This observation is consistent with the client utilizing a previously cached DNS response within its valid Time to Live window, though a pre-capture query cannot be confirmed from this vantage alone.

I turned the notepad toward Dana. She read the revision carefully, then looked over at Priya.

“That’s an analyst’s statement,” Priya said with a brief, approving smile. “It describes what the vantage point captured without pretending to know what happened before the capture started.”

“Remember this when you start Lesson 03,” Dana added, turning back toward her desk. “DNS is not a static directory lookup that happens once and disappears. Names have lifecycles. They have durations, aliases, and memory. If you assume that every conceptual step must leave a visible footprint on the wire at the exact moment you happen to be watching, you will spend half your career investigating ghosts.”

Priya wheeled her chair back toward the network engineering pod, leaving me alone with the two captures.

I looked at the blank Wireshark screen one more time. It was no longer a mystery or a failure. It was simply the boundary of what that specific wire was capable of showing me.

---

### Vocabulary & Concepts

| Term | Desk Translation |
|---|---|
| [Recursive DNS Resolver](#term-dns_resolver) | A DNS server that accepts queries from clients and queries authoritative nameservers recursively to find the IP address. |
| [CNAME Record](#term-cname_record) | A Canonical Name DNS record that maps an alias hostname to another true domain name in a lookup chain. |
| [DNS TTL (Time to Live)](#term-dns_ttl) | A 32-bit field in a DNS resource record defining how many seconds a client or resolver may cache the answer. |
| [DNS Cache](#term-dns_cache) | Temporary local memory where an operating system or browser stores recent DNS answers to avoid repeat queries. |

---

**What happens next.** [Lesson 03 — Names and Expectations](../lessons/03-names-and-expectations.md) explores how DNS records change over time, how Time to Live values govern client behavior, and why healthy name resolution routinely produces answers that look contradictory if you do not understand how names behave.
