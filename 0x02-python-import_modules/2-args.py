#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    if len(sys.argv) == 1:
        print("{} argument".format(len(sys.argv)))
    else:
        print("{} arguments".format(len(sys.argv)))

    for a in range(1, len(sys.argv)):
        print("{}: {}".format(a, sys.argv))
