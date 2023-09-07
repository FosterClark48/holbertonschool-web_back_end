#!/usr/bin/env python3
"""
This module provides a type-annotated function `to_kv` that takes
a string `k` and an int OR float `v` as arguments and returns a tuple.
The first element of the tuple is the string `k`. The second element
is the square of the int/float `v` and should be annotated as a float.

Example:
    >>> to_kv("eggs", 3)
    ('eggs', 9.0)
"""


from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Create a tuple consisting of a str and the square of an int/float.
    """
    return (k, float(v ** 2))
