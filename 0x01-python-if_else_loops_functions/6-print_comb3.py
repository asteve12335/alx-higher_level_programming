#!/usr/bin/python3
for i in range(100):
    if i == 0 or i % 11 == 0 or i > 89 or i % 10 == 0:
        continue
    if i > 20 and i % 10 == 1:
        continue
    if i > 30 and i % 10 == 2:
        continue
    if i > 40 and i % 10 == 3:
        continue
    if i > 50 and i % 10 == 4:
        continue
    if i > 60 and i % 10 == 5:
        continue
    if i > 70 and i % 10 == 6:
        continue
    if i > 80 and i % 10 == 7:
        continue
    if i != 89:
        print("{:02d}, ".format(i), end="")
    else:
        print("{:02d}".format(i))
