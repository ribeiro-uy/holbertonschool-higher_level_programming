#!/usr/bin/python3
def best_score(my_dict):
    if bool(my_dict):
        return max(my_dict.items())[0]
    return None
