#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    if isinstance(my_list, list):
        num_elements = 0

        try:
            for i in range(x):
                print(my_list[i], end="")
                num_elements += 1
        except IndexError:
            pass
        finally:
            print()
            return num_elements
