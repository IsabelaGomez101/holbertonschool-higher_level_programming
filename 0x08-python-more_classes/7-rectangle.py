#!/usr/bin/python3
""" class Square that defines a Rentangle"""


class Rectangle:
    """Public class attribute"""
    number_of_instances = 0
    print_symbol = "#"
    """Private instance attribute width"""
    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        """Define the method to get the height"""
        if isinstance(value, int) is False:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        """Define the method to get the width"""
        if isinstance(value, int) is False:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    def area(self):
        return self.__width*self.__height

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (self.__width*2)+(self.__height*2)

    def __str__(self) -> str:
        symbol = Rectangle.print_symbol
        if self.__width == 0 or self.__height == 0:
            return ""
        else:
            string = (symbol * self.__width) + "\n"
            string = string * (self.__height - 1)
            string = string + (symbol * self.__width)
            return string

    def __repr__(self) -> str:
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
