#!/usr/bin/env python3
"""
A basic asynchronous coroutine.
"""


import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Wait for a random delay between 0 and max_delay seconds
    and return it.

    Args:
        max_delay (int): The maximum delay time in seconds.
        Default is 10.

    Returns:
        float: The actual delay time.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
