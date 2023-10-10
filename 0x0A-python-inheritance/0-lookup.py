#!/usr/bin/python3

"""
    This func return the list of the avaliable and method of an object
"""


def lookup(obj):
    """function that returns the list of available attributes and methods of an object"""
    print(dir(obj))
