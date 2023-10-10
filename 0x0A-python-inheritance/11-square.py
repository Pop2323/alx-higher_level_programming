#!/usr/bin/python3

"""inherit from rectangle"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Define the square"""
    def __init__(self, size):
        """
        Initialize a Square with a given size.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
