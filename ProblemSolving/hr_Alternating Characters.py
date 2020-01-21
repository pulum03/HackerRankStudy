#!/bin/python3

import math
import os
import random
import re
import sys

from collections import Counter

# Complete the alternatingCharacters function below.
def alternatingCharacters(s):

    cnt = 0

    s = list(s)

    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            cnt += 1

    return cnt


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = alternatingCharacters(s)

        fptr.write(str(result) + '\n')

    fptr.close()
