#!/usr/bin/python3
"""
Project: 0x0A-python-inheritance
Task: 1
"""


class MyList(list):
    """
    Class that inherits from list.
    """
    def print_sorted(self):
        """
        Public instance method that prints the list,
        but sorted (ascending sort).
        """
        sort_list = self[:]
        print(sorted(sort_list))
