#!/usr/bin/python3
"""This module inherits a square from rectangle"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Define a square"""

    def __init__(self, size):
        """Initialize a new square"""
        super().integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

