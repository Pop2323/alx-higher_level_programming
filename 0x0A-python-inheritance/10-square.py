#!/usr/bin/python3

# Import the Rectangle class from the correct module
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Define the square"""
        def __init__(self, size):
        """Initialize a new square
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
