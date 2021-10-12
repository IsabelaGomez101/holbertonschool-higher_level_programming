#!/usr/bin/python3
""" class BaseGeometry"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ class Square"""
    def __init__(self, size):
        self.__size = size
        super().__init__(self.__size, self.__size)

    def __str__(self):
        return ("[Square] {}/{}".format(self.__size, self.__size))
