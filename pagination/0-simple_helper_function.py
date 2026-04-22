#!/usr/bin/env python3
"""Pagination helper module for calculating page indices."""


def index_range(page, page_size):
    """Return start and end indices for paginated dataset."""
    start_index = (page - 1) * page_size
    end_index = page * page_size
    return (start_index, end_index)
