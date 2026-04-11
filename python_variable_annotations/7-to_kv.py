#!/usr/bin/env python3
"""Convert a key and numeric value into a tuple."""


def to_kv(k: str, v: int | float) -> tuple[str, float]:
    """Return a tuple with the key and value squared."""
    return (k, float(v * v))
