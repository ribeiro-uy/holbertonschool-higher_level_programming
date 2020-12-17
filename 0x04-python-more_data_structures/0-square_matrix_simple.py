#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []

    for x in matrix:
        new_matrix.append([y**2 for y in x])
    return new_matrix
