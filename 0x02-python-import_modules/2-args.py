#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    if len(sys.argv) == 1:
        print("{} arguments".format(len(sys.argv) - 1))
    elif len(sys.argv) == 2:
        print("{} argument".format(len(sys.argv)))
    else:
        print("{} arguments".format(len(sys.argv)))

    for a in range(1, len(sys.argv)):
        print("{}: {}".format(a, sys.argv))
