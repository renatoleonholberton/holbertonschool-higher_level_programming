#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or type(roman_string) != str:
        return 0

    roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                  'C': 100, 'D': 500, 'M': 1000}
    symbols = roman_dict.keys()
    number, last_digit = 0, 10000

    while roman_string != "":
        key = roman_string[0]
        if key not in symbols:
            return 0

        digit = roman_dict[key]
        if digit > last_digit:
            number -= last_digit * 2

        number += digit
        last_digit = digit
        roman_string = roman_string[1:]

    return number
