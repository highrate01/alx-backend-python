#!/usr/bin/env python3
"""
Contains a function module
"""
from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Defines a function that returns the first element of
    a sequence if it exists, otherwise returns None.

    Args:
        lst (Sequence[Any]): A sequence of elements of any type.

    Returns:
        Optional[Any]: The first element of the sequence if it exists,
        otherwise None.
    """
    if lst:
        return lst[0]
    else:
        return None
