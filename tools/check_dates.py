#!/usr/bin/env python3
"""Check NADF narrative dates, ticket IDs, and surnames against the author bible.

Modelled on Portland Desk's tools/check_dates.py, but scoped to this repo.
It does not run against docs/portland-desk/.

Checks:
- Months and ISO dates in Book 1 chapters (00-09) against the August Year 4
  open recorded in narrative/author-bible/timeline.md, unless a line is marked
  <!-- date-ok: reason -->.
- Weekday drift only when a weekday and a YYYY-MM-DD date appear on the same
  line (or the timeline pins a date for that chapter and the same line names
  both). Later Book 1 and Book 2 chapters name weekdays without pinned calendar
  dates; those are not failed here.
- Ticket and evidence IDs that carry a year, or collide across chapters.
- SEC-prefixed fixed-width yearless IDs (SEC0004021) are accepted. The short
  form still in the current chapters (SEC-4021) is accepted until those
  chapters are migrated; it is not a year-carrying ID.
- date-ok markers must give a reason.
- A registered first name may only be paired with its registered surname,
  using the NADF cast registry in narrative/author-bible/cast-and-relationships.md.

Run from the repository root:

    python3 tools/check_dates.py

Exit code 1 when a finding is printed.
"""
from __future__ import annotations

import calendar
import glob
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
NARRATIVE = ROOT / "narrative"
TIMELINE = ROOT / "narrative/author-bible/timeline.md"
CAST = ROOT / "narrative/author-bible/cast-and-relationships.md"

MONTHS = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December",
]
DAYS = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
YEAR_ZERO = 2022  # Year 4 is 2026, same anchor as Portland Desk.
BOOK1 = {f"{i:02d}" for i in range(0, 10)}
BOOK2 = {f"{i:02d}" for i in range(10, 15)}

# Year-carrying or retired formats. Fixed-width yearless IDs (SEC0004021) and
# the transitional short form (SEC-4021) are handled separately and do not
# match this pattern.
YEAR_OR_OLD_ID = re.compile(
    r"\b(?:INC|ESC|EVD|HD|SEC)-?(?:[A-Z]+-)?20\d\d-\d+\b"
    r"|\b(?:INC|ESC|EVD|HD|SEC)\d{2,4}-\d+\b"
    r"|\bHD-\d+\b"
)
FIXED_ID = re.compile(r"\b(INC|ESC|EVD|SEC)(\d{7})\b")
SHORT_SEC = re.compile(r"\bSEC-(\d+)(?![\d-])")
ISO = re.compile(r"\b(20\d\d)-(\d\d)-(\d\d)\b")
DATE_OK = re.compile(r"<!--\s*date-ok(.*?)-->")
NAME_PAIR = re.compile(r"\b([A-Z][a-z]+) ([A-Z][a-z]+)\b")
EMAIL = re.compile(r"\b([a-z]+)\.([a-z]+)@harrowmere\.")


def chapter_files():
    return sorted(NARRATIVE.glob("[01][0-9]-*.md"))


def ep_of(path: Path) -> str:
    return path.name[:2]


def timeline_text() -> str:
    if not TIMELINE.exists():
        print("missing narrative/author-bible/timeline.md")
        sys.exit(1)
    return TIMELINE.read_text()


def episode_months():
    """Map episode id -> month index (0-11) from the NADF timeline table."""
    out, cur = {}, None
    for line in timeline_text().splitlines():
        m = re.match(r"\| Ch (\d\d)\s+\|", line)
        if m:
            cur = m.group(1)
            out[cur] = ""
        if cur and line.startswith("|"):
            cells = [c.strip() for c in line.split("|")]
            if len(cells) > 3:
                out[cur] += " " + cells[3]
        if cur and line.startswith("|---"):
            # header separator; ignore
            pass
    res = {}
    for ep, text in out.items():
        found = [i for i, n in enumerate(MONTHS) if n in text]
        if found:
            res[ep] = found[0]
    return res


