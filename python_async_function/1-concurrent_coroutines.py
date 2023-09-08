#!/usr/bin/env python3
"""
Asynchronous coroutine to execute multiple wait_random coroutines.
"""


import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Execute wait_random n times with the specified max_delay.

    Args:
        n (int): Number of times to execute wait_random.
        max_delay (int): The maximum delay for wait_random.

    Returns:
        List[float]: List of delays sorted in ascending order.
    """
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    delays = []
    for future in asyncio.as_completed(tasks):
        delay = await future
        delays.append(delay)
    return delays
