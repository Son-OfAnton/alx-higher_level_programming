#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    for i in range(0, 3):
        for j in range(0, 3):
            print("{:d} ".format(matrix[i][j]), end="")
        print("\n")