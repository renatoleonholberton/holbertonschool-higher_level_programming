#!/usr/bin/python3
"""Module with func definition"""


def inherits_from(obj, a_class):
    """Returns True if the object is
    an instance of the class 'a_class'"""
    return type(obj) is not a_class and issubclass(obj.__class__, a_class)
