#!/usr/bin/env python3
"""
Annotate the below functions parameters and return values with
the appropriate types.

def element_length(lst):
    return [(i, len(i)) for i in lst]
"""


from typing import List, Tuple, Sequence, Iterable


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """ Find the length of the element """
    return [(i, len(i)) for i in lst]
