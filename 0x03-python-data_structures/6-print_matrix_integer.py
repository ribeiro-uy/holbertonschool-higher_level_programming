#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    print("{}".format("\n".join([" ".join(["{:d}".format(number)
                                for number in row]) for row in matrix])))
