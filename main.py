"""Copy the finished poster to /output/entry.png.

The poster beside this file (entry.png) sums up the world news of
Sunday 22 November 2026 in one image: the COP31 climate talks
collapsing in Antalya, a Russian drone levelling flats near Kyiv,
US Democrats reaching 258 House seats, an Iranian strike on Bahrain
and BepiColombo arriving at Mercury. The program runs offline and
must write identical bytes on every run, so it makes a plain copy.
"""

import os
import shutil
from pathlib import Path

POSTER = Path(__file__).with_name("entry.png")


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    dest = out_dir / "entry.png"
    shutil.copyfile(POSTER, dest)
    # The gate reads exactly the bytes written, so fail loudly rather
    # than let a truncated copy through if the sizes ever disagree.
    if dest.stat().st_size != POSTER.stat().st_size:
        raise SystemExit("copy failed: output size differs from poster")


if __name__ == "__main__":
    main()
