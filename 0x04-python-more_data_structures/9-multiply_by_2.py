#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new = {}
    for x, y in a_dictionary.items():
        new[x] = y * 2
    return new
