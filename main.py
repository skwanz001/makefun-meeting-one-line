#!/usr/bin/env python3
"""The Meeting That Should Have Been One Line.

Writes the single sentence that could have replaced an entire pointless
meeting to /output/entry.txt. Standard library only.
"""

import os

LINE = (
    # Strategy: the line names the meeting's only product — another meeting.
    # Self-referential, instantly recognizable to anyone who has sat through
    # a useless one, and after it no one can justify holding the meeting.
    "The only decision we made today was to schedule another meeting "
    "about the decision we didn't make."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
