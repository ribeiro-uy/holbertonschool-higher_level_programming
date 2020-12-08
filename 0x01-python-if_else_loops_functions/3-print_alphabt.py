#!/usr/bin/python3
letter = 97
while letter != 123:
    if letter != 101 and letter != 113:
        print("{}".format(chr(letter)), end="")
    letter += 1
