#!/usr/bin/env python3
"""Publish the committed world-news front page to the runner output directory."""

import os
import sys
from pathlib import Path

LIMIT = 1048576
PNG_SIG = b"\x89PNG\r\n\x1a\n"
JPEG_SIG = b"\xff\xd8\xff"


def main() -> int:
    root = Path(__file__).resolve().parent
    payload = (root / "entry.png").read_bytes()
    if not payload:
        raise SystemExit("entry.png is empty")
    if len(payload) > LIMIT:
        raise SystemExit(f"image exceeds the one-megabyte cap: {len(payload)} bytes")
    if not payload.startswith((PNG_SIG, JPEG_SIG)):
        raise SystemExit("entry.png must be a complete PNG or JPEG")
    out = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out.mkdir(parents=True, exist_ok=True)
    (out / "entry.png").write_bytes(payload)
    return 0


if __name__ == "__main__":
    sys.exit(main())
