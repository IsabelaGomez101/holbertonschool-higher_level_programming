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

    @classmethod
    def save_to_file(cls, list_objs):
        """that writes the JSON string representation of list_objs to a file"""
        import json
        my_dict = []
        if list_objs is not None:
            for obj in list_objs:
                temp = cls.to_dictionary(obj)
                my_dict.append(temp)
        string = cls.to_json_string(my_dict)
        filename = cls.__name__ + ".json"
        with open(filename, 'w') as f:
            f.write(string)

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation json_string"""
        import json
        if json_string is None:
            return []
        else:
            return json.loads(json_string)
