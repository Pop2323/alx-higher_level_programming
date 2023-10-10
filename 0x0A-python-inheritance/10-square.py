#!/usr/bin/python3

""" inherit from rectangle """
Rectangle = __import__('9-rectangle.py').Rectangle


class Square(Rectangle):
    """Define the square"""
    def __init__(self, size):
        """Intialize new square"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        size.__size = size
