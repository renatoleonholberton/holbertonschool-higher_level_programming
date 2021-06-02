#!/usr/bin/python3
"""Module with io function"""


def append_write(filename="", text=""):
    """Appends text to a file"""
    with open(filename, mode='a', encoding='utf-8') as file:
        return file.write(text)
