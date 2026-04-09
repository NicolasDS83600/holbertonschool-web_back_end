#!/usr/bin/env python3
"""Provide lengths for each string in a list."""
from typing import List, Tuple


def element_length(lst: List[str]) -> List[Tuple[str, int]]:
    """Return pairs of string and its length."""
    return [(i, len(i)) for i in lst]
