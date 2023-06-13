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


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)
        if delta is not None:
            fptr.write(f"{delta:.0f}" + "\n")

    fptr.close()
