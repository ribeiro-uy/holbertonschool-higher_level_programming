#!/usr/bin/python3
"""
Project: 0x0B. Python - Input/Output
Task: 4
"""
import json


def from_json_string(my_str):
    """
    Function that returns an object (Python data structure) represented by a JSON string
    """
    return json.loads(my_str)
