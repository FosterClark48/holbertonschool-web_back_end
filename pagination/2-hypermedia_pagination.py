#!/usr/bin/env python3
"""
This module provides functionalities for hypermedia pagination
of a database of popular baby names stored in a CSV file.
"""

import csv
import math
from typing import List, Dict, Any


def index_range(page: int, page_size: int) -> tuple:
    """Calculate start and end index for pagination"""
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return start_index, end_index


class Server:
    """
    Server class to paginate and provide hypermedia infos in a
    database of popular baby names
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Return the dataset, loading it if needed"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Return a page of the dataset"""
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        start_index, end_index = index_range(page, page_size)
        return self.dataset()[start_index:end_index]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[str, Any]:
        """Return a dictionary containing hypermedia pagination info"""
        total_data = len(self.dataset())
        total_pages = math.ceil(total_data / page_size)
        data = self.get_page(page, page_size)
        page_data_len = len(data)

        next_page = page + 1 if page < total_pages else None
        prev_page = page - 1 if page > 1 else None

        hyper = {
            "page_size": page_data_len,
            "page": page,
            "data": data,
            "next_page": next_page,
            "prev_page": prev_page,
            "total_pages": total_pages
        }

        return hyper
