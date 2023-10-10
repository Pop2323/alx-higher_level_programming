#!/usr/bin/python3
"""module class MyInt that inherits from int"""


class MyInt(int):
    """Change int operators == and !="""

    def __eq__(self, value):
        """Override the equality operator (==) to invert its behavior"""
        return self.real != value

    def __ne__(self, value):
        """Override the inequality operator (!=) to invert its behavior."""
        return self.real == value
