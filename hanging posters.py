"""
Arthur needs to hang  posters on his wall. Standing on the ground he can reach upto a height of .
Each poster is to be bolted at a certain height above the ground level, described by the array .
 Each poster also has some length, defined by the array .

To hang a poster properly, Arthur needs to hold atleast 50% of the length of the poster and poster is to be bolted at
 a point which is 25% from its top.

image
Arthur wants to know what is the minimum height of the ladder he should buy, in order to hang all the wall posters.
 sThe ladder is only available in integral heights. Arthur can reach any height upto the maximum possible height.
"""

#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'solve' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER h
#  2. INTEGER_ARRAY wallPoints
#  3. INTEGER_ARRAY lengths
#

def solve(h, wallPoints, lengths):
    # Write your code here

    ans = -sys.maxsize - 1

    for i in range(len(lengths)):
        i1 = lengths[i] * 0.25
        j1 = wallPoints[i] - i1
        j2 = round(j1)

        if j2 < j1:
            j2 = j2 + 1
        i3 = j2 - h

        if i3 > ans:
            ans = i3

    if ans < 0:
        return 0

    return ans


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    h = int(first_multiple_input[1])

    wallPoints = list(map(int, input().rstrip().split()))

    lengths = list(map(int, input().rstrip().split()))

    answer = solve(h, wallPoints, lengths)

    fptr.write(str(answer) + '\n')

    fptr.close()
