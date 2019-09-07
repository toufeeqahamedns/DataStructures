"""
An array is a type of data structure that stores elements of the same 
type in a contiguous block of memory. In an array, A, of size N, each 
memory location has some unique index, i (where 0 <= i < N), that 
can be referenced as A[i] (you may also see it written as Ai).

Given an array, A, of N integers, print each element in reverse order 
as a single line of space-separated integers.

Note: If you've already solved our C++ domain's Arrays Introduction 
challenge, you may want to skip this.

"""

import math
import os
import random
import re
import sys

# Complete the reverseArray function below.
def reverseArray(a):
    return a[::-1]
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = reverseArray(arr)

    fptr.write(' '.join(map(str, res)))
    fptr.write('\n')

    fptr.close()
