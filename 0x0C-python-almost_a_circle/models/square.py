#!/usr/bin/python3
"""
Project: 0x0C-python-almost_a_circle
Task: Update Task 3
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Class that inherits from Rectangle
    """

    __nb_objects = 0

    def __init__(self, size, x=0, y=0, id=None):
        """
        Constructor
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        str method
        """
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """
        Getter the size
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        Setter the size
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        Function that assigns an argument to each attribute:
        """

        if len(args) > 4:
            raise IndexError("No more than 4 arguments")
        arguments = ["id", "size", "x", "y"]
        if len(args) != 0:
            for arg in range(len(args)):
                setattr(self, arguments[arg], args[arg])
        else:
                for key, value in kwargs.items():
                    setattr(self, key, value)

    def to_dictionary(self):
        """
        returns the dictionary representation of a Square
        """
        return {"id": self.id, "size": self.size, "x": self.x, "y": self.y}
