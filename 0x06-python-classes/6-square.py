#!/usr/bin/python3
class Square:
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

    def area(self):
        return self.__size ** 2

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            rang = range(self.__size)
            print('\n' * self.__position[1], end="")
            for _ in rang:
                print(' ' * self.__position[0], end="")
                print('#' * self.__size)

    @property
    def size(self):
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
        return self.__position

    @position.setter
    def position(self, value):
        if type(value) is not tuple or len(value) != 2 \
          or type(value[0]) is not int or value[0] < 0 \
          or type(value[1]) is not int or value[1] < 0:
            raise TypeError('position must be a tuple of 2 positive integers')

        self.__position = value
