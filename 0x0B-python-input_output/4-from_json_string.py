#!/usr/bin/python3
"""Module with json handle function"""


def from_json_string(my_str):
    """Parses string to object"""
    import json
    return json.loads(my_str)
