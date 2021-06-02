#!/usr/bin/python3
"""Module with class definition"""


class BaseGeometry:
    """Empty class"""
    def area(self):
        """Raises an Exception"""
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """Validates that a value is a positive integer"""
        if type(value) != int:
            raise TypeError('{} must be an integer'.format(name))
        if value <= 0:
            raise ValueError('{} must be greater than 0'.format(name))
