#!/usr/bin/python3
"""Convert a key and numeric value into a tuple."""

from typing import Union


def to_kv(k: str, v: int | float) -> tuple:
    """Return a tuple with the key and value squared."""
    return (k, v * v)
