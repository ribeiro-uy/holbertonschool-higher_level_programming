#!/usr/bin/python3
def fizzbuzz():
i = 1
while i <= 100:
    if i % 15 == 0:
        print("FizzBuzz", end="")
    elif i % 3 == 0:
        print("Fizz", end="")
    elif (i % 5 == 0):
        print("Buzz", end="")
    else:
        print(i, end="")

    if i != 100:
        print(" ", end="")
    else:
        print("")
    i += 1
