#!/usr/bin/env python3
"""Write the houseplant out-of-office reply to entry.txt.

Entry for make.fun's "The Houseplant Out-of-Office" bounty. The
program writes exactly one line of text and nothing else.

How the line targets the brief: the entry is an out-of-office
auto-reply in a houseplant's voice, at most 120 characters. The plant
is away photosynthesizing -- the only job it has -- and its return
policy is a threat delivered in plant terms: water it, or the next
reply arrives as a brown leaf -- the only attachment a plant can send.
Plant voice, surprise, and brevity are all in one line.
"""

import os
from pathlib import Path

LINE = "Out of office: photosynthesizing. Water me, or my next reply will be a brown leaf."

MAX_CHARS = 120
ENTRY_FILENAME = "entry.txt"


def write_entry(out_dir: Path) -> Path:
    """Write the line to entry.txt inside out_dir and return its path.

    The file holds exactly the line and nothing else: no trailing
    newline, no extra whitespace, so the gate sees one line of at
    most 120 chars.
    """
    if not LINE or chr(10) in LINE or len(LINE) > MAX_CHARS:
        raise ValueError("the entry must be exactly one non-empty line within the limit")
    out_dir.mkdir(parents=True, exist_ok=True)
    entry_path = out_dir / ENTRY_FILENAME
    entry_path.write_text(LINE, encoding="utf-8")
    return entry_path


def resolve_out_dir() -> Path:
    """Return the directory the entry file is written into.

    Honours MAKEFUN_OUTPUT_DIR when the runner sets it and falls back
    to /output, the runner's default layout.
    """
    return Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))


def main() -> None:
    write_entry(resolve_out_dir())


if __name__ == "__main__":
    main()
