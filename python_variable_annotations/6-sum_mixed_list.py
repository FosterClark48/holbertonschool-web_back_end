#!/usr/bin/env python3
"""
This module provides a type-annotated function `sum_mixed_list` which
takes a list `mxd_lst` of integers and floats and
returns their sum as a float.

Example:
    >>> sum_mixed_list([1, 2.0, 3])
    6.0
"""


from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """ Calculate the sum of a list containing integers and floats. """
    return sum(mxd_lst)
