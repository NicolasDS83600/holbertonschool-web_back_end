#!/usr/bin/env python3
"""Yield random floats with async delays."""

import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """Yield random floats after one second delays."""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
