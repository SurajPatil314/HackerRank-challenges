"""
You have three stacks of cylinders where each cylinder has the same diameter, but they may vary in height. You can change the height of a stack by removing and discarding its topmost cylinder any number of times.

Find the maximum possible height of the stacks such that all of the stacks are exactly the same height. This means you must remove zero or more cylinders from the top of zero or more of the three stacks until they're all the same height, then print the height. The removals must be performed in such a way as to maximize the height.

Note: An empty stack is still a stack.
"""

#!/bin/python3

import os
import sys


#
# Complete the equalStacks function below.
#
def equalStacks(h1, h2, h3):
    lfirst = sum(h1)
    lsecond = sum(h2)
    lthird = sum(h3)

    ans = 0
    while (lfirst != 0 and lsecond != 0 and lthird != 0):
        # print('%d::%d::%d'%(lfirst,lsecond,lthird))
        if (lfirst == lsecond == lthird):
            ans = lfirst
            break
        localmax = max(lfirst, lsecond, lthird)
        if (localmax == lfirst):
            q = h1.pop(0)
            lfirst = lfirst - q
        elif (localmax == lsecond):
            q = h2.pop(0)
            lsecond = lsecond - q
        else:
            q = h3.pop(0)
            lthird = lthird - q

    return ans


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n1N2N3 = input().split()

    n1 = int(n1N2N3[0])

    n2 = int(n1N2N3[1])

    n3 = int(n1N2N3[2])

    h1 = list(map(int, input().rstrip().split()))

    h2 = list(map(int, input().rstrip().split()))

    h3 = list(map(int, input().rstrip().split()))

    result = equalStacks(h1, h2, h3)

    fptr.write(str(result) + '\n')

    fptr.close()
