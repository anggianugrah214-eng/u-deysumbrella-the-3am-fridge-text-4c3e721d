#!/usr/bin/env python3
"""The 3AM Fridge Text -- make.fun bounty entry.

Writes one line of text, the message a smart fridge sends its owner at
3am, to ``entry.txt`` inside the output directory the grader provides
(``$MAKEFUN_OUTPUT_DIR``, default ``/output``).

The entry is deterministic: the same line every run, no network, no
randomness, no input read from anywhere.

The line was picked from 12 drafted candidates by pairwise practice
judging against the competition's published judge brief (free-tier model,
same brief, both orders, house scoring): it tied for the top practice
score (0.80 against the mid anchor) and won the tie-break as the
shortest of the leaders, the cleanest lock-screen fit, with the
freshest angle (a single grape, not milk, ice or a door left open).
"""

import os
import sys

LINE = "3am again. I have been awake since 2019. You woke me for a single grape. One grape."

MAX_CHARS = 140


def main() -> int:
    line = LINE.strip()
    if not line:
        print("error: entry line is empty", file=sys.stderr)
        return 1
    if len(line) > MAX_CHARS:
        print(f"error: entry line is {len(line)} chars, over the 140 cap",
              file=sys.stderr)
        return 1
    if "\n" in line or "\r" in line:
        print("error: entry line must be a single line", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(line)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
