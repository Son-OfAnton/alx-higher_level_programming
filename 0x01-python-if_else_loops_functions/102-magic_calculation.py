#!/usr/bin/python3
def magic_calculation(A, B, C):
    if A < B:
        return C
    elif C > B:
        return A + B
    return (A * B) - C
