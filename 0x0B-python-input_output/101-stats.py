#!/usr/bin/python3
"""Module for function definition"""
from os import stat
from sys import stdin


count = 0
size = 0
n_stat = 0
stats = dict()
summary_last_10 = dict()

try:
    for line in stdin:
        count += 1
        line_ls = line.split(' ')
        status_code = line_ls[7]
        size += int(line_ls[-1])

        if status_code not in summary_last_10:
            summary_last_10[status_code] = 0
        summary_last_10[status_code] += 1

        if count % 10 == 0:
            store = {
                "size": size,
                "stats": summary_last_10
            }
            stats[n_stat] = store
            summary_last_10 = dict()
            n_stat += 1
finally:
    for key in sorted(stats.keys()):
        print('File size:', stats[key]['size'])
        inner_stats = stats[key]['stats']
        for sts_code in sorted(inner_stats.keys()):
            print("{}: {}".format(sts_code, inner_stats[sts_code]))
