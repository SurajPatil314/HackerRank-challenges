""""
Given a square matrix, calculate the absolute difference between the sums of its diagonals.
"""
#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    for i in range(len(arr)):
        rn = 0
        ln = 0
        rows = len(arr[0])
        for i in range(len(arr)):
            for j in range(len(arr[0])):
                if (i == j):
                    rn = rn + arr[i][j];

                if (i + j + 1 == rows):
                    ln = ln + arr[i][j];

        return abs(rn - ln)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
