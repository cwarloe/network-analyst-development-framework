# Prologue — The Word in the Ticket

## At a glance

- **Part of:** [the narrative track](README.md) · read before [lesson 01](../lessons/01-what-the-analyst-is-for.md)
- **Version:** 0.1 — draft
- **Date:** 2026-08-20
- **Time:** about 10 minutes
- **Requires:** nothing. No tooling, no capture, no account.
- **Teaches:** nothing directly. It asks the question [lesson 01](../lessons/01-what-the-analyst-is-for.md) answers.

> Every number in this chapter is real, read out of [`assets/pcaps/02-conversation.pcap`](../assets/pcaps/02-conversation.pcap), which you will open yourself in [lesson 02](../lessons/02-reading-a-conversation.md). Nothing here is invented for effect.

---

I had been at Harrowmere eleven days when Dana let me take a ticket.

I want to be honest about what I thought the job was. I thought it was recognizing bad things. I had spent two years on a service desk in Portland resetting passwords and unsticking printers, and I had studied for this on my own time, and what I had studied was lists — ports, protocols, attack names, the shapes of things that were bad. I thought analysis was pattern-matching with a better vocabulary. I thought the people who were good at it had simply memorized more.

The ticket said:

<div class="artifact">
  <div class="ticket-chrome">
    <div class="ticket-bar">
      <span class="ticket-id">SEC-4021</span>
      <span class="sev high">High</span>
      <span class="ticket-status">Assigned: Ethan Vance</span>
    </div>
    <div class="ticket-subject">Possible unauthorized access attempt — internal file service</div>
    <dl class="ticket-meta">
      <div><dt>Source Host</dt><dd>192.0.2.10 (Finance Subnet)</dd></div>
      <div><dt>Destination Host</dt><dd>198.51.100.20:80 (Reporting Server)</dd></div>
      <div><dt>Detection Rule</dt><dd>SecOnion Perimeter Access #2014902</dd></div>
      <div><dt>Timestamp</dt><dd>2026-08-20 09:14:02 UTC</dd></div>
    </dl>
  </div>
</div>

Underneath were two lines from a [[zeek_conn_log|Zeek connection log (`conn.log`)]], and I understood almost none of it:

<div class="artifact">
  <figcaption>Zeek conn.log Telemetry — Attached to Ticket #SEC-4021</figcaption>
  <pre class="console-body"><span class="cmt"># ts uid id.orig_h id.orig_p id.resp_h id.resp_p proto service duration orig_bytes resp_bytes conn_state history</span>
1755681242.000104 CwlV971jSsZWObrEKd 192.0.2.10 42876 198.51.100.20 80 tcp http 0.004053 151 207 <span class="cmd">SF</span> ShADadfF
1755681242.404288 C1f8K83tA9wX1qLmNp 192.0.2.10 42886 198.51.100.20 80 tcp http <span class="cmd">0.000184</span> 148 182 <span class="cmd">SF</span> ShADaFf</pre>
</div>

I had memorized port numbers on my own time for two years and could not pick them out of a row. There were numbers I took for byte counts, one I took for a duration except it was mostly zeros and I could not think of a unit that made it sensible, and a column called `connection.state` reading `[[conn_state_sf|SF]]` twice, about which I had nothing at all.

Here is what I could actually read: both requests came from the same workstation to the same server, spaced four tenths of a second apart. The first was an HTTP `GET` request to an export [[api_endpoint|API endpoint]], and it returned `[[http_200|200 OK]]` with ninety bytes of [[json_payload|JSON payload]]. The second was an HTTP `GET` request to `/api/v2/admin/users`, and it returned `[[http_403|403 Forbidden]]` with forty-four bytes.

I knew what a `403 Forbidden` status code meant, and I understood what `admin` implied.

I counted twenty-six pieces of information in front of me and built my answer out of the two I recognized, and I felt the small hot satisfaction of knowing something. Somebody had attempted to access an admin API endpoint, and the server had refused them. Because that matched the ticket's title, I assumed I was clearly right.

I went and found Dana at her desk and said, "Someone's probing the admin API."

She didn't answer right away. She has a way of pausing that is neither rude nor warm. She simply looks at you with mild, steady interest, the way you might watch a bird doing something unexpected, and waits.

After about four seconds of that silence, I felt uncomfortable enough to keep talking.

"There is a 403 on `/api/v2/admin/users` coming from a finance workstation, 400 milliseconds after a successful export."

"Those are three things you saw," she said. "What did you think?"

"…That someone's probing the admin API."

"Where did the word *probing* come from?"

I opened my mouth and closed it. I turned back toward my screen. It was not in the log. It was not in either of those two lines. It was in the ticket title, in the phrase *unauthorized access attempt*, and it had been sitting there before I opened the ticket. I had spent four minutes assembling a case for a conclusion that somebody I had never met handed me on the way in.

That is the whole thing. Nobody tells you that on your first day. I want to be clear that I am not describing a mistake I made once and then stopped making. I still catch myself doing it. Everybody does. The difference is that now I go looking for the word.

