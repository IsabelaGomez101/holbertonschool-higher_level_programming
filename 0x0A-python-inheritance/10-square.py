#!/usr/bin/python3
""" class BaseGeometry"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ class Square"""
    def __init__(self, size):
        self.__size = size
        self.integer_validator("size", self.__size)
        super().__init__(self.__size, self.__size)
