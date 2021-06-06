"""Module with Rectangle class"""


Base = __import__('base').Base


class Rectangle(Base):
    """Rectangle class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """width property getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """width property setter"""
        self.__width = value

    @property
    def height(self):
        """height property getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """height property setter"""
        self.__height = value

    @property
    def x(self):
        """x property getter"""
        return self.__x

    @x.setter
    def x(self, value):
        """x property setter"""
        self.__x = value

    @property
    def y(self):
        """y property getter"""
        return self.__y

    @y.setter
    def y(self, value):
        """y property setter"""
        self.__y = value
