#!/usr/bin/env python3
"""news-summary-01 entry (Python 3.13, standard library only).

Writes the verified summary of Wednesday 11 November 2026 world news
(summary.txt, beside this file) to /output/entry.txt.

No network, no model calls, no randomness, no clock: the program is a
deterministic copy, so two runs write byte-identical output. The summary
it ships is 1,998 characters, inside the competition's 1-to-2,000 gate;
keep it that way if the text is ever refreshed. Outside the
grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:

    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
import shutil
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
SUMMARY = HERE / "summary.txt"


def main() -> int:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(SUMMARY, out_dir / "entry.txt")
    return 0


if __name__ == "__main__":
    sys.exit(main())
