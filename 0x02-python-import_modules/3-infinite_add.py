#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    argc = len(sys.argv)
    sum = 0
    for i in range(1, argc):
        sum += int(sys.argv[i])
    print(sum)
