#!/usr/bin/python3
"""
This module defines a class `Square` which represents a square.

The purpose of this module is to create a basic structure of a square
by encapsulating the size attribute as a private instance variable.
"""


class Square:
    """
    Represents a square.

    This class defines a square by encapsulating its size as a private
    attribute. The size is a fundamental property of a square and is
    hidden to enforce encapsulation and future validation logic.
    """

    def __init__(self, size):
        """
        Initializes a new instance of the Square class.

        Parameters:
            size (int): The size (length of one side) of the square.
                        No validation is performed at this stage.
        """
        self.__size = size
