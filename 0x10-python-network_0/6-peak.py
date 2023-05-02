#!/usr/bin/python3
"""
a function that finds a peak in a list of unsorted integers.
"""
def find_peak(list_of_integers):
    """
    returns a peak in a list of unsorted integers.
    """
    p = None
    if len(list_of_integers) == 0:
        return p
    else:
        p = list_of_integers[0]
        for x in list_of_integers:
            if p <= x:
                p = x
    return p
