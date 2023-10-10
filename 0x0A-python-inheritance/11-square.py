#!/usr/bin/python3
"""this module inheritance a Square from Rectangle"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Define a square"""

    def __init__(self, size):
        """Initialize a square"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
