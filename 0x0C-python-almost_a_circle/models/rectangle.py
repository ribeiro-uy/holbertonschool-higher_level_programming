#!/usr/bin/python3
"""
Project: 0x0C-python-almost_a_circle
Task: Update Task 13
"""
from models.base import Base


class Rectangle(Base):
    """
    Class that inherits from Base,
    """

    __nb_objects = 0

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Constructor.
        """
        super().__init__(id)
        if type(width) is not int:
                raise TypeError("{:s} must be an integer".format("width"))
        if type(height) is not int:
            raise TypeError("{:s} must be an integer".format("height"))
        if type(x) is not int:
            raise TypeError("{:s} must be an integer".format("x"))
        if type(y) is not int:
            raise TypeError("{:s} must be an integer".format("y"))

        if width <= 0:
            raise ValueError("{:s} must be > 0".format("width"))
        if height <= 0:
            raise ValueError("{:s} must be > 0".format("height"))
        if x < 0:
            raise ValueError("{:s} must be >= 0".format("x"))
        if y < 0:
            raise ValueError("{:s} must be >= 0".format("y"))
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def __str__(self):
        """
        str method.
        """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.__x, self.__y, self.__width, self.__height)

    @property
    def width(self):
        """
        Getter the width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter the width.
        """
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format("width"))
        if value <= 0:
            raise ValueError("{:s} must be > 0".format("width"))
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
        Setter the height.
        """
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format("height"))
        if value <= 0:
            raise ValueError("{:s} must be > 0".format("height"))
        self.__height = value

    @property
    def x(self):
        """
        Getter the x.
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        Setter the x
        """
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format("x"))
        if value < 0:
            raise ValueError("{:s} must be > 0".format("x"))
        self.__x = value

    @property
    def y(self):
        """
        Getter the y.
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        Setter the y.
        """
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format("y"))
        if value < 0:
            raise ValueError("{:s} must be > 0".format("y"))
        self.__y = value

    def area(self):
        """
        Returns the rectangle area.
        """
        return self.__width * self.__height

    def display(self):
        """
        Prints in stdout the Rectangle instance with the character #.
        """
        print("\n" * self.__y)

        for row in range(self.__height):
            print(" " * self.__x, "#" * self.__width)

    def update(self, *args, **kwargs):
        """
        Function that assigns an argument to each attribute.
        """
        if len(args) > 5:
            raise IndexError("No more than 5 arguments")
        arguments = ["id", "width", "height", "x", "y"]
        if len(args) != 0:
            for arg in range(len(args)):
                setattr(self, arguments[arg], args[arg])
        else:
            for key in kwargs:
                setattr(self, key, kwargs[key])

    def to_dictionary(self):
        """
        returns the dictionary representation of a Rectangle.
        """

        return {"id": self.id, "width": self.__width,
                "height": self.__height, "x": self.__x, "y": self.__y}
        """
        return dict(
            (key, value)
            for (key, value) in self.__dict__.items()
        )
        """
