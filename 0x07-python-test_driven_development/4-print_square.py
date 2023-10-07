#!/usr/bin/python3


"""
    function that prints a square with the character #.
"""


def print_square(size):
    """This function prints a square with the character #
    Args:
        size (int): This represents the length of the square
    Raises:
        TypeError: If size is not an integer
        ValueError: If size is less than zero
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    for i in range(0, size):
        for j in range(size):
            print("#", end="")
        print("")
