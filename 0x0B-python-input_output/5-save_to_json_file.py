#!/usr/bin/python3
""" function save_to_json_file """


def save_to_json_file(my_obj, filename):
    """function that writes an Object to a text file
    using a JSON representation:"""
    import json
    with open(filename, 'a+') as f:
        return json.dump(my_obj, f)
