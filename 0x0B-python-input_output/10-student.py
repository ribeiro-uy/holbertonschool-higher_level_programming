#!/usr/bin/python3
"""
Project: 0x0B. Python - Input/Output
Task: 10
"""


class Student:
    """
    Class that define students
    """

    def __init__(self, first_name, last_name, age):
        """
        Constructor
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instanceo
        """
        if attrs is None:
            return self.__dict__
        else:
            new_dict = {}
            for item in attrs:
                if item in self.__dict__:
                    new_dict[item] = self.__dict__[item]
            return new_dict
