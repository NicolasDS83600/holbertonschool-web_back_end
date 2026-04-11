#!/usr/bin/env python3
"""Provide lengths for each string in a list."""

from typing import List, Tuple, Iterable, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Return pairs of string and its length."""
    return [(i, len(i)) for i in lst]
