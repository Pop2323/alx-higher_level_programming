#!/usr/bin/python3
for alph in range(ord("a"), ord("z") + 1):
    if chr(alph) != 'e' and chr(alph) != 'q':
        print("{:c}".format(alph), end="")
