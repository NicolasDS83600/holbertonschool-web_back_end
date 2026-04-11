#!/usr/bin/env python3
"""Convert a key and numeric value into a tuple."""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Return a tuple with the key and value squared."""
    return (k, float(v * v))
