#!/usr/bin/python3
"""
Project: 0x09-python-everything_is_object
Task: 31
"""


class LockedClass:
    """
    A class LockedClass with no class or object attribute, that prevents the
    user from dynamically creating new instance attributes, except if the new
    instance attribute is called first_name.
    """
    __slots__ = ['first_name']
