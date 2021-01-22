#!/usr/bin/python3
"""
Project: 0x0B. Python - Input/Output
Task: 0
"""


def read_file(filename=""):
    """
    Function that reads a text file (UTF8) and prints it to stdout:
    """
    with open(filename, encoding='utf-8') as a_file:
        print(a_file.read(), end='')
