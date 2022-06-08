#!/usr/bin/python3


def square_matrix_simple(matrix=[]):
    new_matrix = []

    for row in matrix:
            new_matrix.append([column**2 for column in row])
    return new_matrix
