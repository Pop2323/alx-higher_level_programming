#!/usr/bin/python3
def no_c(my_string):
    replace_str = ''
    for char in my_string:
        if char != 'c' and char != 'C':
            replace_str += char
        return replace_str
