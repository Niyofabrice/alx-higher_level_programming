#!/usr/bin/python3
"""class Rectangle"""

class Rectangle:
    """class that defines properties of a rectangle"""
    def __init__(self, width=0, height=0):
        """creating new instance of Rectangle"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """width"""
        return(self.__width)

    @property
    def height(self):
        """height"""
        return(self.__height)

    @width.setter
    def width(self, value):
        """setting the width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @height.setter
    def height(self, value):
        """setting the height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    def area(self):
        """calculating area of rectangle"""
        return(self.__width * self.__height)

    def perimeter(self):
        """calculating perimeter of rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return(2 * (self.__width + self.__height))
