#!/usr/bin/env python3
"""Async Comprehensionsi"""
from importlib import import_module as using
from typing import List
async_generator = using('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    An asynchronous coroutine that collects 10 random numbers using an async
    comprehension over async_generator.

    Returns:
        List[float]: A list of 10 random numbers.
    """
    random_numbers = [num async for num in async_generator()]
    return random_numbers
