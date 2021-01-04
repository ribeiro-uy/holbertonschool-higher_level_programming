#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []

    for numbers in range(list_length):
        try:
            result = my_list_1[numbers] / my_list_2[numbers]
        except ZeroDivisionError:
            result = 0
            print("division by 0")
        except TypeError:
            result = 0
            print("wrong type")
        except IndexError:
            result = 0
            print("out of range")
        finally:
            new_list.append(result)
    return new_list
