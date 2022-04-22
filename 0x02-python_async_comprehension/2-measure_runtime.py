#!/usr/bin/env python3

import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension

async def measure_runtime():
    await asyncio.gather(async_comprehension(), async_comprehension(), async_comprehension(), async_comprehension())
    s = time.perf_counter()
    elapsed = time.perf_counter() - s
    return s
