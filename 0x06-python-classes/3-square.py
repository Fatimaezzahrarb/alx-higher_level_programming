#!/usr/bin/python3
"""Define A class Square."""


class Square:
    """Represent A square."""

    def __init__(self, size=0):
        """Initialize A new square.

        Args:
            size (int): The size OF the new square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Return the current area of the square."""
        return (self.__size * self.__size)
