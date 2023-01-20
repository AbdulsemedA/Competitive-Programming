#!/bin/python3

import math
import os
import random
import re
import sys

def countSwaps(a):
    swaps = 0
    size = len(a)
    
    for i in range(size):
        for j in range(size - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                swaps += 1
    
    print(f'Array is sorted in {swaps} swaps.')
    print(f'First Element: {a[0]}')
    print(f'Last Element: {a[-1]}')
    

if __name__ == '__main__':
    n = int(input().strip())
    a = list(map(int, input().rstrip().split()))

    countSwaps(a)
