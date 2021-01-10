#!/usr/bin/python3
"""
Project: 0x07-python-test_driven_development
Task: 2
"""


def say_my_name(first_name, last_name=""):
    """
    Function that prints My name is <first name> <last name>
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is {:s} {:s}".format(first_name, last_name))
