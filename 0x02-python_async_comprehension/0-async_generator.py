#!/usr/bin/env python3
"""Async Generator"""

import asyncio

async def async_generator():
    """coroutine will loop 10 times,
    each time asynchronously wait 1 second,
    then yield a random number between 0 and 10.
    
    Keyword arguments:
    argument -- takes no argument
    Return: return nothing
    """
    
    for i in range(10):
        await asyncio.sleep(1)
        import random
        yield random.uniform(0.0, 10.0)

# print(__import__("0-async_generator").async_generator.__doc__)
