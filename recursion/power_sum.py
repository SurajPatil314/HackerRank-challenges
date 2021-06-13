"""
Find the number of ways that a given integer, , can be expressed as the sum of the  powers of unique, natural numbers.

For example, if  and , we have to find all combinations of unique squares adding up to . The only solution is .
"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the powerSum function below.
def powerSum(X, N):

    return recf(X,N,1)

def recf(X,N,num):
    if X == pow(num,N):
        return 1
    elif X<pow(num,N):
        return 0
    else:
        #first recursive call is trying to see if the current base w
        # second recursive call is exploring the path that the curren
        return(recf(X,N,num+1)+ recf(X-pow(num,N),N,num+1))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    X = int(input())

    N = int(input())

    result = powerSum(X, N)

    fptr.write(str(result) + '\n')

    fptr.close()
