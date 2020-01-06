#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the repeatedString function below.
def repeatedString(s, n):

    #aba
    #10

    numOfa = s.count('a') # 2

    ans = 0

    i = n // len(s) # 3
    
    if numOfa == 0:
        return ans

    if n % len(s) == 0:
        ans = numOfa * i

    else:
        ans = numOfa * i + s[:n % len(s)].count('a')
    
    return ans




if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
