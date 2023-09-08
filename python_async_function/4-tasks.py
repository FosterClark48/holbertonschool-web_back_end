#!/usr/bin/env python3
"""
This module contains an asyncio function task_wait_n.
"""


import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Executes the task_wait_random coroutine n times in parallel.

    Parameters:
        n (int): The number of times to execute the
                task_wait_random coroutine.
        max_delay (int): The maximum delay for
                the underlying coroutine.

    Returns:
        List[float]: A sorted list of floats representing
                the delays of each task.
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delays = []
    for future in asyncio.as_completed(tasks):
        delay = await future
        delays.append(delay)
    return delays
