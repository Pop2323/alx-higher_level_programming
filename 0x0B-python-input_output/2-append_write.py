#!/usr/bin/python3
"""
    This module define  a text file (UTF8) and returns
    the number of characters added
"""


def append_write(filename="", text=""):
    """Append a string inside the text file"""
    with open(filename, "a", encoding="UTF8") as f:
        return f.write(text)
