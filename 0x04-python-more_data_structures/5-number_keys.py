#!/usr/bin/python3
def number_keys(a_dictionary):
    if isinstance(a_dictionary, dict):
        key_list = list(a_dictionary)
        return len(key_list)
