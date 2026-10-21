"""Shop API helpers for the example pipeline.

The Jenkinsfile in this directory would run these tests with PYTHONPATH=src.
This module does not open a socket. shop.example.com is a documentation name.
"""

from __future__ import annotations


def quote_total(unit_cents: int, qty: int) -> int:
    if unit_cents < 0 or qty < 0:
        raise ValueError("negative money")
    return unit_cents * qty


def health() -> dict[str, object]:
    return {"service": "shop-api", "host": "shop.example.com", "ok": True}
