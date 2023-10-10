#!/usr/bin/python3
"""the module define the JSON representation of an object (string)"""
import json


def to_json_string(my_obj):
    """Return the json of the string object"""
    return json.dumps(my_obj)
