#!/usr/bin/python3
for first in range(0, 9):
    for second in range(0, 10):
        if first == 8 and second == 9:
            print("{:d}{:d}".format(first, second))
        elif second > first:
            print("{:d}{:d}, ".format(first, second), end="")
