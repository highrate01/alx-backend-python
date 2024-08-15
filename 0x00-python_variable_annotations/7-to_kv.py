#!/usr/bin/env python3
"""Conatins a function module"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
     Create a tuple from a string and the square of an int or float.

    Args:
        k (str): first element of the turple
        v (Union[int, float]): second element of the tuple.

    Returns:
        Tuple[str,float]: A tuple
    """
    return (k, v * v)
