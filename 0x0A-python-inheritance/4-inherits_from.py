#!/usr/bin/python3
"""
Project: 0x0A-python-inheritance.
Task: 4
"""


def inherits_from(obj, a_class):
    """
    Function that returns True if the object is an instance of a class
    that inherited (directly or indirectly) from the specified class;
    otherwise False.
    """

    if issubclass (obj, a_class):
        if type(obj) == a_class
            return False
        else:
            return True
