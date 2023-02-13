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
        except Exception:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        class method that serializes in CSV
        Arguments:
            list_objs: list of inherited instances of class Base
        """
        filename = cls.__name__ + ".csv"
        with open(filename, "w", newline="") as csvfile:
            if list_objs is None or list_objs == []:
                csvfile.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """
        class method that deserializes in CSV
        """
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r", newline="") as csvfile:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                list_dicts = csv.DictReader(csvfile, fieldnames=fieldnames)
                list_dicts = [dict([k, int(v)] for k, v in d.items())
                              for d in list_dicts]
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """
        Draw rectangles and squares
        'turtle' module imported
        Arguments:
            list_rectangles: list of rectangles
            list_squares: list of squares
        """
        turt = turtle.Turtle()
        turt.screen.bgcolor("#b7312c")
        turt.pensize(3)
        turt.shape("turtle")

        turt.color("#ffffff")
        for rect in list_rectangles:
            turt.showturtle()
            turt.up()
            turt.goto(rect.x, rect.y)
            turt.down()
            for i in range(2):
                turt.forward(rect.width)
                turt.left(90)
                turt.forward(rect.height)
                turt.left(90)
            turt.hideturtle()

        turt.color("#b5e3d8")
        for sq in list_squares:
            turt.showturtle()
            turt.up()
            turt.goto(sq.x, sq.y)
            turt.down()
            for i in range(2):
                turt.forward(sq.width)
                turt.left(90)
                turt.forward(sq.height)
                turt.left(90)
            turt.hideturtle()

        turtle.exitonclick()
