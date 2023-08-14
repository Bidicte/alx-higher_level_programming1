#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    for n in range(len(my_list)):
        if (int(my_list[n])):
            my_list.reverse()
            print(my_list[n])
