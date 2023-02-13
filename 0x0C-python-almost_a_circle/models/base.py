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

    @classmethod
    def create(cls, **dictionary):
        '''
        Returns an instance with all attributes already set
        args:
            dictionary (dict): A "double pointer" to a dictionary
        '''
        if cls.__name__ == 'Rectangle':
            r = cls(10, 5)
        if cls.__name__ == 'Square':
            r = cls(4)
        r.update(**dictionary)
        return r

    @classmethod
    def load_from_file(cls):
        '''
        Returns a list of instances
        '''
        inst_list = []
        try:
            with open(cls.__name__ + ".json", mode="r", encoding="utf-8") as f:
                lst = cls.from_json_string(f.read())

            for obj in lst:
                inst_list.append(cls.create(**obj))
            return inst_list
        except:
            return []
