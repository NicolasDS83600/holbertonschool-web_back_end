#!/usr/bin/env python3
"""Schedule and run multiple asyncio tasks concurrently."""

from typing import List
import asyncio
task_wait_random = __import__("3-tasks").task_wait_random


async def task_wait_n(n: int, max_delay: int = 10) -> List[float]:
    """Return a list of delays from concurrently completed tasks."""

    coros = []
    for _ in range(n):
        coros.append(task_wait_random(max_delay))

    delays = []
    for task in asyncio.as_completed(coros):
        result = await task
        delays.append(result)
    return delays
