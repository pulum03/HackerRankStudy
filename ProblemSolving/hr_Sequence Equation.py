#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the permutationEquation function below.
def permutationEquation(p):
    p_d = dict()

    for i in range(len(p)):
        p_d[i+1] = p[i]
    
    #print(p_d)

    ans = []
    for x in range(1, len(p)+1):
        for y in p:
            if p_d[p_d[y]] == x:
                ans.append(y)
    print(ans)
    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    p = list(map(int, input().rstrip().split()))

    result = permutationEquation(p)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
