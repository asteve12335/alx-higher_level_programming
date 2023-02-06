#!/usr/bin/python3
"""
Get the list of methods of an obj
"""


def lookup(obj):
    """
    Returns list of available attributes and methods:
    """
    return dir(obj)
