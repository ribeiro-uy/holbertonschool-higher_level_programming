#!/usr/bin/python3
"""
Project: 0x0A-python-inheritance
Task: 2
"""

def is_same_class(obj, a_class):
    """
    Function that returns True if the object is exactly
    an instance of the specified class; otherwise False.
    """

    if type(obj) == a_class:
        return True
    else:
        return False
