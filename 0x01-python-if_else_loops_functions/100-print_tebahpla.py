#!/usr/bin/python3
min, max = ord('a') - 1, ord('z')
for i in range(max, min, -1):
    if i % 2 == 0:
        print("{:c}".format(i), end="")
    else:
        print("{:c}".format(i - 32), end="")
