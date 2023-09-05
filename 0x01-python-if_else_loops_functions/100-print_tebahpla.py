#!/usr/bin/python3
for alph in range(ord("z"), ord("a") - 1, -1):
    if alph % 2 == 0:
        char = 0
    else:
        char = 32
    print("{}".format(chr(alph - char)), end="")
