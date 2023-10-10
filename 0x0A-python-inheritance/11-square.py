#!/usr/bin/python3

""" inherit from rectangle """
Rectangle = __import__('9-rectangle.py').Rectangle


class Square(Rectangle):

    """Define the square"""
    def __init__(self, size):
        """
        Initialize a Square with a given size.
        Args:
        size (int): The size of the square.
        Raises:
        - TypeError: If size is not an integer.
        - ValueError: If size is not a positive integer.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        size.__size = size