def pinned_iso_dates():
    """Map episode id -> set of (year, month, day) pinned in the timeline."""
    out = {}
    cur = None
    for line in timeline_text().splitlines():
        m = re.match(r"\| Ch (\d\d)\s+\|", line)
        if m:
            cur = m.group(1)
        if not cur or not line.startswith("|"):
            continue
        for iso in ISO.finditer(line):
            out.setdefault(cur, set()).add(
                (int(iso.group(1)), int(iso.group(2)), int(iso.group(3)))
            )
    return out


def weekday_of(y, mo, d):
    return calendar.day_name[calendar.weekday(y, mo, d)]


def check_months_and_iso():
    bad = 0
    months = episode_months()
    for path in chapter_files():
        ep = ep_of(path)
        allowed_month = months.get(ep)
        for ln, line in enumerate(path.read_text().splitlines(), 1):
            if "date-ok" in line:
                continue
            rel = path.relative_to(ROOT).as_posix()
            if allowed_month is not None:
                for i, name in enumerate(MONTHS):
                    if re.search(rf"\b{name}\b", line) and i != allowed_month:
                        print(f"{rel}:{ln}: '{name}' but Ch {ep} is {MONTHS[allowed_month]}")
                        bad += 1
            for m in ISO.finditer(line):
                year, month, day = int(m.group(1)), int(m.group(2)), int(m.group(3))
                if allowed_month is not None:
                    want_year = YEAR_ZERO + 4
                    if (year, month) != (want_year, allowed_month + 1):
                        print(
                            f"{rel}:{ln}: {m.group(0)} but Ch {ep} is "
                            f"{want_year}-{allowed_month + 1:02d}"
                        )
                        bad += 1
                try:
                    calendar.weekday(year, month, day)
                except ValueError:
                    print(f"{rel}:{ln}: {m.group(0)} is not a real calendar date")
                    bad += 1
    return bad


def check_weekdays():
    """Fail only when a weekday and a calendar date disagree on the same line."""
    bad = 0
    pinned = pinned_iso_dates()
    for path in chapter_files():
        ep = ep_of(path)
        rel = path.relative_to(ROOT).as_posix()
        for ln, line in enumerate(path.read_text().splitlines(), 1):
            if "date-ok" in line:
                continue
            days = [d for d in DAYS if re.search(rf"\b{d}\b", line)]
            isos = list(ISO.finditer(line))
            for m in isos:
                y, mo, d = int(m.group(1)), int(m.group(2)), int(m.group(3))
                try:
                    want = weekday_of(y, mo, d)
                except ValueError:
                    continue
                for named in days:
                    if named != want:
                        print(
                            f"{rel}:{ln}: '{named}' but {m.group(0)} is a {want}"
                        )
                        bad += 1
            # If the timeline pins a single date for the chapter and this line
            # names a weekday next to that same ISO date, the loop above
            # already caught it. Do not compare loose weekdays to a pinned
            # date: Book 1 chapters after the prologue span several weekdays
            # under a copied frontmatter date.
            _ = pinned.get(ep)
    return bad


