#!/usr/bin/python3

"""Define a class Square"""


class Square:
    """Initializing class Square
    Args:
        size: the size of the square
    """
    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """returns the current square area"""
        return (self.__size ** 2)

    def my_print(self):
        """Print square in hash"""
        if self.__size == 0:
            print()

        for size in range(self.__size):
            print("#" * self.__size)
