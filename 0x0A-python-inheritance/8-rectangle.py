#!/usr/bin/python3
"""
Project: 0x0A-python-inheritance.
Task: 8
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    New class Rectangle that inherits from BaseGeometry (7-base_geometry.py).
    """

    def __init__(self, width, height):
        """
        Constructor
        """
        self.__width = width
        self.__height = height
        if super().integer_validator("width", self.__width)
        if super().integer_validator("height", self.__height)
