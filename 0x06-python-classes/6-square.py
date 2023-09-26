class Square:
    """A Square class that defines a square by its size and position."""

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

        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(n, int) for n in value) or
                not all(n >= 0 for n in value)):
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__position = value

    def area(self):
        """Returns the area of the square."""
        return self.__size ** 2


    def print_res(self):
        """returns the square as a string with position"""
        result = ""

        if self.size == 0:
            return "\n"

        for row in range(self.size + self.position[1]):
            if row < self.position[1]:
                result += "\n"
            else:
                result += " " * self.position[0] + "#" * self.size + "\n"

        return result

    def my_print(self):
        """print the square in position"""
        print(self.print_res(), end='')
