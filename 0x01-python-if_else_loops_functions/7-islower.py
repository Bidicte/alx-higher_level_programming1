#!/usr/bin/python3
def islower(c):
    for letter in c:
        if not ('a' <= letter <= 'z') and not c:
            return False
        return True
