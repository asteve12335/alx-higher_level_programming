#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    if isinstance(my_list, list):
        n = 0
        try:
            for i in range(x):
                if type(my_list[i]) == int:
                    print("{:d}".format(my_list[i]), end="")
                    n += 1
                else:
                    continue
        except (ValueError, TypeError):
            pass
        except IndexError:
            print()
            print("list index out of range")
        finally:
            print()
            return n
