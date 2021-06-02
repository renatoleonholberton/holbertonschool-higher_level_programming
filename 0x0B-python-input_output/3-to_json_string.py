#!/usr/bin/python3
"""Module with json handle function"""


def to_json_string(my_obj):
    """Appends text to a file"""
    import json
    return json.dumps(my_obj, sort_keys=True)
