#!/usr/bin/python3
"""a class square with a size field"""


class Square:
    """private size field"""
    def __init__(self, size=0):
        """validates the size"""
        if type(size) != int:
            raise TypeError("size is not an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
