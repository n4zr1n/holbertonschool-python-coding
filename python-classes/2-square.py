#!/usr/bin/python3
"""
This module defines a class `Square` that computes the area of a square.

It validates that size is a non-negative integer and provides a method
to compute the area of the square.
"""


class Square:
    """
    Represents a square with validated size and area calculation.

    Attributes:
        __size (int): The size of one side of the square.
    """

    def __init__(self, size=0):
        """
        Initializes a new Square instance with optional size.

        Args:
            size (int): The size of one side of the square (default is 0).

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is negative.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    def area(self):
        """
        Computes the area of the square.

        Returns:
            int: The area of the square (size * size).
        """
        return self.__size ** 2
