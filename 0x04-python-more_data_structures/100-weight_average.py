#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list is None or my_list == []:
        return 0
    set1 = 0
    set2 = 0
    for x, y in my_list:
        set1 += (x * y)
        set2 += y
    return set1 / set2
