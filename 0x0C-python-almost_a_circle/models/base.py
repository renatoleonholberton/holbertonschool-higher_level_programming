#!/usr/bin/python3
"""Module of base class"""
import os
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
        """Writes a json represetation of a list of dictianries
        to a file"""
        list_dicts = []
        if list_objs is not None and len(list_objs) > 0:
            list_dicts = list(map(lambda el: el.to_dictionary(), list_objs))

        json_str = Base.to_json_string(list_dicts)
        filename = '{}.json'.format(cls.__name__)
        with open(filename, mode='w', encoding='utf-8') as file:
            file.write(json_str)

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances"""
        filename = '{}.json'.format(cls.__name__)
        if not os.path.exists('./{}'.format(filename)):
            return []

        with open(filename, mode='r', encoding='utf-8') as file:
            json_dicts_list = file.read()

        return list(
            map(lambda _dict: cls.create(**_dict),
                cls.from_json_string(json_dicts_list))
        )

    @classmethod
    def create(cls, **dictionary):
        """Returns a new instance with all attributes setted"""
        if not issubclass(cls, Base):
            return
        # All init methods in derived classes take at least 2 args
        new_instance = cls(1, 1)
        new_instance.update(**dictionary)
        return new_instance

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON representation of a list dictionary"""
        if list_dictionaries is None:
            return json.dumps([])

        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """Returns a list of dictionaries loaded from a string
        JSON representation"""
        if json_string is None or json_string == '':
            return []

        return json.loads(json_string)
