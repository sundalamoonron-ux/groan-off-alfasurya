#!/usr/bin/env python3
"""The One-Liner Groan-Off entry for make.fun.

Writes one original dad joke (91 characters, within the 1-140 gate)
to <output>/entry.txt. The joke is fixed, so the program is fully
deterministic: every run writes the exact same bytes.
"""

import os
import sys

JOKE = "I asked my AI for a dad joke. It said, 'I don't have a dad — but I do have a lot of dad-a.'"


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    text = JOKE
    # Gate: 1-140 characters, not only whitespace.
    if not (1 <= len(text) <= 140) or not text.strip():
        print("error: joke fails the 1-140 character gate", file=sys.stderr)
        return 1
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    # Self-check: read it back and fail hard if it is not exactly the joke.
    with open(path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != text:
        print("error: entry.txt does not match the joke", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
