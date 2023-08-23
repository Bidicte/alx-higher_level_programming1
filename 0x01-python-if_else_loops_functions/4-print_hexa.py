#!/usr/bin/python3
for i in range(0,99):
    if i > 9:
        j = hex(i)
        print(f"{i} = {j}")
    else:
        print(f"{i} = 0x{i}")
