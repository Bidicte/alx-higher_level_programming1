#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    for i in range(len(my_list)):
        if (int(my_list[i])):
            ma_liste = my_list[::-1]
            print("{}".format(ma_liste[i]))