Dana came over and leaned on the back of my chair.

I told her I hadn't understood most of the columns, and braced for that to turn out to be the real problem.

She looked genuinely unconcerned. "Which ones?"

I listed them. She stopped me about halfway down. "You'll have all of those inside a month, and not one of them is the hard part. The hard part is the thing you just did with the word. I've been doing this for nine years and I still have to watch for it."

She moved on. "All right. Somebody's poking at an admin API endpoint. Who?"

"A user on a finance laptop."

"Show me the user."

I looked back at the log. The record showed source and destination IP addresses, port numbers, how many bytes traveled in each direction, and the total session duration. It did not list a user. There was no username, no person, no process name, and no recorded intent—only two machines exchanging a sequence of bytes.

"It's not in there," I said.

"It's not in there," she agreed. "Keep hold of that. It comes up constantly." She reached past me and put a finger on the column I hadn't been able to make sense of. "This one's seconds. Now — how long did the second one take?"

The value read zero point zero zero zero one eight four. I counted the decimal places twice to be sure. That was one hundred and eighty-four microseconds in the Zeek connection log's `[[duration_microsecond|duration]]` field.

"So," she said, "if that were a human user, they would have had to read the previous page, decide to try an administrative URL, and type it into the browser—all in under a fifth of a millisecond." She stopped herself. "No. That's wrong, what I just said. I was about to walk you into another assumption."

She was quiet for a second, and then: "Look at the [[user_agent_string|HTTP User-Agent string]] on both of them."

Both lines were identical: `harrow-sync/3.21`. The exact same string appeared on the successful export and on the `403 Forbidden` response.

"So this is evidence of a software agent, not evidence of a person," she said. "The matching User-Agent strings make one process or workflow plausible, though they don't prove it. And the first request went to the export endpoint four tenths of a second earlier and was allowed. That points to an entirely different question than the one the ticket asked, and I nearly got it wrong right in front of you. That's the other lesson to keep. I do this for a living and I still catch myself starting from the story I walked in with."

I asked her what it actually was, then. Whether it was bad.

"I don't know," she said. "Neither do you. That's not a failure, it's just where we are." She counted them off on her fingers. "Is that service supposed to call that endpoint? Does it call it every time it syncs, or only today? Do the other finance machines do the same thing at the same time of day? And does anybody own that software well enough to answer?"

"How do I find out?"

"Some of it you can get from the traffic. Some of it you can't get from the traffic at any price, and knowing which is which is most of the job." She straightened up. "Here is what I actually want you to do instead of guessing an answer. Go write down what you *saw*, without using any of the words the ticket handed you. Then, separately, write down what you think those observations might mean. Keep those two things completely apart on the page. Once you have separated them, come find me."

It took me forty minutes and it was the hardest piece of writing I have ever done, and it was six sentences long.

---

### Vocabulary & Concepts

| Term | Desk Translation |
|---|---|
| [Zeek conn.log](#term-zeek_conn_log) | The connection log in Zeek summarizing Layer 3/4 session facts (IPs, ports, protocol, duration, byte counts, and connection state). |
| [API Endpoint](#term-api_endpoint) | A specific URI or path on a web server where client software sends structured requests to consume backend services. |
| [JSON Payload](#term-json_payload) | A lightweight, text-based data format used to structure application responses between web servers and clients. |
| [HTTP User-Agent string](#term-user_agent_string) | An HTTP header string sent by the client identifying its software application, version, and operating system. |
| [connection.state: SF](#term-conn_state_sf) | Normal SYN/FIN completion in Zeek; both sides cleanly opened and closed the connection. |
| [duration: 0.000184](#term-duration_microsecond) | Session elapsed time in seconds (184 microseconds), proving automated software speed rather than human typing. |
| [403 Forbidden](#term-http_403) | HTTP status code where the server understood the request but actively refused to authorize it. |
| [200 OK](#term-http_200) | HTTP status code indicating the web server successfully accepted and processed the request. |

---

<div class="bridge-card">
  <div class="bridge-label">Next Step in Curriculum</div>
  <div class="bridge-title">Lesson 01 — What the Analyst Is For</div>
  <p class="bridge-desc">Dana asked for Ethan's first writing assignment: keeping observation, interpretation, and judgment strictly separated on the page. Requires zero tools, takes about ninety minutes, and sets the foundation for your entire career as an analyst.</p>
  <a href="#/lessons/01-what-the-analyst-is-for" class="bridge-btn">Start Lesson 01 →</a>
</div>

**If most of that log meant nothing to you, you read it correctly.** It meant nothing to him either, and Dana did not think that was the interesting part. Ports, byte counts, `connection.state`, the `SF` he had nothing at all about — those are a few weeks of exposure, and none of them was what went wrong on his first ticket.

In [lesson 02](../lessons/02-reading-a-conversation.md), you open this capture and establish what the two conversations show. It cannot answer whether the endpoint use is intended or happens every sync: those questions need owner evidence and history. `SF` is explained there in a sentence. The `403` is waiting for you.
