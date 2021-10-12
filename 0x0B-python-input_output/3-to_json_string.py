#!/usr/bin/python3
""" function to_json_string """


def to_json_string(my_obj):
    """function that returns the JSON
    representation of an object (string):"""
    import json
    return json.dumps(my_obj, sort_keys=True)
