#!/usr/bin/python3
"""
Project: 0x0A-python-inheritance
Task: 3
"""


def is_kind_of_class(obj, a_class):
    """
    Function that returns True if the object is an instance of,
    or if the object is an instance of a class that inherited from,
    the specified class; otherwise False.
    """

    if isinstance(obj, a_class):
        return True
    else:
        return False
