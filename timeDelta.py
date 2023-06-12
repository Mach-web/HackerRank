#!/bin/python3

import math
import os
import random
import re
import sys
from datetime import date
from datetime import datetime
# Complete the time_delta function below.
def time_delta(t1, t2):
    t1 = t1.split()
    t2 = t2.split()

    t1_date = date(int(t1[3]), convert_month(t1[2]), int(t1[1]))
    t2_date = date(int(t2[3]), convert_month(t2[2]), int(t2[1]))
    date_difference = t1_date - t2_date
    date_difference = date_difference.total_seconds()
    print(date_difference)

    time_diff = datetime.strptime(t1[4], "%H:%M:%S") - datetime.strptime(t2[4], "%H:%M:%S")
    time_diff = time_diff.total_seconds()
    print(time_diff)

    t1_zone = (int(t1[-1][:3]) * 3600) + (int(t1[-1][3:]) * 60)
    t2_zone = (int(t2[-1][:3]) * 3600) + (int(t2[-1][3:]) * 60)
    timezone_diff = t2_zone - t1_zone
    print(timezone_diff)
    total_diff = date_difference + time_diff + timezone_diff
    print(total_diff)

def convert_month(month):
    month = month.lower()
    if month == "january":
        return 1
    elif month == "february":
        return 2
    elif month == "march":
        return 3
    elif month == "april":
        return 4
    elif month == "may":
        return 5
    elif month == "june":
        return 6
    elif month == "july":
        return 7
    elif month == "august":
        return 8
    elif month == "september":
        return 9
    elif month == "october":
        return 10
    elif month == "november":
        return 11
    elif month == "december":
        return 12
time_delta("Sun 10 May 2015 13:54:36 -0700", "Sun 10 May 2015 13:54:36 -0000")
time_delta("Sat 02 May 2015 19:54:36 +0530", "Fri 01 May 2015 13:54:36 -0000")
# if __name__ == '__main__':
#     # fptr = open(os.environ['OUTPUT_PATH'], 'w')
#     t = int(input())
#     for t_itr in range(t):
#         t1 = input()
#
#         t2 = input()
#
#     #     delta = time_delta(t1, t2)
#     #
#     #     fptr.write(delta + '\n')
#     #
#     # fptr.close()
