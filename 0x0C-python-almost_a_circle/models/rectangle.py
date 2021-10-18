#!/usr/bin/python3
""" Class Rectangle"""
from models.base import Base


class Rectangle(Base):
    """ class Rectangle that inherits from Base
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """ initialization"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ getter function"""
        return self.__width

    @property
    def height(self):
        """ getter function"""
        return self.__height

    @property
    def x(self):
        """ getter function"""
        return self.__x

    @property
    def y(self):
        """ getter function"""
        return self.__y

    @height.setter
    def height(self, value):
        """ setter function"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @width.setter
    def width(self, value):
        """ setter function"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @x.setter
    def x(self, value):
        """ setter function"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @y.setter
    def y(self, value):
        """ setter function"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value
