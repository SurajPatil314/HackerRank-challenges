"""
Jesse loves cookies. He wants the sweetness of all his cookies to be greater than value . To do this, Jesse repeatedly mixes two cookies with the least sweetness. He creates a special combined cookie with:

sweetness  Least sweet cookie   2nd least sweet cookie).

He repeats this procedure until all the cookies in his collection have a sweetness .
You are given Jesse's cookies. Print the number of operations required to give the cookies a sweetness . Print  if this isn't possible.
"""

#!/bin/python3

import os
import sys

#
# Complete the cookies function below.
#
def cookies(k, A):
    from heapq import heappop,heappush,heapify

    heapify(A)
    fC = 0
    try:
        while A[0] < k:
            fC+=1
            c1 = heappop(A)
            c2 = heappop(A)
            newCookie=(1*c1)+(2*c2)
            heappush(A,newCookie)
        return fC
    except:
        return -1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    A = list(map(int, input().rstrip().split()))

    result = cookies(k, A)

    fptr.write(str(result) + '\n')

    fptr.close()
