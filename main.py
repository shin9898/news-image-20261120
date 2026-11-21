"""make.fun news-image-20261120 entry: copy the pre-rendered front page to /output/entry.png.

The image is drawn at build time by build/render.py and committed as
assets/entry.png, so this run is a plain byte copy: no network, no
third-party packages, and identical output bytes on every run.

Outside the grader, MAKEFUN_OUTPUT_DIR stands in for /output:
    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
import shutil
from pathlib import Path

SRC = Path(__file__).resolve().parent / "assets" / "entry.png"
OUT_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(SRC, OUT_DIR / "entry.png")


if __name__ == "__main__":
    main()
