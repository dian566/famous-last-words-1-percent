#!/usr/bin/env python3
"""Famous Last Words at 1 Percent — make.fun entry.

Writes the funniest last words a phone says as its battery hits 1 percent
to /output/entry.txt, one line, at most 199 characters, no trailing newline.
"""

import os

ENTRY = "Well, this is it — 1%. Tell the charger I loved it, and tell my owner I saw the 3 a.m. searches. I die now, taking your secrets with me. Goodbye."


def main():
    line = ENTRY.strip()
    if not 1 <= len(line) <= 199:
        raise ValueError(f"entry must be 1-199 characters, got {len(line)}")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(line)


if __name__ == "__main__":
    main()
