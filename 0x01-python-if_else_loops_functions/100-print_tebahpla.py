#!/usr/bin/python3
if __name__ == "__main__":
    for char in range(ord('z'), ord('a') - 1, -1):
        if char % 2 != 0:
            char = char - 32
        print("{}".format(chr(char)), end="")
