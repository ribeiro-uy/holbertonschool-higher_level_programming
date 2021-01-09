#!/usr/bin/python3
"""
Project: 0x07-python-test_driven_development
Task: 5
"""


def text_indentation(text):
    """
    Function that prints a text with 2 new lines after each of these characters: ., ? and :
    """
    flag_space = 0
    conditions = ".?:"
    
    for character in text:
        if flag_space == 1:
            flag_space = 0
            continue
        if character in conditions:
            print("{}".format(character), end="")
            print()
            print()
            flag_space = 1
        else:
            print("{}".format(character), end="")
