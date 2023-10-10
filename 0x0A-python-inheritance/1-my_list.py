#!/usr/bin/python3
"""This module inherits from list class"""


class MyList(list):
    """ class MyList that inherits from list"""
    def print_sorted(self):
        """print the sorted list"""
        print(sorted(self))
