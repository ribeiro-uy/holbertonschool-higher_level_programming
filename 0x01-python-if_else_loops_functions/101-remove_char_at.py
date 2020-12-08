#!/usr/bin/python3
def remove_char_at(str, n):

    i = 0
    newstr = ""

    while i != len(str):
        if i == n:
            pass
        else:
            newstr += str[i]
        i += 1
    return newstr
