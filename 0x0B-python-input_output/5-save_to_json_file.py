#!/usr/bin/python3
"""
Project: 0x0B. Python - Input/Output
Task: 5
"""
import json


def save_to_json_file(my_obj, filename):
    """
    Function that writes an Object to a text file, using a JSON representation
    """
    with open(filename, encoding="utf-8", mode="w") as my_file:
        my_file.write(json.dumps(my_obj))
