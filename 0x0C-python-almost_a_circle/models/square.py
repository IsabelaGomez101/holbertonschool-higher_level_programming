#!/usr/bin/python3
""" Class Square"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """class Square that inherits from Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """ initialization"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """ getter function"""
        return self.width

    @size.setter
    def size(self, value):
        """ setter function"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """that assigns a key/value argument to attributes"""
        if len(args):
            for i in range(0, len(args)):
                if i == 0:
                    self.id = args[i]
                if i == 1:
                    self.size = args[i]
                if i == 2:
                    self.x = args[i]
                if i == 3:
                    self.y = args[i]
        if len(args) == 0:
            for key, value in kwargs.items():
                if hasattr(self, key) is True:
                    setattr(self, key, value)

    def __str__(self):
        return("[Square] ({}) {}/{} - {}".format(self.id,
               self.x, self.y, self.width))
