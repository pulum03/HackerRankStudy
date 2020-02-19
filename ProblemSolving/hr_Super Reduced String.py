#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the superReducedString function below.
def superReducedString(s):

    l_s=list(set(s))
    
    c = 1
    
    while c!=0:
        c = 0
        for i in l_s:
            temp = s
            s = s.replace(i+i,'')

            if temp != s:
                l_s=list(set(s))
                c+=1
                
    if s:
        return s
    else:    
        return "Empty String"
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = superReducedString(s)

    fptr.write(result + '\n')

    fptr.close()
