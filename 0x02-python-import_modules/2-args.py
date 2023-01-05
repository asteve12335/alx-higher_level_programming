#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    if len(sys.argv) == 1:
        print("{} argument".format(sys.argv))
    else:
        print("{} arguments".format(sys.argv))

    for arg in range(1, len(sys.argv)):
        print("{}: {}".format(arg, sys.argv))
