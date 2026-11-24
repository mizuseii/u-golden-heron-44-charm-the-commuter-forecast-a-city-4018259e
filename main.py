#!/usr/bin/env python3
"""Charm the Commuter: Forecast a City That Isn't.

Writes ONE line of weather (max 140 chars) for a city that does not
exist to /output/entry.txt. Deterministic: no network, no randomness,
no time dependence — the same fixed line every run.
"""

import os
import sys

ENTRY = (
    "Good morning, Nimbostead: 14° and raining upwards, so hold your "
    "umbrella low and your hopes high — the 8:05 still stops here, somehow."
)


def main() -> int:
    # Gate: the bounty allows at most 140 characters, one line. Fail
    # loudly here rather than shipping an over-long entry.
    assert len(ENTRY) <= 140, f"entry is {len(ENTRY)} chars, over the 140 cap"
    assert "\n" not in ENTRY, "entry must be a single line"
    # Optional first argument overrides the output directory (used for
    # local verification); default is /output as the bounty requires.
    output_dir = sys.argv[1] if len(sys.argv) > 1 else "/output"
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