def check_ids():
    bad = 0
    seen = {}  # canonical id -> set of episodes
    for path in chapter_files():
        ep = ep_of(path)
        rel = path.relative_to(ROOT).as_posix()
        text = path.read_text()
        for m in YEAR_OR_OLD_ID.finditer(text):
            print(
                f"{rel}: {m.group(0)} carries a year or old format; "
                "use a yearless fixed-width ID like SEC0004021"
            )
            bad += 1
        for m in FIXED_ID.finditer(text):
            seen.setdefault(m.group(0), set()).add(ep)
        # Transitional short form maps onto the same counter so a later
        # SEC0004021 cannot collide with an earlier SEC-4021 unnoticed.
        for m in SHORT_SEC.finditer(text):
            canonical = f"SEC{int(m.group(1)):07d}"
            seen.setdefault(canonical, set()).add(ep)
    for i, eps in seen.items():
        if len(eps) > 1:
            print(f"{i} is used in more than one chapter: {sorted(eps)}")
            bad += 1
    for prefix in ("INC", "ESC", "EVD", "SEC"):
        rng = {}
        for i, eps in seen.items():
            if i.startswith(prefix):
                n = int(i[len(prefix):])
                for ep in eps:
                    lo, hi = rng.get(ep, (10**9, -1))
                    rng[ep] = (min(lo, n), max(hi, n))
        prev = None
        for ep in sorted(rng):
            if prev and rng[ep][0] <= rng[prev][1]:
                print(
                    f"{prefix} IDs in Ch {ep} start at {rng[ep][0]} "
                    f"but Ch {prev} reaches {rng[prev][1]}"
                )
                bad += 1
            prev = ep
    return bad


def check_date_ok_reasons():
    bad = 0
    for path in chapter_files():
        rel = path.relative_to(ROOT).as_posix()
        for ln, line in enumerate(path.read_text().splitlines(), 1):
            for m in DATE_OK.finditer(line):
                if not re.match(r"\s*:\s*\S", m.group(1)):
                    print(f"{rel}:{ln}: date-ok marker needs a reason (<!-- date-ok: why -->)")
                    bad += 1
    return bad


def cast_registry():
    if not CAST.exists():
        print("missing narrative/author-bible/cast-and-relationships.md")
        sys.exit(1)
    text = CAST.read_text()
    if "## Cast registry" not in text:
        print("cast-and-relationships.md has no '## Cast registry' table")
        sys.exit(1)
    sec = text.split("## Cast registry", 1)[1]
    # Stop at the next same-or-higher heading if one exists.
    nxt = re.search(r"\n## [^#]", sec[1:])
    if nxt:
        sec = sec[: nxt.start() + 1]
    reg = {}
    for m in re.finditer(r"^\| ([A-Z][a-z]+) \| ([A-Za-z]+) \|", sec, re.M):
        if m.group(1) != "First":
            reg.setdefault(m.group(1), set()).add(m.group(2))
    return reg


def check_cast():
    bad = 0
    reg = cast_registry()
    if not reg:
        print("cast registry table is empty")
        return 1
    surnames = {s for v in reg.values() for s in v if s != "none"}
    files = list(chapter_files())
    files += list((ROOT / "narrative/author-bible").glob("*.md"))
    files += [ROOT / "BOOK-1.md", ROOT / "BOOK-2.md", ROOT / "narrative/README.md"]
    for path in sorted(set(files)):
        if not path.exists():
            continue
        try:
            text = path.read_text()
        except (UnicodeDecodeError, IsADirectoryError):
            continue
        rel = path.relative_to(ROOT).as_posix()
        # The registry table itself lists the allowed pairings.
        in_registry = path.name == "cast-and-relationships.md"
        for m in NAME_PAIR.finditer(text):
            first, last = m.groups()
            if first in reg and last in surnames and last not in reg[first]:
                if in_registry and "## Cast registry" in text[: m.start()]:
                    continue
                print(
                    f"{rel}: '{m.group(0)}' but the cast registry says "
                    f"{first} {'/'.join(sorted(reg[first]))}"
                )
                bad += 1
        for m in EMAIL.finditer(text):
            first, last = m.group(1).title(), m.group(2).title()
            if first in reg and last in surnames and last not in reg[first]:
                print(
                    f"{rel}: {m.group(0)} but the cast registry says "
                    f"{first} {'/'.join(sorted(reg[first]))}"
                )
                bad += 1
    return bad


def main():
    bad = 0
    bad += check_months_and_iso()
    bad += check_weekdays()
    bad += check_ids()
    bad += check_date_ok_reasons()
    bad += check_cast()
    print(f"{bad} date finding(s)")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
