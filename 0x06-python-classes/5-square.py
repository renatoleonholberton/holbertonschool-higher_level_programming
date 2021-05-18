#!/usr/bin/python3
"""Simple Square class"""


class Square:
    """Simple class with attrs validation.

    Args:
        size (int): Size of the square
    """
    def __init__(self, size=0):
        self.size = size

    def area(self):
        """Method to calculate the area of the square"""
        return self.__size ** 2

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

    def my_print(self):
        """This function prints the square using '#' chars"""
        if self.__size == 0:
            print()
            return

        rang = range(self.__size)
        for _ in rang:
            print('#' * self.__size)
