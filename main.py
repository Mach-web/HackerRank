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
    t1[2] = convert_month(t1[2])
    t2[2] = convert_month(t2[2])

    t1_date = "-".join(map(lambda x: x, t1[1:5]))
    t2_date = " ".join(map(lambda x: x, t2[1:5]))

    t1_date = datetime.strptime(t1_date, "%d-%m-%Y-%H:%M:%S")
    t2_date = datetime.strptime(t2_date, "%d %m %Y %H:%M:%S")
    time_diff = t1_date - t2_date
    print(time_diff)
    time_diff = time_diff.total_seconds()
    print(time_diff)
    t1_zone = (int(t1[-1][:3]) * 3600) + (int(t1[-1][3:]) * 60)
    t2_zone = (int(t2[-1][:3]) * 3600) + (int(t2[-1][3:]) * 60)
    timezone_diff = t1_zone - t2_zone

    total_diff = time_diff + timezone_diff
    return total_diff
    #413962293
    #12527392
def convert_month(month):
    month = month.lower()
    if month == "january" or "jan":
        return "1"
    elif month == "february" or "feb":
        return "2"
    elif month == "march" or "mar":
        return "3"
    elif month == "april" or "apr":
        return "4"
    elif month == "may":
        return "5"
    elif month == "june" or "jun":
        return "6"
    elif month == "july" or "jul":
        return "7"
    elif month == "august" or "aug":
        return "8"
    elif month == "september" or "sep":
        return "9"
    elif month in ["october", "oct"]:
        return "10"
    elif month == "november" or "nov":
        return "11"
    elif month == "december" or "dec":
        return "12"

print(time_delta("Fri 11 Feb 2078 00:05:21 +0400", "Mon 29 Dec 2064 03:33:48 -1100"))
print(time_delta("Wed 12 May 2269 23:22:15 -0500", "Tue 05 Oct 2269 02:12:07 -0200"))
# 413962293
# 12527392
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
