#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the quickSort function below.
def quickSort(arr):

    l, e, r = [], [], []
    pivot = arr[0]

    for i in arr:
        if i == pivot:
            e.append(i) 
        elif i > pivot:
            r.append(i) 
        elif i < pivot:
            l.append(i) 

    if len(l) > 1:
        l = quickSort(l)

    if len(r) > 1:
        r = quickSort(r)

    return l + e + r

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = quickSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
