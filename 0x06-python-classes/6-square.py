#!/usr/bin/python3
"""
A class Square that defines a square by: (based on 5-square.py)
"""


class Square:
    """
    A class Square
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        Constructor

        Args:
        size (int): Size of square
        position (tuple): square position
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """
        Getter the size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter the size
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """
        Getter the position
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Setter the position
        """
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not isinstance(value[0], int) or not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Returns the current square area
        """
        return self.__size * self.__size

    def my_print(self):
        """
        Prints in stdout the square with the character #
        """
        print('{}'.format('\n' * self.__position[1]), end="")
        for element in range(self.size):
            print(" " * self.position[0] + "#" * self.size)
