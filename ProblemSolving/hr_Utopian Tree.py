# There is a pattern on the height every year.

# original height: 1

# year 1 (2 cycles) : 1*2+1 = 3 
# year 2 (4 cycles) : 3*2+1 = 7
# year 3 (6 cycles) : 7*2+1 = 15
# year 4 (8 cycles) : 15*2+1 = 31
# year 5 (10 cycles) : 31*2+1 = 63

# and you can notice the value in binary is like this

# year 1 (2 cycles) : 1*2+1 = 3     ->      11 
# year 2 (4 cycles) : 3*2+1 = 7     ->     111
# year 3 (6 cycles) : 7*2+1 = 15    ->    1111
# year 4 (8 cycles) : 15*2+1 = 31   ->   11111
# year 5 (10 cycles) : 31*2+1 = 63  ->  111111

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the utopianTree function below.
def utopianTree(n):

    ans =1
    for i in range(n):
        ans = ans*2 if i%2 ==0 else ans+1
        
    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = utopianTree(n)

        fptr.write(str(result) + '\n')

    fptr.close()
