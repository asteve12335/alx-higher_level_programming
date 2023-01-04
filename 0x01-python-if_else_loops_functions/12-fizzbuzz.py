#!/usr/bin/python3
def fizzbuzz():
    for i in range(101):
        if i != 100:
            if i == 0:
                print("{} ".format(i), end="")
            if i % 15 == 0:
                print("{} ".format("FizzBuzz"), end="")
            elif i % 5 == 0:
                print("{} ".format("Buzz"), end="")
            elif i % 3 == 0:
                print("{} ".format("Fizz"), end="")
            else:
                print("{} ".format(i), end="")
        else:
            print("{}".format("Buzz"))
