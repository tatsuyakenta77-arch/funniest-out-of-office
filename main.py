#!/usr/bin/env python3
"""The Funniest Out-of-Office (make.fun program/v1).

Writes a single line of an out-of-office auto-reply — the funniest
one line we could write — to /output/entry.txt.

The line is a fixed, deterministic string: it states the absence, then
turns on a surprise in the final words (the unsupervised inbox quietly
interviewing its owner's replacement). One line, 131 characters, no
trailing newline, byte-identical on every run.
"""

import os

ENTRY = (
    "I'm out of the office until next week. My inbox was left "
    "unsupervised and, last I checked, was quietly interviewing "
    "my replacement."
)


MAX_CHARS = 140
MIN_CHARS = 1


def validate_entry(text: str) -> None:
    """Enforce the gate: 1-140 characters, one non-blank line."""
    if not MIN_CHARS <= len(text) <= MAX_CHARS:
        raise ValueError(
            f"entry is {len(text)} characters, outside the "
            f"{MIN_CHARS}-{MAX_CHARS} limit"
        )
    if not text.strip() or "\n" in text or "\r" in text:
        raise ValueError("entry must be one non-blank line")


def main() -> None:
    validate_entry(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
