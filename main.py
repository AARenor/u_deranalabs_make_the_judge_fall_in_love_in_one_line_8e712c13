#!/usr/bin/env python3
"""Write the one-line entry artifact for the judge."""

import os
from pathlib import Path

# One scene, one particular (the second turn of the key), one withheld truth.
LINE = (
    "Every night he locks the door twice, once for himself and once for my "
    "mother, who has been gone eleven years and is still only running late."
)


def write_entry(output_dir: Path) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_text(LINE, encoding="utf-8")


def main() -> None:
    write_entry(Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")))


if __name__ == "__main__":
    main()
