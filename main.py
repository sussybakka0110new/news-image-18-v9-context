#!/usr/bin/env python3
"""Publish the committed world-news front page to the runner output directory."""

import os
import struct
import sys
from pathlib import Path

LIMIT = 1048576
MAX_SIDE = 1024
PNG_SIG = b"\x89PNG\r\n\x1a\n"
JPEG_SIG = b"\xff\xd8\xff"


def check_png_dimensions(payload: bytes) -> None:
    """Read the IHDR of a PNG and refuse one wider or taller than the cap."""
    if payload.startswith(PNG_SIG) and payload[12:16] == b"IHDR":
        width, height = struct.unpack(">II", payload[16:24])
        if width > MAX_SIDE or height > MAX_SIDE:
            raise SystemExit(
                f"image exceeds the {MAX_SIDE}x{MAX_SIDE} cap: {width}x{height}"
            )


def main() -> int:
    root = Path(__file__).resolve().parent
    payload = (root / "entry.png").read_bytes()
    if not payload:
        raise SystemExit("entry.png is empty")
    if len(payload) > LIMIT:
        raise SystemExit(f"image exceeds the one-megabyte cap: {len(payload)} bytes")
    if not payload.startswith((PNG_SIG, JPEG_SIG)):
        raise SystemExit("entry.png must be a complete PNG or JPEG")
    check_png_dimensions(payload)
    out = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out.mkdir(parents=True, exist_ok=True)
    (out / "entry.png").write_bytes(payload)
    return 0


if __name__ == "__main__":
    sys.exit(main())
