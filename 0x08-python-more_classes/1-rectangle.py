#!/usr/bin/python3

"""define the class Rectangle"""


class Rectangle:
    """represent Rectangle"""
    def __init__(self, width=0, height=0):
        """Initialize the instance with optional width and height
        Args:
            width: represent the rectangle width
            height: represent the rectangle width
        Raises:
            TypeError: if width and height are not integers
            ValueError: if width and height are less than zero
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Define the property for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Define the setter for width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Define the property for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Define the setter for height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

