#!/usr/bin/python3
"""Module with MyList class"""


class MyList(list):
    """this class inherits from list"""
    def print_sorted(self):
        """Prints a list sorted in ascending order"""
        print(sorted(self))
