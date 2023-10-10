#!/usr/bin/python3
"""
    This module define a text file (UTF8) and returns 
    the number of characters written
"""
def write_file(filename="", text=""):
    """writes a string inside a text file"""
    with open(filename, "w", encoding="UTF8") as f:
        return f.write(text)
