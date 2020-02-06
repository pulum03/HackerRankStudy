#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the minimumDistances function below.
def minimumDistances(a):
    
    for i in range(1, len(a)):
        for j in range(len(a) - i):
            if a[j] == a[j+i]:
                return i
    return -1


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    a = list(map(int, input().rstrip().split()))

    result = minimumDistances(a)

    fptr.write(str(result) + '\n')

    fptr.close()
