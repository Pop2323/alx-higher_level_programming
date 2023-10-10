#!/usr/bin/python3

""" inherit from rectangle """
from 9-rectangle import Rectangle


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
        self.__size = size
