#!/usr/bin/python3

"""module class MyInt that inherits from int"""


class MyInt(int):
    def __eq__(self, value):
        """Override the equality operator (==) to invert its behavior"""
        return super().__ne__(value)

    def __ne__(self, value):
        """Override the inequality operator (!=) to invert its behavioe"""
        return super().__eq__(value)

