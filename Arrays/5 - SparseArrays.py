"""
There is a collection of input strings and a collection of 
query strings. For each query string, determine how many 
times it occurs in the list of input strings.

For example, given input strings = ['ab', 'ab', 'abc'] and 
queries = ['ab', 'abc', 'bc'], we find 2 instances of 'ab',  
1 of 'abc' and 0 of 'bc'. For each query, we add an element to 
our return array, results = [2, 1, 0].

"""

import math
import os
import random
import re
import sys

# Complete the matchingStrings function below.
def matchingStrings(strings, queries):

    res = []

    for i in queries:
        count = 0
        for j in strings:
            if i == j:
                count += 1
        res.append(count)

    return res

if __name__ == '__main__':
    
    strings_count = int(input())

    strings = []

    for _ in range(strings_count):
        strings_item = input()
        strings.append(strings_item)

    queries_count = int(input())

    queries = []

    for _ in range(queries_count):
        queries_item = input()
        queries.append(queries_item)

    res = matchingStrings(strings, queries)

    print(res)

