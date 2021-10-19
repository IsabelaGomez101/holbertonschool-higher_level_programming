#!/usr/bin/python3
""" Class Base"""


class Base:
    """ Class Base
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """ initialize Base """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries"""
        import json
        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries, sort_keys=True)
