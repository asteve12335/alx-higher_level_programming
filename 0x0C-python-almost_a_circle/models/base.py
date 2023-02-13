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

    @staticmethod
    def from_json_string(json_string):
        '''
        Returns the list of the JSON string representation `json_string`
        args:
            json_string (str): A json string
        '''
        if json_string is None:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        '''
        Writes the JSON string representation of list_objs to a file
        args:
            list_objs (list): List of instances that inherit Base
        '''
        lst = []
        with open(cls.__name__ + ".json", "w", encoding="utf-8") as f:
            if list_objs:
                for obj in list_objs:
                    lst.append(obj.to_dictionary())
            f.write(cls.to_json_string(lst))
