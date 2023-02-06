#!/usr/bin/python3
""" Inheritance """


class Mylist(list):
    """
    Superclass -> list
    Subclass -> Mylist
    """
    def __init__(self):
        """
        Initialisations
        """
        super().__init__()

    def print_sorted(self):
        """
        Prints sorted lis
        in ascending order
        """
        print(sorted(self))
