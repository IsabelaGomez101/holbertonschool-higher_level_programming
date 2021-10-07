#!/usr/bin/python3
"""
This is module 4-print_square
function that prints a square with the character #.
size must be an integer
"""


def text_indentation(text):
    """
    function that prints a square with the character #.
    """
    a = 0
    if type(text) is not str:
        raise TypeError("text must be a string")
    text = text.strip()
    for i in range(0, len(text)):
        if a == 1 and text[i] == " ":
            a = 0
        else:
            if text[i] == " " and text[i - 1] == " ":
                ()
            else:
                print("{:s}".format(text[i]), end="")
        if text[i] == "." or text[i] == "?" or text[i] == ":":
            a = 1
            print("\n")
