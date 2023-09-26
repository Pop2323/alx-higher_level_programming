#!/usr/bin/python3

"""Define a class Square"""


class Square:
    """Define a class Square"""

    def __init__(self, size=0, position=(0, 0)):
        """Initializing class Square
        Args:
            size: the size of the square
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """The size of the square"""
        return(self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        return (self._position)

    @position.setter
    def position(self, value):
        """Setter method for position"""
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(n, int) for n in value) or
                not all(n >= 0 for n in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Public instance method to calculate the area"""
        return (self.__size ** 2)

    def my_print(self):
        """Public instance method to print the square"""
        if self.__size == 0:
            print("")
            return

        [print("") for n in range(0, self.__position[1])]
        for n in range(0, self.__size):
            [print(" ", end="") for p in range(0, self.__position[0])]
            [print("#", end="") for s in range(0, self.__size)]
            print("")

