#!/usr/bin/python3
"""Class Rectangle"""


class Rectangle:
    """class Rectangle that defines a rectangle"""

    number_of_instances = 0  # class variable shared by all instances

    def __init__(self, width=0, height=0):
        """Instantiation method or constructor"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Getter method width; Private instance attribute: width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter method width Private instance attribute: width"""
        if not isinstance(value, int):
            msg = "width must be an integer"
            raise TypeError(msg)
        if value < 0:
            msg = "width must be >= 0"
            raise ValueError(msg)
        self.__width = value

    @property
    def height(self):
        """Setter method height Private instance attribute: height
        Private instance attribute: height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Setter method height Private instance attribute: height
        Private instance attribute: height
        """
        if not isinstance(value, int):
            msg = "height must be an integer"
            raise TypeError(msg)
        if value < 0:
            msg = "height must be >= 0"
            raise ValueError(msg)
        self.__height = value

    def area(self):
        """Public instance method, that returns the rectangle area"""
        return self.width * self.height

    def perimeter(self):
        """Public instance method: def perimeter(self): that returns the
        rectangle perimeter
        """
        return 2 * (self.width + self.height)

    def __str__(self):
        """Custom representation of the Rectangle class object"""
        print_obj = ''
        if self.__width == 0 or self.__height == 0:
            return print_obj
        for line in range(self.__height):
            print_obj += "{}".format('#' * self.__width)
            if line != (self.__height - 1):
                print_obj += '\n'
        return print_obj

    def __repr__(self):
        """Custom representation of how the object is generated"""
        return "Rectangle({:d}, {:d})".format(self.__height, self.__width)

    def __del__(self):
        """Calling destructor"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
