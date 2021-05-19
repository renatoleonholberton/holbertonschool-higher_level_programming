#!/usr/bin/python3
"""Simple Square class"""


class Square:
    """Simple class with attrs validation"""

    def __init__(self, size=0):
        self.size = size

    def area(self):
        """Method to calculate the area of the square"""
        return self.__size ** 2

    def __eq__(self, square):
        return self.area() == square.area()

    def __ne__(self, square):
        return self.area() != square.area()

    def __gt__(self, square):
        return self.area() > square.area()

    def __ge__(self, square):
        return self.area() >= square.area()

    def __lt__(self, square):
        return self.area() < square.area()

    def __le__(self, square):
        return self.area() <= square.area()

    @property
    def size(self):
        """size: property to modify private __size attr"""
        return self.__size

    @size.setter
    def size(self, size):
        if type(size) is not int:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')

        self.__size = size
