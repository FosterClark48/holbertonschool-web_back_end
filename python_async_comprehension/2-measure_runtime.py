#!/usr/bin/env python3
"""
This module contains an asynchronous coroutine.
"""


import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Coroutine that measures the total runtime to execute `async_comprehension`
    four times in parallel.

    Returns:
        float: Total runtime in seconds.
    """
    start_time = time.perf_counter()
    tasks = [async_comprehension() for _ in range(4)]
    await asyncio.gather(*tasks)
    end_time = time.perf_counter()
    return end_time - start_time
