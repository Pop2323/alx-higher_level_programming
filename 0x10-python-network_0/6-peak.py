#!/usr/bin/python3
def find_peak(list_of_integers):
    lenght = len(list_of_integers)
    mid = lenght
    middle = lenght // 2
    
    if lenght == 0:
        return None
    
    while True:
        mid = mid // 2
        
    