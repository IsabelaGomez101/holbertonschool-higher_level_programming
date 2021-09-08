#!/usr/bin/python3
import sys

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("0 arguments.")
    elif len(sys.argv) == 2:
        print(len(sys.argv) - 1, "argument:")
        print("1:", sys.argv[1])
    else:
        print(len(sys.argv) - 1, "arguments:")
        for i in range(1, len(sys.argv)):
            print("{:d}: {:s}".format(i, sys.argv[i]))
