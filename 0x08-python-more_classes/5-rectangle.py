#!/usr/bin/python3
"""
Defines a Rectangle class.
"""


class Rectangle:
    """
    Represent methods to create attributes.
    """

    def __init__(self, width=0, height=0):
        """Init The objects atribute"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width AND raise"""
        if type(value) != int:
            raise TypeError("width must BE an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set THE height and raise"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns THE area of the rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Returns the peri-meter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (self.__width + self.__height) * 2

    def __str__(self):
        """Prints the rectangle with str magic method"""
        if self.__width == 0 or self.__height == 0:
            return ""
        for i in range(self.__height - 1):
            print('#' * self.__width)
        print('#' * self.__width, end='')
        return ""

    def __repr__(self):
        """Return a string that represent the rectangle"""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Deletes the instance of Rectangle"""
        print("Bye rectangle...")
