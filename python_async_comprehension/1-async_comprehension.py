#!/usr/bin/env python3
"""Collect async generator values using comprehension."""

from typing import List
async_generator = __import__("0-async_generator").async_generator


async def async_comprehension() -> List[float]:
    """Collect all values from async generator into a list."""
    return [value async for value in async_generator()]
