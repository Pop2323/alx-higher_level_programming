#!/usr/bin/python3
"""Adds all arguments to a Python list and then saves them to a file"""
import sys
from import_json import save_to_json_file, load_from_json_file


if __name__ == "__main":
    try:
        items = load_from_json_file("add_item.json")
    except FileNotFoundError:
        items = []

    items.extend(sys.argv[1:])

    save_to_json_file(items, "add_item.json")
