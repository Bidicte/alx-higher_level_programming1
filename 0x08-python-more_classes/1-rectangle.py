#!/usr/bin/python3
""" Define a rectangle class """


class Rectangle:
    """ Represents a class with properties """

    def __init__(self, width=0, height=0):
        """ Initialize a new rectangle

        Args:
            width (int): the width of the new rectangle
            height (int): the height of the new rectangle
        """
        self.__width = width,
        self.__height = height

    @property
    def width(self):
        """ Getter and setter of the new rectangle """
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ Getter and setter of the new rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__height = value
