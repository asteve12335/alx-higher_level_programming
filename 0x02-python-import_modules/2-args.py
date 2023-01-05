#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    n = len(argv)

    if n == 1:
        print("0 arguments.")
    elif n == 2:
        print("{} argument:".format(n - 1))
    else:
        print("{} arguments:".format(n - 1))

    for a, b in enumerate(argv):
        if a == 0:
            continue
        print("{}: {}".format(a, b))
