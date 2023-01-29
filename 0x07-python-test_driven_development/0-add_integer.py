#!/usr/bin/python3
"""
The following function accepts only int and float
as parameters.
It adds only integers though.
"""
def add_integer(a, b=98):
    """
    a: integer
    b: integer, default value 98
    """
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    if not isinstance(a, int):
        raise TypeError("a, must be an integer")
    if not isinstance(b, int):
        raise TypeError("b must be an integer")
    sum = a + b
    return (sum)
