#!/usr/bin/python3
"""Summation helper for a mixed int/float list."""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Return the sum of a list of ints/floats."""
    return sum(mxd_lst)
