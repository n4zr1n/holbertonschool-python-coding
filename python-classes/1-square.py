#!/usr/bin/python3
"""
This module defines a class `Square` that validates the size input.

The Square class encapsulates the concept of a square and ensures that
its size is a non-negative integer.
"""


class Square:
    """
    Represents a square with a validated size.

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
