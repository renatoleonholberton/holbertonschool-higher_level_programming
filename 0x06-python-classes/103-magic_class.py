#!/usr/bin/python3
"""MagiClass declaration"""


class MagicClass:
    """Simple class with attrs validation"""

    def __init__(self, radius=0):
        """Instance inicialization

        Args:
            radius (int/float): Radius attr
        """

        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')

        self.__radius = radius

    def area(self):
        """area: Calculates the area"""
        return (self.__radius ** 2) * __import__('math').pi

    def circumference(self):
        """circumference: Calculates the circumference"""
        return 2 * __import__('math').pi * self.__radius
