#!/usr/bin/python3
"""Module of base class"""
import json


class Base:
    """Base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            type(self).__nb_objects += 1
            self.id = type(self).__nb_objects

    @classmethod
    def save_to_file(cls, list_objs):
        """"""
        list_dicts = []
        if list_objs is not None and len(list_objs) > 0:
            list_dicts = list(map(lambda el: el.to_dictionary(), list_objs))

        json_str = Base.to_json_string(list_dicts)
        filename = '{}.json'.format(cls.__name__)
        with open(filename, mode='w', encoding='utf-8') as file:
            file.write(json_str)

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON representation of a list dictionary"""
        if list_dictionaries is None:
            return json.dumps([])
        return json.dumps(list_dictionaries)
