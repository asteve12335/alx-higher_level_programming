#!/usr/bin/python3
def print_list_integers(my_list=[]):
    for i in range(len(my_list)):
        string = "{:d}"
        print(string.format(my_list[i]))
