#!/usr/bin/env python3
"""
This module contains an asynchronous coroutine.
"""


from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Coroutine that collects 10 random numbers using async comprehension
    over the `async_generator`, then returns the 10 random numbers.

    Returns:
        List[float]: List of 10 random numbers.
    """
    return [i async for i in async_generator()]
