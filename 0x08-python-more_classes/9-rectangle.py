#!/usr/bin/python3


"""define the calss Rectangle"""


class Rectangle:
    """represent Rectangle"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialize the instance with optional width and height
        Args:
            width: represent the rectangle width
            height: represent the rectangle width
        Raises:
            TypeError: if width and height is not integer
            ValueError: if width and height less than zero
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Define the property for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Define the setter for width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Define the property for width"""
        return self.__height

    @height.setter
    def height(self, value):
        """Define the setter for height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """return the rectangle area"""
        return (self.__width * self.__height)

    def perimeter(self):
        """return the  rectangle perimeter"""
        if self.__width == 0 or self.__height == 0:
            return (0)
        else:
            return 2 * (self.__width + self.__height)

    def __str__(self) -> str:
        if self.__width == 0 or self.__height == 0:
            return ""
        else:
            shape = ""
            for h in range(self.__height):
                for w in range(self.__width):
                    try:
                        shape += str(self.print_symbol)
                    except TypeError:
                        shape += type(self.print_symbol).__name__
                if h < self.__height -1:
                    shape += "\n"
            return shape

    def __repr__(self):
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        return(size, size)
