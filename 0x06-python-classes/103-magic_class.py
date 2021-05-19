#!/usr/bin/python3
"""MagiClass declaration"""


class MagicClass:
    """Simple class with attrs validation"""

    def __init__(self, radius=0):
        """Instance inicialization

        Args:
            radius (int/float): Radius attr
        """
        self.__radius = 0

        if type(self.__radius) is not int and type(self.__radius) is not float:
            raise TypeError('radius must be a number')

        self.__radius = radius

    def area(self):
        """area: Calculates the area"""
        return (self.__radius ** 2)

    def circumference(self):
        """circumference: Calculates the circumference"""
        return 2 * self.__radius
