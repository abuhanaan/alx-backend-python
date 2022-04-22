#!/usr/bin/env python3
"""Async Comprehension"""

import asyncio

async_generator = __import__('0-async_generator').async_generator

async def async_comprehension():
    """coroutine will collect 10 random numbers
    using an async comprehensing over async_generator
    
    Keyword arguments:
    argument -- takes no argument
    Return: return the 10 random floating numbers
    """
    
    randNum = []
    async for i in async_generator():
        randNum.append(i)
    return randNum
