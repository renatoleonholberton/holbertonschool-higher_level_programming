#!/usr/bin/python3
"""Module with function definition"""


def read_file(filename=""):
    """Opens a file and prints its contents to stdout"""
    with open(filename, mode='r', encoding='utf-8') as file:
        print(file.read(), end="")
