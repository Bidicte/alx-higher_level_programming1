#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if not isinstance(my_list, int):
        my_list.reverse()
    for i in my_list:
        print("{}".format(i))
