#!/usr/bin/python3
"""
Project: 0x0A-python-inheritance.
Task: 8
"""


class BaseGeometry:
    """
    Based on 7-base_geometry.py
    """

    def area(self):
        """
        Public instance method: def area(self):
        that raises an Exception with the message area() is not implemented.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Public instance method: def integer_validator(self, name, value):
        that validates value.
        """
        if not isinstance(value, int):
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """
    New class Rectangle that inherits from BaseGeometry (7-base_geometry.py).
    """

    def __init__(self, width, height):
        """
        Constructor
        """
        super().integer_validator("width", self.__width)
        super().integer_validator("height", self.__height)
        self.__width = width
        self.__height = height
