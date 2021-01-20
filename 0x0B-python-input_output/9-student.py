#!/usr/bin/python3
"""
Project: 0x0B. Python - Input/Output
Task: 9
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

    def to_json(self):
        """
        Retrieves a dictionary representation of a Student instanceo
        """
        return self.__dict__
