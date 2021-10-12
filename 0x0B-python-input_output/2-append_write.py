#!/usr/bin/python3
""" function append_write """


def append_write(filename="", text=""):
    """function that appends a string at the end of a text file
    returns the number of characters added"""

    with open(filename, 'a+') as f:
        return f.write(text)
