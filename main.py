"""A whole story in 32 characters: a Wi-Fi network name.

Prints the name to stdout and writes the exact same name, with no
trailing newline, to /output/entry.txt. Standard library only, no
network access, no files read — the name is a constant in this file.
The 32-character gate is checked on every run so an over-long edit
can never slip through silently. A Wi-Fi name has no room for setup —
the joke has to be the name.
"""

import os
import sys

LINE = "MyExTookTheRouter"


def main() -> int:
    if not 1 <= len(LINE) <= 32:
        print(f"error: line is {len(LINE)} chars, must be 1-32",
              file=sys.stderr)
        return 1
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
