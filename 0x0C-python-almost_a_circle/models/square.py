#!/usr/bin/python3
"""Module with Sqaure class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """size property getter"""
        return self.width

    @size.setter
    def size(self, value):
        """size property setter, uses wdth and height
        properties from Rrectangle"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Updates the listed instance attributes"""
        valid_attrs = ['id', 'size', 'x', 'y']
        self._protected_update(valid_attrs, *args, **kwargs)

    def to_dictionary(self):
        """Returns a dictionary containing attributes listed
        in 'valid_attrs'"""
        valid_attrs = ['id', 'size', 'x', 'y']
        return self._protected_to_dictionary(valid_attrs)

    def __str__(self):
        return '[Square] ({:d}) {:d}/{:d} - {:d}'\
            .format(self.id, self.x, self.y, self.width)
