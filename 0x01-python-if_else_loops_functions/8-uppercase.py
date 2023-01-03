#!/usr/bin/python3
def uppercase(str):
    word = ""
    for i in str:
        if i in "abcdefghijklmnopqrstuvwxyz":
            num = ord(i) - 32
        else:
            num = ord(i)
        word += chr(num)
    print("{}".format(string))
