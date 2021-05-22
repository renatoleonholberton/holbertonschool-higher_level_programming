#!/usr/bin/python3
"""This module contains say_my_name function"""


def say_my_name(first_name, last_name=""):
    """say_my_name: Prints My name is <first name> <last name>

    Args:
        first_name (str): Name as string
        last_name (int): Last name as string
    """

    if type(first_name) is not str:
        raise TypeError('first_name must be a string')
    if type(last_name) is not str:
        raise TypeError('last_name must be a string')

    print('My name is {} {}'.format(first_name, last_name))
