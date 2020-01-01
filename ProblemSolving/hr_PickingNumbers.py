#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pickingNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

from collections import defaultdict

def pickingNumbers(a):
    # Write your code here
    d = defaultdict(int)
    r_v = 0

    for v in a:
        d[v] += 1
        r_v = max(r_v, d[v]+d[v+1], d[v]+d[v-1])

    return r_v

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    fptr.write(str(result) + '\n')

    fptr.close()
