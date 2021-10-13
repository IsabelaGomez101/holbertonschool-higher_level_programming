#!/usr/bin/python3
""" class BaseGeometry"""


Rectangle = __import__('9-rectangle').Rectangle


class Rectangle(BaseGeometry):
    """ class Rectangle that inherits from BaseGeometry """
    def __init__(self, width, height):
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height
