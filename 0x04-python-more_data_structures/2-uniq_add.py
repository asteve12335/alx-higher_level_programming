#!/usr/bin/python3
def uniq_add(my_list=[]):
    if isinstance(my_list, list):
        uniq = set(my_list)
        sum_uniq = sum(uniq)
        return sum_uniq
