#!/usr/bin/python3
""" class Square that defines a square """


class Square:
    """Private instance attribute size"""
    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        """Define the method to get the size"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
            """calculate the area of a square"""
            return self.__size * self.__size
