#!/bin/python3

import math
import os
import random
import re
import sys

from collections import defaultdict

# Complete the minimumSwaps function below.

"""
https://www.hackerrank.com/challenges/minimum-swaps-2/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays

You are given an unordered array consisting of consecutive integers  [1, 2, 3, ..., n] without any duplicates. You are allowed to swap any two elements. Find the minimum number of swaps required to sort the array in ascending order.
"""


def minimumSwaps(arr):
    ans = 0
    arr1 = defaultdict(int)

    for i in range(len(arr)):
        arr1[arr[i]] = i

    for i in range(len(arr)):

        if arr[i] == i + 1:
            continue
        else:
            i1 = arr1[i + 1]

            arr[i], arr[i1] = arr[i1], arr[i]
            arr1[i] = i + 1
            arr1[arr[i1]] = i1
            ans += 1

    return ans


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

    fptr.write(str(res) + '\n')

    fptr.close()
