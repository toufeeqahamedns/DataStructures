"""
Given a 6 * 6 2D Array, arr:

1 1 1 0 0 0
0 1 0 0 0 0
1 1 1 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0

We define an hourglass in A to be a subset of values with indices 
falling in this pattern in arr's graphical representation:

a b c
  d
e f g

There are 16 hourglasses in arr, and an hourglass sum is the sum of an hourglass' 
values. Calculate the hourglass sum for every hourglass in arr, 
then print the maximum hourglass sum.

For example, given the 2D array:

-9 -9 -9  1 1 1 
 0 -9  0  4 3 2
-9 -9 -9  1 2 3
 0  0  8  6 6 0
 0  0  0 -2 0 0
 0  0  1  2 4 0

We calculate the following 16 hourglass values:

-63, -34, -9, 12, 
-10, 0, 28, 23, 
-27, -11, -2, 10, 
9, 17, 25, 18
Our highest hourglass value is  from the hourglass:

0 4 3
  1
8 6 6
Note: If you have already solved the Java domain's Java 2D 
Array challenge, you may wish to skip this challenge.

"""

import math
import os
import random
import re
import sys

def findMax(arr, row, col):
    sum = arr[row + 0][col + 0] + arr[row + 0][col + 1] + arr[row + 0][col + 2] + arr[row + 1][col + 1] + arr[row + 2][col + 0] + arr[row + 2][col + 1] + arr[row + 2][col + 2]
    return sum
# Complete the hourglassSum function below.
def hourglassSum(arr):
    max = -9999
    arrlen = len(arr)
    for row in range(0, arrlen - 2):
        for col in range(0, arrlen - 2):
            sum = findMax(arr, row, col)
            if sum > max:
                max = sum
    return max
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
