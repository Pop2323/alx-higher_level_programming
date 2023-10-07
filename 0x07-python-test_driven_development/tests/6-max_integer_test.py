#!/usr/bin/python3
"""
    Module to find the max int in a list
"""


def max_integer(list=[]):
    """
        Function to find and return the max int in a list of integers
        If the list is empty, the function will return None
    """
    if len(list) == 0:
        return None
    res = list[0]
    n = 1
    while n < len(list):
        if list[n] > res:
            res = list[n]
        n += 1
    return res
