#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    if isinstance(a_dictionary, dict):
        if key not in list(a_dictionary):
            return a_dictionary
        else:
            del a_dictionary[key]
            return a_dictionary
