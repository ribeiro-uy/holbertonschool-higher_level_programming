#!/usr/bin/python3
"""function that finds a peak in a list of unsorted integers"""


def find_peak(list_of_integers):
    """find peak"""
    list = list_of_integers
    lng = len(list)
    if lng < 1:
        return None
    if lng == 1:
        return list[0]
    if lng == 2:
        return max(list)
    mid = lng // 2
    if list[mid] < list[mid - 1]:
        return find_peak(list[:mid])
    if list[mid] < list[mid + 1]:
        return find_peak(list[mid + 1:])
    return list[mid]
