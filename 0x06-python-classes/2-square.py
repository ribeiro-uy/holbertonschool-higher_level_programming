#!/usr/bin/python3
"""
A class Square that defines a square by: (based on 0-square.py)
"""


class Square:
    """
    A class Square
    """
    def __init__(self, size=0):
        """
        Args:
        size (int): Size of square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an interger")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
