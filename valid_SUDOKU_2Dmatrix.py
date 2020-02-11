#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'validate' function below.
#
# The function is expected to return a STRING.
# The function accepts 2D_INTEGER_ARRAY data as parameter.
#

def validate(data):
    # Write your code here

    ans = ''

    matrix = [[0 for i in range(9)] for j in range(9)]

    for i in data:
        matrix[i[0] - 1][i[1] - 1] = i[2]

    # check for duplicate rows
    ro = []
    sig = 0

    for i in matrix:
        ro = []
        for j in i:
            if j != 0 and j in ro:
                sig = 1
                break
            else:
                ro.append(j)

    if sig == 1:
        return "WRONG INPUT"

    # check for duplicate coloumn

    rez = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]

    ro = []
    sig = 0

    for i in matrix:
        ro = []
        for j in i:
            if j != 0 and j in ro:
                sig = 1
                break
            else:
                ro.append(j)

    if sig == 1:
        return "WRONG INPUT"

    return ans


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    suduko = []

    for _ in range(n):
        suduko.append(list(map(int, input().rstrip().split())))

    ans = validate(suduko)

    fptr.write(ans + '\n')

    fptr.close()
