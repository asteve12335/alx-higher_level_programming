#!/usr/bin/python3
def max_integer(my_list=[]):
    if isinstance(my_list, list):
        if my_list == []:
            max_value = None
            return max_value
        else:
            max_value = 0
            for i in my_list:
                if i > max_value:
                    max_value = i

            return max_value
