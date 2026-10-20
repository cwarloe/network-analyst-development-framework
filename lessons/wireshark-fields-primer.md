# Wireshark: pull out the fields you need

A two-minute primer for [Lesson 03](03-names-and-expectations.md), [Lesson 04](04-what-encryption-hides.md) and [Lesson 06](06-when-it-breaks.md). It covers the moves those lessons take for granted once you know the basics: filter on a protocol or a field, show a field as a column, and pull fields out with `tshark`. New to Wireshark? Start with [Wireshark: a first look](wireshark-first-look.md).

<video controls width="100%" src="assets/video/wireshark-fields-primer.mp4">Video: Wireshark, pull out the fields you need (2:17)</video>

[Watch or download the video (2:17, mp4)](../assets/video/wireshark-fields-primer.mp4). The steps are written out below, so you can skip the video.

It practices on [`03-dns.pcap`](../assets/pcaps/03-dns.pcap) and on the first TLS connection in [`04-tls.pcap`](../assets/pcaps/04-tls.pcap), using only what those lessons' own text already shows. Nothing here answers a lesson question.

## The moves

1. **Every field has a name.** Click a field in the details pane and read the status bar: the name in brackets, such as `dns.qry.name`, is the name you use in filters. Right-click the field → Copy → Fieldname puts it on the clipboard. The words in the details pane are labels, not names.
2. **Filter on a protocol.** Type just the protocol, `tls`, and press Enter. Only packets that contain it stay. In `04-tls.pcap` that is 13 of 29.
3. **Filter on a field's value.** Write the field, `==`, then a value: `tls.handshake.type == 1` keeps the two packets that are a Client Hello.
4. **Numbers pick a conversation or a port.** `tcp.stream == 0` keeps one TCP conversation; streams are numbered from 0. `udp.port == 53` matches port 53 on either side, source or destination.
5. **Show a field as a column.** Click the field, right-click → **Apply as Column**. Every packet now shows that field's value in the packet list. Right-click the column heading → **Remove Column** to undo it.
6. **Pull fields out with `tshark`.** `-T fields` prints only the fields you ask for, one `-e` per field, in that order, separated by tabs. A blank cell means that packet has no such field. A comma means it has the field more than once.
7. **See one packet in full.** `-V` prints the whole details tree. Pick the packet with `-Y`, or the output is very long. It shows labels such as `Name`; to filter or extract you still need the field name.

## At the command line

Fields come out one row per packet. These are the query names in `03-dns.pcap`:

```
tshark -r assets/pcaps/03-dns.pcap -T fields -e frame.number -e dns.qry.name
```

```
1    www.github.com
2    www.github.com
3    en.wikipedia.org
4    en.wikipedia.org
```

Filtering and picking fields combine in one command. Here, the TLS packets of the first connection:

```
tshark -r assets/pcaps/04-tls.pcap -Y "tcp.stream == 0 && tls" -T fields -e frame.number -e tls.handshake.type
```

```
4    1
6    2,11,12,14
8    16
9    4
10
11
```

Frame 6 carries several handshake messages, so it has several values. Frames 10 and 11 carry none, so their cells are blank.

And the whole of one packet, labels and all (the output is long, so run it and scroll):

```
tshark -r assets/pcaps/03-dns.pcap -Y "frame.number == 1" -V
```

## Names differ between tools

Wireshark and Security Onion each use their own field names. Match them by meaning, and look each one up in [`field-names.md`](field-names.md):

| Wireshark / `tshark` | Security Onion |
|---|---|
| `dns.qry.name` | `dns.query.name` |
| `tls.handshake.extensions_server_name` | `ssl.server_name` |
| `dns.qry.type` (a number, such as `1`) | `dns.query.type_name` (a word, such as `A`) |

## Your turn

- **Lesson 03:** run the `-T fields` command it prints and read the table.
- **Lesson 04:** filter on `tls`, then pick fields by name.
- **Lesson 06:** use `-T fields` on the second capture, as the lesson shows.

Then answer each lesson's questions in your own words. A field name tells you where to look. What the value means is your call.

## Where this comes from

Field names in the status bar, `Apply as Column`, `Remove Column`, `Copy → Fieldname`, and filtering on a protocol or a field come from the [Wireshark User's Guide](https://www.wireshark.org/docs/wsug_html_chunked/): [chapter 6](https://www.wireshark.org/docs/wsug_html_chunked/ChapterWork.html), its [display filter](https://www.wireshark.org/docs/wsug_html_chunked/ChWorkBuildDisplayFilterSection.html) and [pop-up menu](https://www.wireshark.org/docs/wsug_html_chunked/ChWorkDisplayPopUpSection.html) pages, and the [status bar](https://www.wireshark.org/docs/wsug_html_chunked/ChUseStatusbarSection.html) page. `-T fields`, `-e`, `-V` and `-Y` come from the [`tshark` manual page](https://www.wireshark.org/docs/man-pages/tshark.html). Field names were checked against `tshark -G fields`. Every packet, row, field and value in the video was taken from this course's captures with `tshark`. The video is drawn, not recorded, so Wireshark's own window will look different from it. The scene file that produced it is [`wireshark-fields-primer.html`](../assets/video/wireshark-fields-primer.html).
