#!/usr/bin/python3
""" function to_json_string """


def to_json_string(my_obj):
    import json
    """function that returns the JSON
    representation of an object (string):"""
    return json.dumps(my_obj)
