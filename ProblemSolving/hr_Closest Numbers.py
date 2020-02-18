#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the closestNumbers function below.
def closestNumbers(arr):

    s_a = sorted(arr)
    
    diff = []

    for i in range(len(s_a) - 1):
        diff.append(s_a[i+1] - s_a[i])

    #print(min(diff))

    min_d = min(diff)

    res = []

    for i in range(len(s_a) - 1):
        if s_a[i+1] - s_a[i] == min_d:
            res.append(s_a[i])
            res.append(s_a[i+1])

    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = closestNumbers(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
