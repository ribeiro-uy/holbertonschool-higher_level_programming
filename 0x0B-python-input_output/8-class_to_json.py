#!/usr/bin/python3
"""
Project: 0x0B. Python - Input/Output
Task: 8
"""


def class_to_json(obj):
    """
    Function that returns the dictionary description
    with simple data structure (list, dictionary, string,
    integer and boolean) for JSON serialization of an object
    """
    return obj.__dict__
