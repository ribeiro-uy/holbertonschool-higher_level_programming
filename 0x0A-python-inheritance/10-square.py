#!/usr/bin/python3
"""
Project: 0x0A-python-inheritance.
Task: 10
"""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """
    Square that inherits from Rectangle (9-rectangle.py):
    """

    def __init__(self, size):
        """
        Constructor
        """
        self.__size = size
        super().integer_validator("size", self.__size)
        super().__init__(size, size)

    def area(self):
        """
        Area of the Square
        """
        return self.__size * self.__size
