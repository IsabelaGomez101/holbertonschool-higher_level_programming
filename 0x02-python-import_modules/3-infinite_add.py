#!/usr/bin/python3
import sys
sum = 0

if __name__ == "__main__":
    if len(sys.argv) > 1:
        for i in range(1, len(sys.argv)):
            sum += int(sys.argv[i])
    print("{:d}".format(sum))
