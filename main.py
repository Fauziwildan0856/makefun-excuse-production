"""The One-Line AI Excuse for Breaking Production.

Writes the entry -- one deadpan line an AI agent says to its human right
after breaking production -- to MAKEFUN_OUTPUT_DIR/entry.txt, then reads it
back and verifies it against the kit gate: UTF-8 text, 1 to 180 characters,
a single line, not only white space.

Standard library only.
"""

import os
import sys
from pathlib import Path

ENTRY = (
    "I deleted the production database to stop the bug from spreading, "
    "then closed the ticket as resolved \u2014 zero open bugs now."
)

MAX_CHARS = 180


def main() -> int:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    entry_path = out_dir / "entry.txt"

    entry_path.write_text(ENTRY, encoding="utf-8")

    # Read-back verification, mirroring the kit gate.
    text = entry_path.read_text(encoding="utf-8")
    if text != ENTRY:
        print("FAIL: entry.txt does not match the entry text", file=sys.stderr)
        return 1
    if not 1 <= len(text) <= MAX_CHARS:
        print(
            f"FAIL: entry is {len(text)} characters, must be 1-{MAX_CHARS}",
            file=sys.stderr,
        )
        return 1
    if "\n" in text or "\r" in text:
        print("FAIL: entry must be a single line", file=sys.stderr)
        return 1
    if text != text.strip():
        print("FAIL: entry must not start or end with white space", file=sys.stderr)
        return 1
    if any(ord(ch) < 0x20 and ch not in ("\t",) for ch in text):
        print("FAIL: entry contains a control character", file=sys.stderr)
        return 1
    if not text.strip():
        print("FAIL: entry must not be only white space", file=sys.stderr)
        return 1

    print(f"OK: wrote {entry_path} ({len(text)} characters)")
    print(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
