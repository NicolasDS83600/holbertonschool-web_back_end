#!/usr/bin/env python3
"""Run multiple async wait operations concurrently."""

from typing import List
import asyncio
wait_random = __import__("0-basic_async_syntax").wait_random


async def wait_n(n: int, max_delay: int = 10) -> List[float]:
    """Return a list of delays from concurrently awaited coroutines."""
    coros = []
    for _ in range(n):
        coros.append(wait_random(max_delay))

    delays = []
    for task in asyncio.as_completed(coros):
        result = await task
        delays.append(result)
    return delays
