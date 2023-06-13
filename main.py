#!/bin/python3

import math
import os
import random
import re
import sys
from datetime import *


# Complete the time_delta function below.
def time_delta(t1, t2):
    t1 = t1.split()
    t2 = t2.split()
    # t1[2] = convert_month(t1[2])
    # t2[2] = convert_month(t2[2])
    t1_date = "-".join(map(lambda x: x, t1[1:6]))
    t2_date = " ".join(map(lambda x: x, t2[1:6]))

    t1_date = datetime.strptime(t1_date, "%d-%b-%Y-%H:%M:%S-%z")
    t2_date = datetime.strptime(t2_date, "%d %b %Y %H:%M:%S %z")
    time_diff = t1_date - t2_date
    time_diff = time_diff.total_seconds()
    return abs(time_diff)
def convert_month(month):
    month = month.lower()
    if month == "january" or month == "jan":
        return "01"
    elif month == "february" or month == "feb":
        return "02"
    elif month == "march" or month == "mar":
        return "03"
    elif month == "april" or month == "apr":
        return "04"
    elif month == "may":
        return "05"
    elif month == "june" or month == "jun":
        return "06"
    elif month == "july" or month == "jul":
        return "07"
    elif month == "august" or month == "aug":
        return "08"
    elif month == "september" or month == "sep":
        return "09"
    elif month == "october" or month == "oct":
        return "10"
    elif month == "november" or month == "nov":
        return "11"
    elif month == "december" or month == "dec":
        return "12"
print(time_delta("Sun 10 May 2015 13:54:36 -0700", "Sun 10 May 2015 13:54:36 -0000"))
print(time_delta("Fri 11 Feb 2078 00:05:21 +0400", "Mon 29 Dec 2064 03:33:48 -1100"))
print(time_delta("Wed 12 May 2269 23:22:15 -0500", "Tue 05 Oct 2269 02:12:07 -0200"))
print(time_delta("Sat 14 Sep 2126 00:36:44 +1400", "Wed 22 Jun 2050 23:18:57 -0100"))
# 413962293
# 12527392
#2405413067
# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')
#     t = int(input())
#
#     for t_itr in range(t):
#         t1 = input()
#
#         t2 = input()
#
#         delta = time_delta(t1, t2)
#         if delta is not None:
#             fptr.write(f"{delta:.0f}" + "\n")
#
#     fptr.close()
