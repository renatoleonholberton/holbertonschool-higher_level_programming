#!/usr/bin/python3
"""Module that handles serialization"""


def class_to_json(obj):
    """Returns the dictionary descrition of a simple data structure"""
    return obj.__dict__
