#!/usr/bin/env python3
"""
Contains a function module
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Multiplies a float by multiplier.
    Args:
        multiplier (float): Represents the value to be multiplied.
    Returns:
        Callable[[float], float]: A function that returns a float.
    """
    def multiplies(n: float) -> float:
        """
        Multiplies two numbers.
        """
        return n * multiplier

    return multiplies
