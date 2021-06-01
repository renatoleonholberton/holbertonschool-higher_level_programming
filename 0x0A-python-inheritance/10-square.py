#!/usr/bin/python3
"""Module with class definition"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """"Square class that inherits from Rectangle"""
    def __init__(self, size):
        super().__init__(size, size)
        super().integer_validator('size', size)
        self.__size = size

    def area(self):
        """Calculates the area of the rectangle"""
        return self.__size ** 2
