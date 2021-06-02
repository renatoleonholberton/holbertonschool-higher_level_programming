#!/usr/bin/python3
"""Module for class Student"""


class Student:
    """Class Student"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Returns a dictionary representation of the object"""
        if attrs is None:
            return self.__dict__
        d = dict()
        for attr in attrs:
            if attr in self.__dict__:
                d[attr] = self.__dict__[attr]
        return d

    def reload_from_json(self, json):
        """Replace all attributes of the instance"""
        for key in json:
            self.__dict__[key] = json[key]
