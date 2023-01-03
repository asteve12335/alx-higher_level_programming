#!/usr/bin/python3
def uppercase(str):
    for letter in str:
        if 65 <= ord(letter) and ord(letter) <= 90:
            continue
        else:
            ord(letter) - 32
        print("{}".format(letter), end="")
    print("{}".format())
