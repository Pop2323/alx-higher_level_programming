#!/usr/bin/python3
"""math module"""
import math


class MagicClass:
    """Declare MagicClass"""

    def __init__(self, radius=0):
        """Initialize a MagicClass.

        Arg:
            radius (type(int or float)): The radius of the MagicClass.
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """Public instance method to calculate the area"""
        return (self.__radius ** 2 * math.pi)

    def circumference(self):
        """return the circum"""
        return (2 * math.pi * self.__radius)
