#!/usr/bin/python3
flag = 0
letter = 122
while letter != 96:
    if flag == 0:
        print("{}".format(chr(letter)), end="")
        flag = 1
        letter -= 1
    else:
        print("{}".format(chr(letter - 32)), end="")
        flag = 0
        letter -= 1
