#!/usr/bin/python3
def no_c(my_string):
    new_string = ""
    for letter in range(len(my_string)):
        if my_string[letter] == "c" or my_string[letter] == "C":
            pass
        else:
            new_string += my_string[letter]
    return new_string
