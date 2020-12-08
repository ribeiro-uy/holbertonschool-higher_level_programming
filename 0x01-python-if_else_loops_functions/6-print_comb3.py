#!/usr/bin/python3
decimal = 0
while decimal <= 9:
    unit = 0
    while unit <= 9:
        if decimal == 8 and unit == 9:
            print("{}{}".format(decimal, unit))
            break
        elif unit != decimal and unit > decimal:
            print("{}{}, ".format(decimal, unit), end="")
        unit += 1
    decimal += 1
