#!/bin/python3

import math
import os
import random
import re
import sys

def countingSort(arr):
    arr.sort()
    arr2 = []
    for i in range(100):
        if i in arr:
            arr2.append(arr.count(i))
            arr.remove(i)
        else:
            arr2.append(0)
    return arr2
         

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = countingSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
