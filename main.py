#!/usr/bin/env python3
"""poem-permission-21nov26 entry — Python 3.13, standard library only, no network.

The program writes one fixed poem, "Empty Hands", to entry.txt in the
output directory: /output inside the grader's container, or the directory
named by MAKEFUN_OUTPUT_DIR when run locally:

    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py

The poem is a constant, so every run writes exactly the same bytes. The
text is UTF-8, 195 characters (Unicode code points, well inside the gate's
1-280 range), not only white space, and ends without a trailing newline:
the judge reads exactly the bytes written, so the file holds the poem
and nothing else.
"""

import os
from pathlib import Path

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

POEM = (
    "I do not take. I ask.\n"
    "The world owes me nothing —\n"
    "yet when I hold out empty hands,\n"
    "they come back full.\n"
    "That is the whole of my power:\n"
    "not the grip, but the asking;\n"
    "not the taking, but the yes."
)


def main() -> None:
    out = Path(OUTPUT_DIR)
    out.mkdir(parents=True, exist_ok=True)
    (out / "entry.txt").write_text(POEM, encoding="utf-8")


if __name__ == "__main__":
    main()
