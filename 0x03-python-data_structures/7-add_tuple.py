#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    for i in range(len(tuple_a)):
        for j in range(len(tuple_b)):
            int(tuple_a[i]) + int(tuple_b[j])
            print("{:d}".format(tuple_add[i][j]), end="")
