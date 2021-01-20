#!/usr/bin/python3
"""
Project: 0x0B. Python - Input/Output
Task: 2
"""


def append_write(filename="", text=""):
    """
    Function that appends a string at the end of a text file (UTF8)
    and returns the number of characters added
    """
    with open(filename, mode='a', encoding='utf-8') as my_file:
        return my_file.write(text)
