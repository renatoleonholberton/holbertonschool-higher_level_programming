#!/usr/bin/python3
"""Module with class definition"""


class MyInt(int):
    def __eq__(self, other_val):
        return super().__ne__(other_val)

    def __ne__(self, other_val):
        return super().__eq__(other_val)
