#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    printed = 0
    i = 0

    for i in range(0, x):
        try:
            print("{:d}".format(my_list[i]), end="")
            printed += 1
        except IndexError:
            raise
        except Exception:
            pass
    print()

    return printed


my_list = [1, 2, 3, 4, 5]

nb_print = safe_print_list_integers(my_list, 2)
print("nb_print: {:d}".format(nb_print))

my_list = [1, 2, 3, "Holberton", 4, 5, [1, 2, 3]]
nb_print = safe_print_list_integers(my_list, len(my_list))
print("nb_print: {:d}".format(nb_print))

nb_print = safe_print_list_integers(my_list, len(my_list) + 2)
print("nb_print: {:d}".format(nb_print))