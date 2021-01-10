#!/usr/bin/python3
"""
Project: 0x07-python-test_driven_development
Task: 1
"""


def matrix_divided(matrix, div):
    """
    Function that divides all elements of a matrix.
    """

    if div == 0:
        raise ZeroDivisionError("division by zero")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix (list of lists) " +
                        "of integers/floats")
    for row in range(0, len(matrix)):
        if not isinstance(matrix[row], list):
            raise TypeError("matrix must be a matrix (list of lists) " +
                            "of integers/floats")
        if not len(matrix[0]) == len(matrix[row]):
            raise TypeError("Each row of the matrix must have the same size")
        for number in matrix[row]:
            if not isinstance(number, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) " +
                                "of integers/floats")
    new_matrix = []
    for row in range(len(matrix)):
        new_matrix.append([])
        for number in matrix[row]:
            new_matrix[row].append(round((number / div), 2))
    return new_matrix
