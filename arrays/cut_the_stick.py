#https://www.hackerrank.com/challenges/cut-the-sticks/problem
'''
You are given a number of sticks of varying lengths. You will iteratively cut the sticks into smaller sticks, discarding
the shortest pieces until there are none left. At each iteration you will determine the length of the shortest stick
 remaining, cut that length from each of the longer sticks and then discard all the pieces of that shortest length. When
  all the remaining sticks are the same length, they cannot be shortened so discard them.

Given the lengths of  sticks, print the number of sticks that are left before each iteration until there are none left.

For example, there are  sticks of lengths . The shortest stick length is , so we cut that length from the longer two and
 discard the pieces of length . Now our lengths are . Again, the shortest stick is of length , so we cut that amount from
  the longer stick and discard those pieces. There is only one stick left, , so we discard that stick. Our lengths are .

'''

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the cutTheSticks function below.
def cutTheSticks(arr):

    arr.sort()
    ans = []
    ans.append(len(arr))

    while True:
        mina = arr[0]
        del arr[0]
        count = 0
        i = 0

        while i<len(arr):
            qw = arr[i] - mina

            if qw == 0:
                del arr[i]
            else:
                count+=1
                i+=1

        if count>0:
            ans.append(count)
        else:
            break

    return ans


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = cutTheSticks(arr)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
