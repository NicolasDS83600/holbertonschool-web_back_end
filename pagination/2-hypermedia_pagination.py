#!/usr/bin/env python3
"""Simple pagination server for baby names dataset."""

import csv
import math
from typing import List, Dict


def index_range(page, page_size):
    """Return start and end indices for paginated dataset."""
    start_index = (page - 1) * page_size
    end_index = page * page_size
    return (start_index, end_index)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Return paginated data for given page and page size."""
        assert isinstance(page, int)
        assert page > 0
        assert isinstance(page_size, int)
        assert page_size > 0

        data = self.dataset()
        start, end = index_range(page, page_size)

        return data[start:end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """Return hypermedia pagination info for given page and size."""
        data = self.get_page(page, page_size)
        dataset = self.dataset()
        total_items = len(dataset)
        total_pages = math.ceil(total_items / page_size)

        if page > 1:
            prev_page = page - 1
        else:
            prev_page = None

        if page < total_pages:
            next_page = page + 1
        else:
            next_page = None

        result = {
            "page_size": page_size,
            "page": page,
            "data": data,
            "next_page": next_page,
            "prev_page": prev_page,
            "total_pages": total_pages
        }

        return result
