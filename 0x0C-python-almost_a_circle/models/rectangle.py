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

    def __validate_type(self, attr_name, value, _type):
        """Validates attr type"""
        if type(value) is not _type:
            raise TypeError('{} must be an integer'.format(attr_name))

    def __validate_gt0(self, attr_name, value):
        """Validates if attr value is greater than 0"""
        if value <= 0:
            raise ValueError('{} must be > 0'.format(attr_name))

    def __validate_ge0(self, attr_name, value):
        """Validates if attr value is greater than or equal to 0"""
        if value < 0:
            raise ValueError('{} must be >= 0'.format(attr_name))

    @property
    def width(self):
        """width property getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """width property setter"""
        self.__validate_type('width', value, int)
        self.__validate_gt0('width', value)
        self.__width = value

    @property
    def height(self):
        """height property getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """height property setter"""
        self.__validate_type('height', value, int)
        self.__validate_gt0('height', value)
        self.__height = value

    @property
    def x(self):
        """x property getter"""
        return self.__x

    @x.setter
    def x(self, value):
        """x property setter"""
        self.__validate_type('x', value, int)
        self.__validate_ge0('x', value)
        self.__x = value

    @property
    def y(self):
        """y property getter"""
        return self.__y

    @y.setter
    def y(self, value):
        """y property setter"""
        self.__validate_type('y', value, int)
        self.__validate_ge0('y', value)
        self.__y = value

    def area(self):
        """Calculates and returns the rectangle's area"""
        return self.width * self.height
