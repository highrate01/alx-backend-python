#!/usr/bin/env python3
"""
Contains a function module
"""
from typing import Union, List


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Calculate the sum of a list containing both integers and floats.

    Args:
        mxd_lst (List[Union[int, float]]): A list of integers and floats.

    Returns:
        float: The sum of all numbers in the input list.
    """
    return sum(mxd_lst)
