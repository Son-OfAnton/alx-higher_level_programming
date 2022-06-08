#!/usr/bin/python3


def square_matrix_map(matrix=[]):
    return (list(map(lambda i: list(map(lambda a: a ** 2, i)), matrix)))
