#!/usr/bin/python3
"""
This is module 4-print_square
function that prints a square with the character #.
size must be an integer
"""


def print_square(size):
    """
    function that prints a square with the character #.
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(0, size):
        for n in range(0, size):
            print("#", end="")
        print("")
