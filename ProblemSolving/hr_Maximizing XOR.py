#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the maximizingXor function below.
def maximizingXor(l, r):
    
    res = []

    for i in range(l ,r+1):
        for j in range(l+1, r+1):
            res.append(i^j)
    
    return max(res)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    l = int(input())

    r = int(input())

    result = maximizingXor(l, r)

    fptr.write(str(result) + '\n')

    fptr.close()
