#!/usr/bin/python3
"""the module define an object (Python data structure)
    represented by a JSON string
"""
import json


def from_json_string(my_str):
    """Return the json object of the json string"""
    return json.loads(my_str)
