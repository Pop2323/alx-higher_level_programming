#!/usr/bin/python3
"""this module inheritane a square from rectangle"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Define a square"""

    def __init__(self, size):
        """Initial a new square"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
