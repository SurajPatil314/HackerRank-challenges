'''
https://www.hackerrank.com/challenges/utopian-tree/problem

The Utopian Tree goes through 2 cycles of growth every year. Each spring, it doubles in height. Each summer, its height increases by 1 meter.

Laura plants a Utopian Tree sapling with a height of 1 meter at the onset of spring. How tall will her tree be after  growth cycles?

For example, if the number of growth cycles is , the calculations are as follows:
'''

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the utopianTree function below.
def utopianTree(n):
    ans = 1
    if n==0:
        return ans
    for i in range(1,n+1):
        if i%2 == 0:
            ans = ans + 1
        else:
            ans = ans*2

    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = utopianTree(n)

        fptr.write(str(result) + '\n')

    fptr.close()
