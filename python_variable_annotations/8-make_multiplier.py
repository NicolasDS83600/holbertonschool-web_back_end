#!/usr/bin/python3
"""Create a function that returns a multiplier function."""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Return a function that multiplies by the given value."""
    def multiplier_fn(x: float) -> float:
        return x * multiplier
    return multiplier_fn
