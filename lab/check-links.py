#!/usr/bin/env python3
"""Verify every relative Markdown link in the repository resolves.

Cheap, fast, and catches the one thing that breaks constantly: a file moves
and the links to it do not. External links are not fetched -- this only
checks that paths inside the repository are real.

    python3 lab/check-links.py [root]
"""
import re, sys, pathlib

LINK = re.compile(r'\[[^\]]*\]\(([^)\s]+?)(?:\s+"[^"]*")?\)')


def main(root="."):
    root = pathlib.Path(root)
    checked = broken = 0
    for f in sorted(root.rglob("*.md")):
        if ".git" in f.parts:
            continue
        for m in LINK.finditer(f.read_text()):
            target = m.group(1).strip()
            if target.startswith(("http://", "https://", "mailto:", "#")):
                continue
            path = target.split("#", 1)[0]
            if not path:
                continue
            checked += 1
            if not (f.parent / path).resolve().exists():
                print(f"BROKEN  {f}  ->  {target}")
                broken += 1
    print(f"{checked} relative links checked, {broken} broken")
    return 1 if broken else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1] if len(sys.argv) > 1 else "."))
