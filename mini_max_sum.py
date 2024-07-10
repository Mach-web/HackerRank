"""
https://www.hackerrank.com/challenges/mini-max-sum/problem?utm_campaign=challenge-recommendation&utm_medium=email&utm_source=24-hour-campaign
"""
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(n):
    # Write your code here
    max_sum = 0
    min_sum = 0
    # set the minimum and maximum to have an initial value of 0
    maxi = int(n[0])
    mini = int(n[0])
    # 3 2 4 1 5
    for j in range(1, len(n)):
        i = int(n[j])
        if i < maxi:
            max_sum += maxi
            maxi = i
        else:
            max_sum += i

        if i > mini:
            min_sum += mini
            mini = i
        else:
            min_sum += i
    print("{} {}".format(min_sum, max_sum))

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
