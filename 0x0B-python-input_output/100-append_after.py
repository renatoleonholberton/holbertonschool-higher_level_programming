#!/usr/bin/python3
"""Module for function definition"""


def append_after(filename="", search_string="", new_string=""):
    """Adds a new line of test after each coincidence"""
    lines = []
    with open(filename, mode='r', encoding='utf-8') as file:
        lines = file.readlines()
        for ind, line in enumerate(lines):
            if search_string in line:
                lines[ind] += "{}".format(new_string)

    with open(filename, mode='w', encoding='utf-8') as file:
        file.write("".join(lines))
