#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the happyLadybugs function below.
def happyLadybugs(b):

    s_b = set(b)

    #print(s_b)

    for s_b_i in s_b:
        if s_b_i != '_' and b.count(s_b_i) == 1:
            return 'NO'

    if b.count('_') == 0:
        for i in range(1,len(b)-1):
            if b[i-1] != b[i] and b[i+1] != b[i]:
                return 'NO'
    
    return 'YES'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    g = int(input())

    for g_itr in range(g):
        n = int(input())

        b = input()

        result = happyLadybugs(b)

        fptr.write(result + '\n')

    fptr.close()
