#!/usr/bin/python3
"""
Checks for same class
"""


def is_same_class(obj, a_class):
    if isinstance(obj, a_class):
        return True
    return False
