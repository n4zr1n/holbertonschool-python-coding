#!/usr/bin/python3
"""
This module defines a class Square with a private size attribute,
including property getter and setter for controlled access.
"""


class Square:
    """
    Represents a square with validated size and area calculation.
    """

    def __init__(self, size=0):
        """
        Initializes a new Square instance.

        Args:
            size (int): Optional size of the square (default 0).

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        self.size = size  # use the setter for validation

    @property
    def size(self):
        """
        Retrieves the current size of the square.

        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets a new value for size with validation.

        Args:
            value (int): The new size of the square.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        """
        Calculates the area of the square.

        Returns:
            int: The area (size squared).
        """
        return self.__size ** 2
