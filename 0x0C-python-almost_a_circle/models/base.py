#!/usr/bin/python3
"""Defines a class Base"""
import json


class Base:
    """Represent a base"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialisations

        Args:
            Id: an integer
        """
        if id is not None:
            self.id = id
        else:
            type(self).__nb_objects += 1
            self.id = type(self).__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Returns JSON string representation of
        list_dictionaries
        args:
            list_dictionaries (list): A list of dicts
        """
        if list_dictionaries is None:
            return "{}"
        else:
            return json.dumps(list_dictionaries)
