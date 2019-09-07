  
"""
Create a list, seqList, of N empty sequences, where each sequence is indexed from 0 to N-1.
The elements within each of the N sequences also use 0-indexing.

Create an integer, lastAns, and initialize it to 0.

The types of queries that can be performed on your list of sequences (seqList) are described below:
1] Query: 1 . y
	1] Find the sequence, seq, at index ((x xor lastAns) % N) in seqList.
	2] Append integer y to sequence seq
2] Query: 2 . y
	1] Find the sequence, seq, at index ((x xor lastAns) % N) in seqList.
	2] Find the value of element y % size in seq (where size is the size of seq) and assign it to lastAns.
	3] Print the new value of lastAns on a new line

"""

import math
import os
import random
import re
import sys

#
# Complete the 'dynamicArray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#



def dynamicArray(n, queries):
    # Write your code here
    seqList = [[] for _ in range(n)]
    lastAnswer = 0
    lastAns = []

    for i in queries:
        index = (i[1] ^ lastAnswer) % n
        seq = seqList[index]
        if i[0] == 1:            
            seq.append(i[2])
        elif i[0] == 2:
            size = len(seq)
            lastAnswer = seq[i[2] % size]
            lastAns.append(lastAnswer)
    
    return lastAns



if __name__ == '__main__':

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    q = int(first_multiple_input[1])

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    result = dynamicArray(n, queries)

    print(type(result))

