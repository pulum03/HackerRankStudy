#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the kaprekarNumbers function below.
def kaprekarNumbers(p, q):

    ans = []
    for i in range(p, q+1):
        if i == 1:
            ans.append(i)

        elif i>8:
            squared = str(i**2)
            if i == int(squared[0:len(squared)//2]) + int(squared[len(squared)//2:]): 
                ans.append(i) 

    if ans:
        print(' '.join(map(str,ans)))

    else:
        print('INVALID RANGE')

if __name__ == '__main__':
    p = int(input())

    q = int(input())

    kaprekarNumbers(p, q)
