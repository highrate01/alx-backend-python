#!/usr/bin/env python3
"""Measure the runtime"""
import time
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the total execution time for wait_n
    nd returns the average time per execution.
    Args:
        n (int): Number of times to spawn wait_random in wait_n.
        max_delay (int): Maximum delay value for wait_random in wait_n.
    Returns:
        float: Average time per execution.
    """
    start_time = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.perf_counter()
    return (end_time - start_time) / n
