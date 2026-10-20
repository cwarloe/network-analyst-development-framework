# Wireshark: a first look

A two-minute primer for [Lesson 02](02-reading-a-conversation.md). It covers the handful of Wireshark moves that lesson, and several after it, take for granted: open a capture, filter it, and follow one conversation.

<video controls width="100%" src="assets/video/wireshark-first-look.mp4">Video: Wireshark, a first look (2:14)</video>

[Watch or download the video (2:14, mp4)](../assets/video/wireshark-first-look.mp4). The steps are written out below, so you can skip the video.

It practices on **conversation one** of [`02-conversation.pcap`](../assets/pcaps/02-conversation.pcap). Lesson 02 asks you to analyze conversation two, so nothing here answers the lesson.

## The six moves

1. **Open the capture.** File → Open, or drag the `.pcap` onto the window. A capture is a recording of packets, in order, as they crossed one point on the network.
2. **Click a packet.** Its layers appear in the details tree, and clicking a layer lights up its bytes in the bytes pane.
3. **Type a display filter and press Enter.** `tcp.port == 42876` keeps only packets using that port. The filter bar turns red while the filter is incomplete or invalid, and green when it is valid.
4. **Know that nothing was deleted.** A filter only changes what you see. All 20 packets are still in the file. Click **Clear** to bring them back.
5. **Combine conditions.** `and` (or `&&`) needs both to be true; `or` (or `||`) needs either. `tcp.port == 42876 and tcp.flags.syn == 1` shows the two packets that open the connection. Comparisons work too: `tcp.len > 0` keeps only packets that carry data.
6. **Follow the stream.** Right-click a packet → Follow → TCP Stream. The packets of one conversation come back together as what the client said and what the server said.

## No screen to click on?

`tshark` takes the same filters with `-Y`:

```
tshark -r assets/pcaps/02-conversation.pcap -Y "tcp.port == 42876 && tcp.len > 0"
```

## Your turn

Open `02-conversation.pcap`, filter to conversation two (it starts at frame 11), follow its TCP stream, and then work through [Lesson 02](02-reading-a-conversation.md).

The screen shows you what happened. What it means is your call.

## Where this comes from

How the filter bar, the syntax colors, Clear, `and`/`or`, and the right-click menu behave comes from [Wireshark User's Guide, chapter 6](https://www.wireshark.org/docs/wsug_html_chunked/ChapterWork.html). Every packet, byte, and line of stream text in the video was taken from this course's capture with `tshark`. The video is drawn, not recorded, so Wireshark's own window will look different from it. The scene file that produced it is [`wireshark-first-look.html`](../assets/video/wireshark-first-look.html).
