#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    a=sum(arr)
    '''
    c=[]
    for i in arr:
        c.append(a-i)

    c.sort()
    arr.clear()
    arr.append(c[0])
    arr.append(c[len(c)-1])
'''
    print(f'{a-max(arr)} {a-min(arr)}')

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))
    

    miniMaxSum(arr)

