#!/usr/bin/env python3
"""Async Comprehension"""

import asyncio
from typing import List

async_generator = __import__('0-async_generator').async_generator

async def async_comprehension() -> List[float]:
    """coroutine will collect 10 random numbers
    using an async comprehensing over async_generator
    
    Keyword arguments:
    argument -- takes no argument
    Return: return the 10 random floating numbers
    """
    
    randNum = [i async for i in async_generator()]
    return randNum
