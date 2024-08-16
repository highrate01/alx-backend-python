#!/usr/bin/env python3
"""
Contains a function module
"""
from typing import Mapping, Any, Optional, TypeVar

T = TypeVar('T')


def safely_get_value(dct: Mapping[Any, T], key: Any,
                     default: Optional[T] = None) -> Optional[T]:
    """
    Safely retrieves a value from a dictionary using a key,
    or returns a default value.

    Args:
        dct (Mapping[Any, T]): A dictionary with keys of any type and
                                values of a generic type T.
        key (Any): The key used to retrieve the value from the dictionary.
        default (Optional[T], optional): The default value to return
                                         if the key is not found.
                                         Defaults to None.

    Returns:
        Optional[T]: The value associated with the key if found,
                     otherwise the default value.
    """
    if key in dct:
        return dct[key]
    else:
        return default
