#!/usr/bin/python3
"""
Project: 0x07-python-test_driven_development
Task: 4
"""


def print_square(size):
    """
    Function that prints a square with the character #.
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if type(size) is not int and size < 0:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if size == 0:
        print()
    for element in range(size):
        print("#" * size)
