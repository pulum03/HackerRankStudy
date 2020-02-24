#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the pangrams function below.

from collections import Counter

def pangrams(s):
    
    c_s = Counter(s.lower())

    if len(c_s) == 27:
        return "pangram"

    else:
        return "not pangram"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = pangrams(s)

    fptr.write(result + '\n')

    fptr.close()
