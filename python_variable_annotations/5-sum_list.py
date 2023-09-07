#!/usr/bin/env python3
"""
This module provides a type-annotated function `sum_list` which
takes a list `input_list` of floats as argument and returns their
sum as a float.

Example:
    >>> sum_list([1.0, 2.0, 3.0])
    6.0
"""


from typing import List


def sum_list(input_list: List[float]) -> float:
    """ Calculate the sum of a list of floats. """
    return sum(input_list)
