"""
A left rotation operation on an array of size  shifts each of 
the array's elements 1 unit to the left. For example, if 2 left 
rotations are performed on array [1, 2, 3, 4, 5], then the array would become [3, 4, 5, 1, 2].

Given an array of n integers and a number, d, perform d left 
rotations on the array. Then print the updated array as a single line of space-separated integers.

"""

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))

    mod = d % n

    for i in range(0, n):
        print(str(a[(mod + i) % n]), end = " ")

    
