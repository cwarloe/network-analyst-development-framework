# Stacking in Security Onion Hunt: a primer

A two-minute primer for [Hunt 02](hunt-02-least-frequency-analysis/README.md). Hunt 02 builds a stack as an Elasticsearch query: group events by a field, count them, and look at the rarest first. This shows the same thing on the Hunt screen, with `| groupby`.

<video controls width="100%" src="assets/video/security-onion-groupby-primer.mp4">Video: Stacking in Security Onion Hunt (2:27)</video>

[Watch or download the video (2:27, mp4)](../assets/video/security-onion-groupby-primer.mp4). The steps are written out below, so you can skip the video.

It uses captures from Book 1: [`07-suspicious.pcap`](../assets/pcaps/07-suspicious.pcap) for the stacks and [`06-failures.pcap`](../assets/pcaps/06-failures.pcap) for the missing-values example. Finish those lessons first, because the stacks show what they found.

## The moves

1. **Get a capture in.** `sudo so-import-pcap /full/path/to/07-suspicious.pcap`. It needs an Import node, or another node with sensor services such as Eval or Standalone. You can also upload the pcap in Grid, and it runs the import for you. The upload dialog in the 3.3.0 documentation shows a maximum upload size of 26,214,400 bytes, far more than these captures need. Security Onion runs Suricata and Zeek on the file and keeps the **original timestamps**. Import one pcap per command if you want a link to each.
2. **Set the time range.** Hunt starts at the last 24 hours. An imported capture keeps the date it was recorded, so you will see nothing until you widen the time picker. `07-suspicious.pcap` was recorded on August 19, 2026 (UTC).
3. **Stack.** Search `event.dataset:conn | groupby destination.ip destination.port`. A **Group Metrics** table appears with a **Count** for each combination. With only this capture imported you should see four rows, counting 40, 11, 9, and 1.
4. **Sort rarest first.** Click the **Count** heading to sort, and click again to flip the order. Ascending puts the rarest combinations at the top. Rare is not the same as bad: a count tells you where to look first, not what you found.
5. **Keep rows with missing values.** `groupby` leaves out events where the field is missing. Add an asterisk after the field name to keep them. Import `06-failures.pcap` and compare `event.dataset:conn | groupby network.protocol` with `event.dataset:conn | groupby network.protocol*`. The second adds a blank row of four connections that never got a protocol.
6. **Pivot from a value.** Click a value in the table. **Only** starts a new search for that value and keeps your `groupby` terms. **Correlate** finds related logs for the same conversation.

## Field names depend on where the data came from

An imported capture gets Security Onion's field names. The generated Hunt data uses ECS-style names.

| Field | Imported capture | Hunt data |
|---|---|---|
| HTTP user agent | `http.useragent` | `user_agent.original` |
| DNS name asked | `dns.query.name` | `dns.question.name` |
| Protocol | `network.protocol` | `service` |
| JA4 fingerprint | `hash.ja4` | `tls.ja4` |

The left column is the same in Security Onion 2.4 and 3.x ([checked](field-names.md) against both). The examples above use Security Onion's names because they come from imported captures. Hunt 02 uses the generated data from [`lab/generate-hunt-telemetry.py`](../lab/HUNT-DATA-GUIDE.md), so check the field list in your data before you copy a query. [`field-names.md`](field-names.md) lists Security Onion's names.

## What has and hasn't been checked

The steps follow Security Onion's documentation for Hunt, Dashboards, and `so-import-pcap`, which describe these features in both the 2.4 and 3.x documentation. The counts come from running Zeek 7.0 on the captures in this repository. The video is mostly drawn, so your screen will look different. Two screenshots in it, the Hunt screen and the Grid upload dialog, are from the Security Onion documentation (version 3.3.0). Their sample data is Security Onion's, not this course's. **None of this has been run end to end on a live Security Onion for this course.**

## Where this comes from

- Security Onion documentation: [Dashboards](https://docs.securityonion.net/en/3/main/dashboards/) (the query language, `groupby`, the time picker), [Hunt](https://docs.securityonion.net/en/3/main/hunt/), and [so-import-pcap](https://docs.securityonion.net/en/3/main/so-import-pcap/). The 2.4 versions are [Dashboards](https://docs.securityonion.net/en/2.4/dashboards.html), [Hunt](https://docs.securityonion.net/en/2.4/hunt.html), and [so-import-pcap](https://docs.securityonion.net/en/2.4/so-import-pcap.html).
- Field names: Security Onion's `zeek.http` and `zeek.ssl` ingest pipelines, and this repository's `lab/generate-hunt-telemetry.py`.
- The two screenshots are © Security Onion Solutions, LLC, from the documentation pages above, used for teaching with credit. They are not covered by this repository's license. Details are in [`assets/video/security-onion-screens/README.md`](../assets/video/security-onion-screens/README.md).
- The scene file that produced the video is [`security-onion-groupby-primer.html`](../assets/video/security-onion-groupby-primer.html).
