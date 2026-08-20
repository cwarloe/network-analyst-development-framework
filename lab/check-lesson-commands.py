#!/usr/bin/env python3
"""Run every tshark and zeek command printed in the lessons, and check the
output printed underneath against what the command actually produces.

Two checks per command.

  runs        The command exits 0 and produces output. Catches a renamed
              field, a moved capture, a filter that stopped parsing.

  matches     Every value shown in the block underneath the command really
              appears in that command's output. Catches a lesson that
              describes tool output from memory instead of from a run.

The second check applies only when an output block sits directly beneath the
command with nothing between them. A block separated by prose is something
else -- a Security Onion view, an aggregate, a reformatted summary -- and is
reported as not checkable rather than guessed at.

Exit codes: 0 all good, 1 a real failure, 2 tools missing (cannot verify).
"""

import os
import re
import shutil
import subprocess
import sys
import tempfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

GREEN, RED, YELLOW, DIM, OFF = "\033[32m", "\033[31m", "\033[33m", "\033[2m", "\033[0m"

# Values a lesson prints for legibility that no tool ever emits.
DECORATION = {"-", "--", "...", "<-", "|", "+", "no.", "•"}

# tshark prints these as True/False; lessons render flag columns as 1/0.
BOOLISH = {"true": "1", "false": "0"}


def find_zeek():
    for candidate in (os.environ.get("ZEEK"), shutil.which("zeek"),
                      "/opt/zeek-install/bin/zeek", "/usr/local/zeek/bin/zeek",
                      "/opt/zeek/bin/zeek", "/usr/bin/zeek"):
        if candidate and os.path.exists(candidate):
            return candidate
    return None


def blocks_in(text):
    return [(m.start(), m.end(), m.group(1))
            for m in re.finditer(r"```(?:\w+)?\n(.*?)```", text, re.S)]


def is_command(block):
    return re.match(r"\s*(tshark|zeek)\b", block) is not None


def tokens(text):
    """Data-shaped tokens: numbers, addresses, hex, hostnames, quoted strings.

    Prose words are dropped, so an annotated block contributes only its data.
    """
    out = set()
    for raw in re.split(r"[\s,]+", text):
        t = raw.strip().strip("`*").lower()
        if not t or t in DECORATION:
            continue
        if re.fullmatch(r"[a-z]+", t):          # a bare word is prose or a header
            continue
        if re.fullmatch(r"[\d.]+|0x[0-9a-f]+|[\w.:=/-]*\d[\w.:=/-]*", t):
            out.add(BOOLISH.get(t, t))
    return out


def run(command, zeek):
    """Run one printed command from the repository root."""
    cmd = re.sub(r"\\\n\s*", " ", command).strip()
    if cmd.startswith("zeek"):
        if not zeek:
            return None, "zeek not found"
        workdir = tempfile.mkdtemp(prefix="lessoncheck-")
        cmd = cmd.replace("zeek", zeek, 1)
        cmd = re.sub(r"(-r )(assets/)", r"\1" + ROOT + r"/\2", cmd)
    else:
        workdir = ROOT
    try:
        p = subprocess.run(cmd, shell=True, cwd=workdir, capture_output=True,
                           text=True, timeout=120)
    except subprocess.TimeoutExpired:
        return None, "timed out"
    if p.returncode != 0:
        return None, (p.stderr.strip().splitlines() or ["exit %d" % p.returncode])[-1]
    if workdir != ROOT:
        # zeek writes logs rather than printing; its output is the log set.
        logs = sorted(f for f in os.listdir(workdir) if f.endswith(".log"))
        if not logs:
            return None, "wrote no logs"
        body = "".join(open(os.path.join(workdir, f), encoding="utf-8",
                            errors="replace").read() for f in logs)
        shutil.rmtree(workdir, ignore_errors=True)
        return "wrote " + " ".join(logs) + "\n" + body, None
    return p.stdout, None


def main():
    if not shutil.which("tshark"):
        print("tshark not found -- CANNOT VERIFY HERE.\n"
              "This checks lesson text against real tool output, so without the\n"
              "tools it proves nothing. That is not the same as a failure.")
        return 2
    zeek = find_zeek()

    lessons = sorted(
        os.path.join(dp, f)
        for dp, _, fs in os.walk(os.path.join(ROOT, "lessons"))
        for f in fs if f.endswith(".md"))

    checked = failed = skipped = 0

    for path in lessons:
        rel = os.path.relpath(path, ROOT)
        text = open(path, encoding="utf-8").read()
        bs = blocks_in(text)
        printed_header = False

        for i, (start, end, body) in enumerate(bs):
            if not is_command(body):
                continue
            if not printed_header:
                print("\n" + rel)
                printed_header = True

            label = re.sub(r"\s+", " ", body.strip())
            label = (label[:66] + "...") if len(label) > 66 else label

            output, error = run(body, zeek)
            if error == "zeek not found":
                print(f"  {YELLOW}skip{OFF}  {label}\n        zeek not found -- cannot check this one")
                skipped += 1
                continue
            if error:
                print(f"  {RED}FAIL{OFF}  {label}\n        did not run: {error}")
                failed += 1
                continue
            if not output.strip():
                print(f"  {RED}FAIL{OFF}  {label}\n        ran, but produced no output")
                failed += 1
                continue
            checked += 1
            print(f"  {GREEN}runs{OFF}  {label}")

            # Only an immediately adjacent block is this command's output.
            if i + 1 >= len(bs):
                continue
            gap = text[end:bs[i + 1][0]]
            nxt = bs[i + 1][2]
            if gap.strip() or is_command(nxt):
                print(f"        {DIM}output block not adjacent -- not checked{OFF}")
                skipped += 1
                continue

            missing = sorted(tokens(nxt) - tokens(output))
            if missing:
                print(f"  {RED}FAIL{OFF}  values shown that the command does not produce:")
                for m in missing[:12]:
                    print(f"          {m}")
                if len(missing) > 12:
                    print(f"          ... and {len(missing) - 12} more")
                failed += 1
            else:
                print(f"        {GREEN}matches{OFF} the block underneath it")

    print()
    summary = f"{checked} commands ran, {failed} failed"
    if skipped:
        summary += f", {skipped} output blocks not machine-checkable"
    print(summary)
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
