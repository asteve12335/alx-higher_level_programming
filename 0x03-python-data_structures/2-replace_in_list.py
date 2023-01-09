#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    if idx not in range(len(my_list)):
        return my_list
    else:
        return (my_list[idx]=element)
