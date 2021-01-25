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
        if type(list_objs) is not list:
            raise TypeError("argument must be a list")
        lista = []
        name = str(cls.__name__) + ".json"
        if list_objs is None:
            with open(name, 'w') as f:
                f.write(cls.to_json_string(lista))
        else:
            for i in list_objs:
                lista.append(cls.to_dictionary(i))
            with open(name, 'w') as f:
                    f.write(cls.to_json_string(lista))

    @staticmethod
    def from_json_string(json_string):
        """
        Returns the list of the JSON string representation json_string.
        """
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Returns an instance with all attributes already set.
        """
        dummy_instance = cls(1, 1, 1, 1)
        cls.update(dummy_instance, **dictionary)
        return dummy_instance

    @classmethod
    def load_from_file(cls):
        """
        Returns a list of instances.
        """
        filename = str(cls.__name__) + ".json"
        lista_big = []
        lista_dicts = []
        text = ""
        try:
            with open(filename, 'r') as f:
                text = f.read()
            lista_dicts = cls.from_json_string(text)
            for i in lista_dicts:
                inst = cls.create(**i)
                lista_big.append(inst)
            return lista_big
        except IOError:
            return []
