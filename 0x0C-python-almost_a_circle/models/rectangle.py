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
        return self.__width

    @property
    def height(self):
        return self.__height

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @height.setter
    def height(self, value):
        """ setter function"""
        self.__height = value

    @width.setter
    def width(self, value):
        """ setter function"""
        self.__width = value

    @x.setter
    def x(self, value):
        """ setter function"""
        self.__x = value

    @y.setter
    def y(self, value):
        """ setter function"""
        self.__y = value
