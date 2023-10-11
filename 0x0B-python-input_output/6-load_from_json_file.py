#!/usr/bin/python3
"""This module define an Object from a “JSON file”"""

import json


def load_from_json_file(filename):
    """Define an object from json file"""
    with open(filename) as f:
        return json.load(f)
