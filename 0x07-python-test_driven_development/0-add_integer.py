#!/usr/bin/python3
"""
Project: 0x07-python-test_driven_development
Task: 0
"""


def add_integer(a, b=98):
    """
    Function that adds 2 integers.
    """
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    if a+1 == a:
        raise OverflowError("cannot convert float infinity to integer")
    if b+1 == b:
        raise OverflowError("cannot convert float infinity to integer")
    return int(a) + int(b)
