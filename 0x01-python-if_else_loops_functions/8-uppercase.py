#!/usr/bin/python3
def uppercase(str):
    for c in str:
        if ord(c) >= ord('a') and ord(c) <= ord('z'):
            plus = -32
        else:
            plus = 0
        print("{:c}".format(ord(c) + plus), end="")
    print()
