#!/usr/bin/env python3
"""news-image-20261118 entry: copy the bundled 1024x1024 PNG to /output/entry.png.

Deterministic by construction: a pure byte copy of a fixed asset in this
repository. No network, no randomness, no timestamps — every run writes the
exact same bytes.
"""
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ASSET = os.path.join(HERE, "assets", "entry.png")


def main():
    out = sys.argv[1] if len(sys.argv) > 1 else "/output/entry.png"
    parent = os.path.dirname(os.path.abspath(out))
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(ASSET, "rb") as src, open(out, "wb") as dst:
        shutil.copyfileobj(src, dst, length=1024 * 1024)
    print("wrote", out)


if __name__ == "__main__":
    main()
