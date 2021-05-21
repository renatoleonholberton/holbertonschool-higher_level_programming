#!/usr/bin/python3
"""This module contains print_square function"""


def print_square(size):
    """print_square: Prints a square with '#' char

    Args:
        size (int): Square's size
    """
    if type(size) is not int or (type(size) is float and size < 0):
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')

    for _ in range(size):
        print('#' * size)
