#!/usr/bin/python3
def uppercase(str):
    for i in range(0, len(str)):
        if str[i] >= 'a' and str[i] <= 'z':
            ascii = ord(str[i])
            print("{:c}".format(ascii - 32), end="")
        else:
            print(str[i], end="")
    print()
