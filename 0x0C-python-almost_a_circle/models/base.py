#!/usr/bin/python3
"""
Project: 0x0C-python-almost_a_circle
Task: update task 15
"""
import json


class Base:
    """
    Class Base:
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Constructor
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Returns the JSON string representation of list_dictionaries.
        """
        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Writes the JSON string representation of list_objs to a file.
        """
        if list_objs is None:
            return "[]"

        for objects in list_objs:
            with open(filename, encoding="utf-8", mode="w") as my_file:
                my_file.write(cls.to_json_string(objects))
