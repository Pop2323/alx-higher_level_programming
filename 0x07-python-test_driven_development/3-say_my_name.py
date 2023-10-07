#!/usr/bin/python3
""""

This module contains a function that prints the 1st and 2nd name

"""


def say_my_name(first_name, last_name=""):
    '''This function prints name (first name + last name)

    Args:
        first_name : The fisrt name to be printed should be str
        last_name : The last name to be printed should be str
    Raises:
        TypeError: If either the first_name and last_name are not strings
    Return:
        return the first name and last name

    '''

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print(f"My name is {first_name} {last_name}")
