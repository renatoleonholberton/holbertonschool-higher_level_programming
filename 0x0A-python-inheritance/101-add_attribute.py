#!/usr/bin/python3
"""Module with class definition"""


def add_attribute(obj, attr_name, value):
    """This function adds a new attribute to an object"""
    if hasattr(obj, '__dict__'):
        setattr(obj, attr_name, value)
    else:
        raise TypeError('can\'t add new attribute')
