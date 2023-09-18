#!/usr/bin/env python3
"""
This module contains a function index_range that calculates the start and
end index for pagination based on the page number and items per page.
"""


def index_range(page: int, page_size: int) -> tuple:
    """
    Calculate start and end index for pagination

    Params:
    - page (int): The current page number
    - page_size (int): the number of items per page.

    Returns:
    - tuple: A tuple containing the start index and end index for pagination.
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return start_index, end_index
