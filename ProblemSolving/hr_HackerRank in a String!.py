#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hackerrankInString function below.
def hackerrankInString(s):
    
    p = 0

    for h_i in 'hackerrank':
        if h_i in s[p:]:
            p = s.index(h_i,p) + 1
        else:
            return 'NO'
    
    return 'YES'


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = hackerrankInString(s)

        fptr.write(result + '\n')

    fptr.close()
