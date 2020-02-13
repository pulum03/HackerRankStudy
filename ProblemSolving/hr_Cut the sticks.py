#!/bin/python3

import math
import os
import random
import re
import sys

from collections import Counter

# Complete the cutTheSticks function below.
def cutTheSticks(arr):
    res = []
    
    l = len(arr)

    for k,v in sorted(Counter(arr).items()):
        res.append(l)
        l-=v
    
    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = cutTheSticks(arr)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
