#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence == "":
        length = 0
        first = None
    else:
        first = sentence[0]
        length = len(sentence)

    tuple = (length, first)
    return tuple
