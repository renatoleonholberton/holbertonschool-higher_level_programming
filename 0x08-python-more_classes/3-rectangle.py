#!/usr/bin/python3
"""Module that defines a class"""


class Rectangle:
    """Rectangle empty class"""

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """width property"""
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """height property"""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        """Return the rectangle's area"""
        return self.width * self.height

    def perimeter(self):
        """Return the rectangle's perimeter"""
        if self.width == 0 or self.height == 0:
            return 0
        return (self.width + self.height) * 2

    def __str__(self):
        """Prints the rectangle to stdout using #"""
        if self.width == 0 or self.height == 0:
            return ''
        rstr = ''
        for _ in range(self.__height):
            rstr += ('#' * self.width) + '\n'
        return rstr[:-1]
