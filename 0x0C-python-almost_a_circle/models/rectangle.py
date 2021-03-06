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

    def update(self, *args, **kwargs):
        """that assigns a key/value argument to attributes"""
        list_attrib = ['id', '_Rectangle__width', '_Rectangle__height',
                       '_Rectangle__x', '_Rectangle__y']
        my_dict = {'id': 'id', 'width': '_Rectangle__width',
                   'height': '_Rectangle__height', 'x': '_Rectangle__x',
                   'y': '_Rectangle__y'}
        for i in range(0, len(args)):
            self.__dict__[list_attrib[i]] = args[i]
        if len(args) == 0:
            for key, value in kwargs.items():
                self.__dict__[my_dict[key]] = value

    def area(self):
        """returns the area value of the Rectangle instance"""
        return self.__width * self.__height

    def display(self):
        """that prints in stdout the Rectangle instance
        with the character #"""
        print("\n" * self.__y, end="")
        string = (" " * self.__x) + ("#" * self.__width) + "\n"
        string = string * (self.__height - 1)
        string = string + (" " * self.__x) + ("#" * self.__width)
        print(string)

    def __str__(self):
        return("[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
               self.__x, self.__y, self.__width, self.__height))

    def to_dictionary(self):
        """that returns the dictionary representation of a Rectangle"""
        return {'id': self.id, 'width': self.__width, 'height': self.__height,
                'x': self.__x, 'y': self.__y}
