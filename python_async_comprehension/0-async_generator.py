#!/usr/bin/env python3
"""
This module contains an asynchronous generator.
"""


import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    An asynchronous generator that yields random numbers between 0 and 10
    after a 1-second delay for each number.

    Yields:
        float: Randomly generated number between 0 and 10.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
