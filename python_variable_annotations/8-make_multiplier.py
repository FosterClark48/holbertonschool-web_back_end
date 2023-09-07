#!/usr/bin/env python3
"""
This module provides a type-annotated function `make_multiplier`
that takes a float `multiplier` as argument and returns a function
that multiplies a float by `multiplier`.

Example:
    >>> multiply_by_two = make_multiplier(2.0)
    >>> multiply_by_two(4.0)
    8.0
"""


from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Return a function that multiplies its argument
    by the given multiplier.

    Args:
        multiplier (float): The number by which the returned function
        will multiply its argument.

    Returns:
        Callable[[float], float]: A function that multiplies its
        argument by `multiplier`.
    """
    def multiplier_func(x: float) -> float:
        return x * multiplier

    return multiplier_func
