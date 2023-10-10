#!/usr/bin/python3


""" Define a base geometry class BaseGeometry"""


class BaseGeometry:
    def area(self):
        """
        Raises an Exception with the message "area() is not implemented."
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validate that a value is an integer and greater than 0.
        Args:
        name (str): The name of the value (a string).
        value: The value to validate.
        Raises:
        - TypeError: If the value is not an integer.
        - ValueError: If the value is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
