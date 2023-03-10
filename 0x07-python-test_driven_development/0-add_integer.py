#!/usr/bin/python3
"""Defines an integer addition function."""


def add_integer(a, b=98):
    """
    a: integer
    b: integer, default value 98
    """

    if type(a) not in (int, float):
        raise TypeError("a, must be an integer")
    elif type(b) not in (int, float):
        raise TypeError("b must be an integer")
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    sum = a + b
    return (sum)
