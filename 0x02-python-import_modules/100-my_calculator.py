#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv
    from calculator_1 import add, sub, mul, div

    argc = len(argv)
    if argc != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    operator = argv[2]
    ops = ['+', '-', '*', '/']
    if operator not in ops:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    num1 = int(argv[1])
    num2 = int(argv[3])

    res = 0
    if operator == '+':
        res = add(num1, num2)
    elif operator == '-':
        res = sub(num1, num2)
    elif operator == '*':
        res = mul(num1, num2)
    elif operator == '/':
        res = div(num1, num2)

    print("{0} {op} {1} = {2}".format(num1, num2, res, op=operator))
