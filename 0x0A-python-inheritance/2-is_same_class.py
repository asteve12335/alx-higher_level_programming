#!/usr/bin/python3
"""
Same class check
"""


def is_kind_of_class(obj, a_class):
    """
    Check for same class.
    Args:
        obj (any): The object to check.
        a_class (type): The class to match the type of obj to.
    Returns:
        If type(obj) is a_class - True.
        Otherwise - False.
    """
    if type(obj) == a_class:
        return True
    return False
