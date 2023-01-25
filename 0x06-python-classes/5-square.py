#!/usr/bin/python3
"""Define a class Square"""


class Square:
    """Represent a square."""

    def __init__(self, size=0):
        """Initialize a new square.

        Args:
            size (int): The size of the new square.
        """
        self.size = size

    @property
    def size(self):
        """Getter"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """Setter"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns square area"""
        return (self.__size ** 2)

    def my_print(self):
        """Outputs square in #'s"""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                for j in range(self.size):
                    print("#", end="")
                print()
