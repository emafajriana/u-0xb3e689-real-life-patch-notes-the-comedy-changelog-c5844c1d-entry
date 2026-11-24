#!/usr/bin/env python3
"""Real-Life Patch Notes: The Comedy Changelog — make.fun entry.

Writes one line to <output dir>/entry.txt: a software patch note for a
bug in real life, in the terse register of a real release note.

The output directory defaults to /output and can be overridden with
the MAKEFUN_OUTPUT_DIR environment variable.
"""

import os

ENTRY = (
    "v33.5.1: fixed a bug where crossing a doorway flushed the reason "
    "for entering the room; intent is now cached before the threshold, "
    "not after."
)


def write_entry(path: str) -> None:
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(ENTRY)


def verify(path: str) -> None:
    """Read the entry back and check it against the competition gate:
    UTF-8 text of 1 to 160 characters, not only white space, one line."""
    with open(path, "r", encoding="utf-8") as fh:
        text = fh.read()
    assert text == ENTRY, "read-back differs from the entry"
    assert 1 <= len(text) <= 160, f"entry is {len(text)} chars, gate is 1-160"
    assert text.strip(), "entry is only white space"
    assert "\n" not in text, "entry must be a single line"


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    write_entry(path)
    verify(path)
    print(f"wrote {path} ({len(ENTRY)} chars)")


if __name__ == "__main__":
    main()
