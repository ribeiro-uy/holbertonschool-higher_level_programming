#!/usr/bin/python3
"""
Project: 0x08. Python - More Classes and Objects
Task: 7
"""


class Rectangle:
    """"
    Class Rectangle that defines a rectangle by: (based on 0-rectangle.py)
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Constructor
        """

        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def __str__(self):
        """
        Print the rectangle with the character #
        """

        txt = ""
        if self.__width == 0 or self.__height == 0:
            return txt
        else:
            for row in range(self.__height):
                txt += str(self.print_symbol) * self.__width
                if row < (self.__height - 1):
                    txt += "\n"
        return txt

    def __repr__(self):
        """
        Return a string representation of the rectangle
        """

        return ("Rectangle(" + str(self.__width) + ", " +
                str(self.__height) + ")")

    def __del__(self):
        """
        Delete object
        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @property
    def width(self):
        """
        Getter the width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter the width
        """

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Getter the height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter the height
        """

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Returns the rectangle area
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Returns the rectangle perimeter

        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width + self.__height) * 2

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Returns the biggest rectangle based on the area
        """

        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")

        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area == rect_2.area:
            return rect_1
        elif rect_1.area() < rect_2.area():
            return rect_2
        else:
            return rect_1

    @classmethod
    def square(cls, size=0):
        """
        Returns a new Rectangle instance with width == height == size
        """

        return Rectangle(size, size)
