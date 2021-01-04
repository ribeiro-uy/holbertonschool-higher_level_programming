#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    total_elements = 0

    try:
        for element in range(x):
            print("{}".format(my_list[element]), end="")
            total_elements += 1
    except IndexError:
        pass
    print()
    return total_elements
