#!/usr/bin/python3

"""Define a class Square"""


class Square:
    """this defines a sqr by its size and position."""

    def __init__(self, size=0, position=(0, 0)):
        """Initializer with optional size and position.

        Args:
            size (int): The size of the square. Defaults to 0.
        """

        # Validate the size attribute.
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        # Validate the position attribute.
        if not isinstance(position, tuple) or len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if position[0] < 0 or position[1] < 0:
            raise ValueError("position must be a tuple of 2 positive integers")

        # Set the private instance attributes.
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """Returns the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size of the square.

        Args:
            value (int): The new size of the square.
        """

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    @property
    def position(self):
        """Returns the position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        """Sets the position of the square."""

        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise ValueError("position must be a tuple of 2 positive integers")

        self.__position = value

    def area(self):
        """Returns the area of the square."""
        return self.__size ** 2

    def my_print(self):
        """Prints the square to stdout using the character '#'.

        If the size of the square is equal to 0, an empty line is printed.
        """

        if self.__size == 0:
            print()
        else:
            for y in range(self.__position[1]):
                print()
            for y in range(self.__size):
                for x in range(self.__position[0]):
                    print(" ", end="")
                for x in range(self.__size):
                    print("#", end="")
                print()
