#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the gridChallenge function below.
def gridChallenge(grid):

    s_g = []

    for i in grid:
        s_g.append(sorted(i))
    
    for i in range(len(s_g)-1):
        for j in range(len(s_g)):
            if s_g[i][j] > s_g[i+1][j]:
                return 'NO'
    
    return 'YES'


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        grid = []

        for _ in range(n):
            grid_item = input()
            grid.append(grid_item)

        result = gridChallenge(grid)

        fptr.write(result + '\n')

    fptr.close()     
