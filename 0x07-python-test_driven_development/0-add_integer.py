#!/usr/bin/python3
"""
This module contains
the addition
of two intergers
"""


def add_integer(a, b=98):
    """
    to add two intergers
    """
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(a) is bool:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    if type(b) is bool:
        raise TypeError("b must be an integer")
    if a+1 == a:
        raise OverflowError("cannot convert float infinity to integer")
    if b+1 == b:
        raise OverflowError("b is too big")
    
    #cast a and b into intergers
    a = int(a)
    b = int(b)
    try:
        return a + b
    except SyntaxError:
        raise SyntaxError("cualca")
