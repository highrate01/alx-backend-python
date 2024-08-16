#!/usr/bin/env python3
"""
This module provides a function to zoom in on a
tuple by repeating its elements.
"""

from typing import List, Tuple


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """
    Create a zoomed in version of the input tuple by
    repeating each element.

    Args:
        lst (Tuple): The input tuple to zoom in on.
        factor (int, optional): The number of times each
        element should be repeated..

    Returns:
        List: A new list with each element from the input tuple
    """
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = [12, 72, 91]

zoom_2x = zoom_array(tuple(array))

zoom_3x = zoom_array(tuple(array), 3)
