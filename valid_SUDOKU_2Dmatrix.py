"""
https://www.hackerrank.com/contests/hackerrank-women-technologists-codesprint-2019/challenges/sudoku-input/problem

Suduko is a logic-based number-placement puzzle. The objective is to fill a 9×9 grid with digits so that each column, each row, and each of the nine 3×3 subgrids that compose the grid contains all of the digits from 1 to 9.

In this problem, you will be given a set of input data for a partially filled sudoku puzzle. Your task is to determine if it is a valid input. Print "OK" if input is valid. Otherwise print "WRONG INPUT".

Note that an input is valid if no rows, columns, or subgrids contain duplicates.
"""


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

    for i in rez:
        ro = []
        for j in i:
            if j != 0 and j in ro:
                sig = 1
                break
            else:
                ro.append(j)

    if sig == 1:
        return "WRONG INPUT"

    # check for sub grid duplicates

    i1 = 0
    i2 = 0

    q = 0
    w1 = []
    w2 = []
    w3 = []
    w4 = []
    w5 = []
    w6 = []
    w7 = []
    w8 = []
    w9 = []
    for i in range(0, 9, 1):
        for j in range(0, 9, 1):
            if i < 3 and j < 3:
                if matrix[i][j] != 0 and matrix[i][j] not in w1:
                    w1.append(matrix[i][j])
                elif matrix[i][j] == 0:
                    i1 = 0
                else:
                    q = 1
                    break
            # ^^^
            if i < 3 and (j > 2 and j < 6):
                if matrix[i][j] != 0 and matrix[i][j] not in w2:
                    w2.append(matrix[i][j])
                elif matrix[i][j] == 0:
                    i1 = 0
                else:
                    q = 1
                    print('break at 2')
                    break
            # ^^^
            if i < 3 and (j > 5 and j < 9):
                if matrix[i][j] != 0 and matrix[i][j] not in w3:
                    w3.append(matrix[i][j])
                elif matrix[i][j] == 0:
                    i1 = 0
                else:
                    q = 1
                    print('break at 3')
                    break
            # ^^^
            if (i > 2 and i < 6) and j < 2:
                if matrix[i][j] != 0 and matrix[i][j] not in w4:
                    w4.append(matrix[i][j])
                elif matrix[i][j] == 0:
                    i1 = 0
                else:
                    q = 1
                    print('break at 4')
                    break
            # ^^^
            if (i > 2 and i < 6) and (j > 2 and j < 6):
                if matrix[i][j] != 0 and matrix[i][j] not in w5:
                    w5.append(matrix[i][j])
                elif matrix[i][j] == 0:
                    i1 = 0
                else:
                    q = 1
                    print('break at 5')
                    break
            # ^^^
            if (i > 2 and i < 6) and (j > 5 and j < 9):
                if matrix[i][j] != 0 and matrix[i][j] not in w6:
                    w6.append(matrix[i][j])
                elif matrix[i][j] == 0:
                    i1 = 0
                else:
                    q = 1
                    print("i1 is %s" + str(i))
                    print("j1 is %s" + str(j))
                    print('break at 6')
                    break
            # ^^^
            if (i > 5 and i < 9) and j < 2:
                if matrix[i][j] != 0 and matrix[i][j] not in w7:
                    w7.append(matrix[i][j])
                elif matrix[i][j] == 0:
                    i1 = 0
                else:
                    q = 1
                    print('break at 7')
                    break
            # ^^^
            if (i > 5 and i < 9) and (j > 2 and j < 6):
                if matrix[i][j] != 0 and matrix[i][j] not in w8:
                    w8.append(matrix[i][j])
                elif matrix[i][j] == 0:
                    i1 = 0
                else:
                    q = 1
                    print('break at 8')
                    break
            # ^^^
            if (i > 5 and i < 9) and (j > 5 and j < 9):
                if matrix[i][j] != 0 and matrix[i][j] not in w9:
                    w9.append(matrix[i][j])
                elif matrix[i][j] == 0:
                    i1 = 0
                else:
                    q = 1
                    print('break at 9')
                    break

        if q == 1:
            break

    print(w1)

    if q == 1:
        return "WRONG INPUT"
    else:
        return "OK"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    suduko = []

    for _ in range(n):
        suduko.append(list(map(int, input().rstrip().split())))

    ans = validate(suduko)

    fptr.write(ans + '\n')

    fptr.close()
