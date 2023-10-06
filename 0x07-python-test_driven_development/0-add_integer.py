#!/usr/bin/python3

"""

function that adds 2 integers.

"""
def add_integer(a, b=98):
    """Return the result of the intger calculation

    Args:
        a: the first arg
        b: the second arg
    
    Raises:
        TypeError: if a and b must be integers or floats
    
    Return:
        the sum the two numbers
    """
    
    if ((not isinstance(a, int)) and not isinstance(a, float)):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
