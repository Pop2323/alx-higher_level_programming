#!/usr/bin/python3
"""module class MyInt that inherits from int"""


class MyInt(int):
    def __eq__(self, value):
        return self.other != value

    def __ne__(self, value):
        return self.other == value
