#!/usr/bin/env python3
""" Import async_comprehension from the previous file(2-measure_runtime.py)
    and write a measure_runtime coroutine that will execute async_comprehension
    four times in parallel using asyncio.gather.
    measure_runtime should measure the total runtime and return it.
"""

import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension

async def measure_runtime():
    """ Runtime for four parallel comprehensions """
    s = time.perf_counter()
    await asyncio.gather(async_comprehension(), async_comprehension(),
                         async_comprehension(), async_comprehension())
    elapsed = time.perf_counter() - s
    return elapsed
