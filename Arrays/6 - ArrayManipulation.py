"""
 Starting with a 1-indexed array of zeros and a list of operations, for 
each operation add a value to each of the array element between two 
given indices, inclusive. Once all operations have been performed, 
return the maximum value in your array.

For example, the length of your array of zeros n = 10. Your list of queries is as follows:

    a b k
    1 5 3
    4 8 7
    6 9 1

Add the values of k between the indices a and b inclusive:

index ->    1 2 3  4  5 6 7 8 9 10
	        [0,0,0, 0, 0,0,0,0,0,0]
	        [3,3,3, 3, 3,0,0,0,0,0]
	        [3,3,3,10,10,7,7,7,0,0]
	        [3,3,3,10,10,8,8,8,1,0]

The largest value is 10 after all operations are performed.

"""

import math
import os
import random
import re
import sys

# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):
    a = [0] * (n + 1)

    for i, j, k in queries:
        a[i - 1] += k
        if(j <= len(a)):
            a[j] -= k
    max = i = 0
    print(a)
    for x in a:
        i = i + x
        if (max < i):
            max = i
    return max    

if __name__ == '__main__':
    
    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    print(result)