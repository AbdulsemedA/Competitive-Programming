#!/bin/python3

import math
import os
import random
import re
import sys

def countingValleys(steps, path):
    arr =[]
    for i in path:
        arr.append(i)
    counter = 0
    value = 0
    for item in arr:
        if item == "U":
            value+=1
            if (value-1) == -1:
                counter += 1
        elif item == "D":
            value-=1
            if value == 0 and value+1 !=1:
                counter += 1
    return counter            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()
