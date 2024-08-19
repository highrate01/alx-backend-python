#!/usr/bin/env python3
"""Tasks"""
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Creates and returns an asyncio Task that runs wait_random.

    Args:
        max_delay (int): The maximum delay value for wait_random.

    Returns:
        asyncio.Task: A Task object that runs wait_random.
    """
    return asyncio.create_task(wait_random(max_delay))
