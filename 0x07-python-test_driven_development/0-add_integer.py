#!/usr/bin/python3
"""This module contains add_integer function"""


def add_integer(a, b=98):
    """add_integer: adds two ints and returns the result

    Args:
        a (int): First number
        b (int): Second number
    """
    if type(a) not in [int, float]:
        raise TypeError('a must be an integer')
    if type(b) not in [int, float]:
        raise TypeError('b must be an integer')

    return int(a) + int(b)
