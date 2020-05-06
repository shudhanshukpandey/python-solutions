#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
   # s=' '.join(list(map(lambda a:a.capitalize(),s.strip().split(' '))))
    s=' '.join(i.capitalize() for i in s.split(' '))
    return s

if __name__ == '__main__':
