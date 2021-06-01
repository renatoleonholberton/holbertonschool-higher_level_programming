#!/usr/bin/python3
"""Module with func definition"""


def is_same_class(obj, a_class):
    """Returns True if the object is exactly
    an instance of the class 'a_class'"""
    return type(obj) is a_class
