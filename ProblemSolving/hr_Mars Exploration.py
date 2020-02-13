#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the marsExploration function below.
def marsExploration(s):

    sos = (len(s)//3)*"SOS"

    cnt = 0

    for i in range(len(s)):
        if s[i] != sos[i]:
            cnt += 1

    return cnt
            
    


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = marsExploration(s)

    fptr.write(str(result) + '\n')

    fptr.close()
