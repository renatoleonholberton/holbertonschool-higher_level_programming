#!/usr/bin/python3
"""Module with json handle and io function"""


def load_from_json_file(filename):
    """Reads a JSON file and creates a new object based on it"""
    import json
    with open(filename, mode='r', encoding='utf-8') as file:
        return json.loads(file.read())
