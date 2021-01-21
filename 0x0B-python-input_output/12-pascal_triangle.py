#!/usr/bin/python3
"""
Project: 0x0B. Python - Input/Output
Task: 12
"""


def pascal_triangle(n):
    """
    Create a function def pascal_triangle(n):
    that returns a list of lists of integers representing
    the Pascals triangle of n
    """
    new_list = []
    if n <= 0:
        return new_list
    new_list = [[1], [1, 1]]
    for i in range(1, n):
        row = [1]
        for j in range(0, len(new_list[i]) - 1):
            row.extend([new_list[i][j] + new_list[i][j+1]])
        row += [1]
        new_list.append(row)
    return new_list
