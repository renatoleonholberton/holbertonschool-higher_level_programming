#!/usr/bin/python3
"""Simple Square class"""


class Square:
    """Simple class with attrs validation"""

    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    def area(self):
        """Method to calculate the area of the square"""
        return self.__size ** 2

    def my_print(self):
        """This function prints the square using '#' chars"""
        if self.__size == 0:
            print()
        else:
            rang = range(self.__size)
            print('\n' * self.__position[1], end="")
            for _ in rang:
                print(' ' * self.__position[0], end="")
                print('#' * self.__size)

    def __str__(self):
        str_rep = ""
        if self.__size == 0:
            str_rep = "\n"
        else:
            rang = range(self.__size)
            str_rep = str_rep + '\n' * self.__position[1]
            for _ in rang:
                str_rep = str_rep + ' ' * self.__position[0]
                str_rep = str_rep + '#' * self.__size + "\n"
        return str_rep[:-1]

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

    @property
    def position(self):
        """position: property to modify private __position attr"""
        return self.__position

    @position.setter
    def position(self, value):
        if type(value) is not tuple or len(value) != 2 \
          or type(value[0]) is not int or value[0] < 0 \
          or type(value[1]) is not int or value[1] < 0:
            raise TypeError('position must be a tuple of 2 positive integers')

        self.__position = value
