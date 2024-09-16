#!/bin/python3

import math
import os
import random
import re
import sys
from statistics import quantiles


#
# Complete the 'quartiles' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def quartiles(arr):
    # Write your code here
    quant = sorted([i for i in quantiles(arr,n=4)])
    #print(quant)
    quant = [math.ceil(quant[0]),round(quant[1]),math.floor(quant[2])]
    return(quant)
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    data = list(map(int, input().rstrip().split()))

    res = quartiles(data)

    fptr.write('\n'.join(map(str, res)))
    fptr.write('\n')

    fptr.close()
