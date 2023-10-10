#!/usr/bin/python3
"""This module define a text file (UTF8) and prints it to stdout"""


def read_file(filename=""):
    """print the contant of the filename"""
    with open(filename, encoding="UTF8") as f:
        print(f.read, end="")
