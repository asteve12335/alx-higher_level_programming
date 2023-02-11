#!/usr/bin/python3
"""Defines a class Base"""


class Base:
    """Represent a base"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialisations

        Args:
            Id: an integer
        """
        if id != None:
            self.id = id
        type(self).__nb_objects += 1
        self.id = type(self).__nb_objects
