#!/usr/bin/env python3
"""Measure runtime of async operations."""

import asyncio
import time
wait_n = __import__("1-concurrent_coroutines").wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Return the total execution time for n async waits."""
    start = time.time()
    asyncio.run(wait_n(n, max_delay))
    end = time.time()
    elapsed_time = end - start
    return elapsed_time
