#!/usr/bin/python3
"""Module with json handle function"""


def save_to_json_file(my_obj, filename):
    """Parses string to object"""
    import json
    obj_str = json.dumps(my_obj, sort_keys=True)
    with open(filename, mode='w', encoding='utf-8') as file:
        file.write(obj_str)
