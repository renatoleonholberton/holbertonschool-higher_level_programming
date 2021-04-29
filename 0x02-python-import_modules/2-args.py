#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    argc = len(sys.argv) - 1
    str = "argument"
    if argc == 0:
        print("0 {}s.".format(str))
    else:
        if argc > 1:
            str += "s"
        str += ":"
        print(argc, str)

        for i in range(1, argc + 1):
            print("{}:".format(i), sys.argv[i])
