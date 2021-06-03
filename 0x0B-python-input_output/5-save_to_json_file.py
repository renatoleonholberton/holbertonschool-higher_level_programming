#!/usr/bin/python3
"""Module with json handle function"""


def save_to_json_file(my_obj, filename):
    """Parses string to object"""
    import json
    with open(filename, mode='w', encoding='utf-8') as file:
        json.dump(my_obj, file)
