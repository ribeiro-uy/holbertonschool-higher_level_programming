#!/usr/bin/python3
def element_at(my_list, idx):
    if  0 > idx > (len(my_list) - 1):
        return None
    return my_list[idx]
