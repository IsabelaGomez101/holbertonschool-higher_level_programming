#!/usr/bin/python3
""" Class Student module"""


class Student:
    """ Student
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ method that retrieves a dictionary representation of
        a Student instance"""
        if type(attrs) is list:
            my_dict = {}
            for i in attrs:
                if i in self.__dict__:
                    my_dict[i] = self.__dict__[i]
            return my_dict
        return self.__dict__
