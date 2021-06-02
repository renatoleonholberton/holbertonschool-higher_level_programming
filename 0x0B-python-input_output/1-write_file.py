#!/usr/bin/python3
"""Module with io function"""


def write_file(filename="", text=""):
    """Writes to a file"""
    with open(filename, mode='w', encoding='utf-8') as file:
        return file.write(text)
