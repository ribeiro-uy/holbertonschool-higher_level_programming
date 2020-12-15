#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    my_list.reverse()
    for interger in range(len(my_list)):
        print ("{:d}".format(my_list[interger]))
