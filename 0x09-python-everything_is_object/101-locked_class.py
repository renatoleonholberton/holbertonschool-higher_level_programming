#!/usr/bin/python3
"""LockedClass to prevent atribute creation"""


class LockedClass:
    """Class that prevent attribute ceation"""
    __slots__ = ['first_name']
    def __setattr__(self, name, value):
        if not name == 'first_name':
            raise AttributeError(
                "'LockedClass' object has no attribute '{}'".format(name))
        self.__dict__[name] = value
