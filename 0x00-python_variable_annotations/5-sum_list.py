#!/usr/bin/env python3
from re import X
from typing import List
"""returns sum of list elements"""


def sum_list(input_list: List[float]) -> float:
    """
    arguments:
        input_list - list of floats
    returns: sum of elements as float
    """

    length = len(input_list)
    sumOfList = 0
    for i in range(length):
        sumOfList += input_list[i]
    return sumOfList
