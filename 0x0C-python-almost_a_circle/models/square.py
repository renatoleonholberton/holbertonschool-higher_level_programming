#!/usr/bin/python3
"""Module with Sqaure class"""


Rectangle = __import__('rectangle').Rectangle


class Square(Rectangle):
    """Square class"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return '[Square] ({:d}) {:d}/{:d} - {:d}'\
            .format(self.id, self.x, self.y, self.width)
