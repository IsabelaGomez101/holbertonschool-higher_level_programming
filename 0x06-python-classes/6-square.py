#!/usr/bin/python3
""" class Square that defines a square """


class Square:
    """Private instance attribute size"""
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

    @property
    def size(self):
        return self.__size

    @property
    def position(self):
        return self.__position

    @size.setter
    def size(self, size):
        """Define the method to get the size"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    @position.setter
    def position(self, position):
        """Define the method to get the position"""
        if (type(position) is not tuple or
            all(isinstance(num, int) for num in position) is False or
            len(position) != 2 or
                all((num < 0) for num in position) is True):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = position

    def area(self):
            """calculate the area of a square"""
            return self.__size * self.__size

    def my_print(self):
        if self.__size == 0:
            print("")
        else:
            if self.__position[1] > 0:
                print("\n" * self.__position[1], end="")
            for i in range(0, self.__size):
                if self.__position[0] > 0 or self.__position[1] <= 0:
                    print("_" * self.__position[0], end="")
                    print("#" * self.__size)
