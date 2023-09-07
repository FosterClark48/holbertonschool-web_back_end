#!/usr/bin/env python3
"""
This module provides a type-annotated function `floor` that returns
the floor of a given float.

Example:
    >>> floor(3.7)
    3
    >>> floor(-3.7)
    -4
"""


from math import floor as math_floor


def floor(n: float) -> int:
    """
    Return the floor of the given float number.

    The function takes a float `n` and returns its floor as an integer.
    The floor of a number is the largest integer less than or equal
    to the number.
    """
    return math_floor(n)
