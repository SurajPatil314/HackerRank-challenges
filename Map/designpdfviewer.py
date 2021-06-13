#https://www.hackerrank.com/challenges/designer-pdf-viewer/problem

'''
When you select a contiguous block of text in a PDF viewer, the selection is highlighted with a blue rectangle. In this PDF viewer, each word is highlighted independently. For example:

PDF-highighting.png

In this challenge, you will be given a list of letter heights in the alphabet and a string. Using the letter heights given, determine the area of the rectangle highlight in  assuming all letters are  wide.

For example, the highlighted . Assume the heights of the letters are  and . The tallest letter is  high and there are  letters. The hightlighted area will be  so the answer is .
'''

#!/bin/python3

import math
import os
import random
import re
import sys
from string import ascii_lowercase


# Complete the designerPdfViewer function below.
def designerPdfViewer(h, word):
    alph = {}
    i = 0
    for c in ascii_lowercase:
        alph[c] = h[i]
        i += 1

    longest = alph[word[0]]
    for i in word:
        if alph[i] > longest:
            longest = alph[i]

    return longest * len(word)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = list(map(int, input().rstrip().split()))

    word = input()

    result = designerPdfViewer(h, word)

    fptr.write(str(result) + '\n')

    fptr.close()
