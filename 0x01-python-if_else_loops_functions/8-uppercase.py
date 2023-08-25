#!/usr/bin/python3
def uppercase(str):
    for c in str:
        diff = ord('a') - ord('A')
        if ord(c) >= ord('a') and ord(c) <= ord('z'):
            c = chr(ord(c) - diff)
            print("{}".format(c), end="")
    print()
                                                        
