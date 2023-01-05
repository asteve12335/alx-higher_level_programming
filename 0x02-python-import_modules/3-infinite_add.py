#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    sum_args = 0
    n = len(argv)

    if n == 1:
        sum = 0
    else:
        for index in enumerate(argv):
            sum += int(index)
    print(sum)
