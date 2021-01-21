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

    if n <= 0:
        lista = []
        return lista
    else:
        lista = [[1], [1, 1]]
    for i in range(1, n):
        linea = [1]
        for j in range(0, len(lista[i]) - 1):

            linea.extend([lista[i][j] + lista[i][j+1]])
        linea += [1]
        lista.append(linea)
    return lista
