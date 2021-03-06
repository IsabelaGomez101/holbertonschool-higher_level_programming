#!/usr/bin/python3
"""
This is module 0-add_integer
function that adds 2 integers.
a and b must be integers or floats.
"""


def add_integer(a, b=98):
    """
    Returns an integer: the addition of a and b.
    """
    if a is None:
        raise TypeError("a must be an integer")
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)
    if type(a) is not int:
        raise TypeError("a must be an integer")
    if type(b) is not int:
        raise TypeError("b must be an integer")
    return a + b
