#!/usr/bin/env python3
"""The Funniest Excuse for Skipping a Meeting.

Writes one deterministic excuse line to the output directory.
Output contract (program/v1): <output dir>/entry.txt, UTF-8,
1 to 200 characters, a single line. The output dir comes from
ENTRY_OUTPUT_DIR when set, otherwise /output (the grader's path),
falling back to ./output when /output is not writable.
"""

import os
from pathlib import Path

EXCUSE = (
    "Sorry, can't attend \u2014 my calendar read the agenda, recognized it "
    "as an email in a costume, and reported it to HR for impersonating work."
)


def output_dir() -> Path:
    env = os.environ.get("ENTRY_OUTPUT_DIR")
    if env:
        return Path(env)
    default = Path("/output")
    try:
        default.mkdir(parents=True, exist_ok=True)
        return default
    except OSError:
        return Path("output")


def main() -> None:
    # The gate counts characters, so guard the cap here as well.
    assert 1 <= len(EXCUSE) <= 200, "excuse must be 1..200 characters"
    target_dir = output_dir()
    target_dir.mkdir(parents=True, exist_ok=True)
    (target_dir / "entry.txt").write_text(EXCUSE, encoding="utf-8")


if __name__ == "__main__":
    main()
