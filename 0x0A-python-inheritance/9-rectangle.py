#!/usr/bin/python3
"""Module with class definition"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """"Rectangle class that inherits from BaseGeometry"""
    def __init__(self, width, height):
        super().__init__()
        super().integer_validator('width', width)
        super().integer_validator('height', height)
        self.__width = width
        self.__height = height

    def area(self):
        """Calculates the area of the rectangle"""
        return self.__width * self.__height

    def __str__(self):
        return '[Rectangle] {}/{}'.format(self.__width, self.__height)
