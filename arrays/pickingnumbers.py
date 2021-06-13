#!/bin/python3
'''
Given an array of integers, find and print the maximum number of integers you can select from the array such that the
absolute difference between any two of the chosen integers is less than or equal to . For example, if your array is ,
 you can create two subarrays meeting the criterion:  and . The maximum length subarray has  elements.
'''

import math
import os
import random
import re
import sys

#
# Complete the 'pickingNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def pickingNumbers(a):
    a.sort()
    ans = 0
    tempaans = 0
    q = []
    i=0
    while(i<len(a)):
        if len(q) == 0:
            #print('in if')
            #print(q)
            q.append(a[i])
            tempaans = 1
            i= i+1
            if tempaans>ans:
                ans =tempaans
        else:
            if((q[0]==a[i]) or(q[0]+1==a[i])):
                tempaans =tempaans+1
                if tempaans>ans:
                    ans =tempaans
                i=i+1
                #print('in else')
                #print(q)
            else:
                #print('in else if')
                #print(a[i])
                q.clear()

    return ans


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    fptr.write(str(result) + '\n')

    fptr.close()
