#!/usr/bin/python3
"""Module for function definition"""
from sys import stdin


count = 0
size = 0
n_stat = 0
status_codes_metrics = dict()
valid_status_codes = ['200', '301', '400', '401', '403', '404', '405', '500']


def print_stats(size, metrics):
    """Print stats"""
    print('File size:', size)
    for key in sorted(metrics.keys()):
        print("{}: {}".format(key, metrics[key]))


try:
    for line in stdin:
        count += 1
        line_ls = line.split(' ')

        try:
            status_code = line_ls[7]
            size += int(line_ls[-1])

            if status_code in valid_status_codes:
                if status_code not in status_codes_metrics:
                    status_codes_metrics[status_code] = 0
                status_codes_metrics[status_code] += 1
        except:
            pass

        if count % 10 == 0:
            print_stats(size, status_codes_metrics)
finally:
    print_stats(size, status_codes_metrics)
