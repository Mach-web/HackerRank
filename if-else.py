#!/bin/python3

import math
import os
import random
import re
import sys

def weird(n):
    if n % 2 == 1:
        print('Weird')
    else:
        if (n >= 6) and (n <= 20):
            print('Weird')
        else:
            print('Not Weird')

if __name__ == '__main__':
    n = int(input().strip())
    weird(n)
