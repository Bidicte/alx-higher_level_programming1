#!/usr/bin/python3
def islower(c):
    for letter in c:
        if not ('a' <= letter <= 'z'):
            return False
        return True
