#!/usr/bin/python3
""" function read_file """


def read_file(filename=""):
    """ function that reads a text file and prints it to stdout"""
    with open(filename) as f:
        for line in f:
            print(line, end="")
        print("")
