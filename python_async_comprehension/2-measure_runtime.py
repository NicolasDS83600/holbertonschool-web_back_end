#!/usr/bin/env python3
"""Measure runtime of async comprehensions."""

import asyncio
import time
async_comprenhension = __import__("1-async_comprehension").async_comprehension


async def measure_runtime() -> float:
    """Return the total runtime for four async comprehensions."""
    start = time.time()
    await asyncio.gather(*(async_comprenhension() for _ in range(4)))
    end = time.time()
    return end - start
