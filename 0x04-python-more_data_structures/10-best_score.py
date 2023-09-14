#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None or a_dictionary == {}:
        return None
    biggest_int = max(a_dictionary.values())
    for k, val in a_dictionary.items():
        if val is biggest_int:
            return k
