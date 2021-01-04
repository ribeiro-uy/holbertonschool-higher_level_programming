#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    printed_elements = 0

    for element in range(x):
        try:
            print("{:d}".format(my_list[element]), end="")
            printed_elements += 1
        except (TypeError, ValueError):
            continue
    print()
    return printed_elements

#    try:
#        for element in range(x):
#            print("{:d}".format(my_list[element]), end="")
#            printed_elements += 1
#    except ValueError:
#        continue
#    print()
#    return printed_elements
