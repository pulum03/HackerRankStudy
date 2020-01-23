#!/bin/python3

import math
import os
import random
import re
import sys

from collections import Counter

# Complete the makingAnagrams function below.
def makingAnagrams(s1, s2):

    s2_l = list(s2)

    for s_i in s1:
        if s_i in s2_l:
            #print(s_i)
            s2_l.remove(s_i)

    nc = len(s2) - len(s2_l)

    #print(nc)

    return len(s1)+len(s2) - 2*nc


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s1 = input()

    s2 = input()

    result = makingAnagrams(s1, s2)

    fptr.write(str(result) + '\n')

    fptr.close()
