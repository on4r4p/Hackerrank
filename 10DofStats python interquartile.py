#!/bin/python3

import math
import os
import random
import re
import sys
from statistics import quantiles

#
# Complete the 'interQuartile' function below.
#
# The function accepts following parameters:
#  1. INTEGER_ARRAY values
#  2. INTEGER_ARRAY freqs
#8.0

def interQuartile(values, freqs):
    # Print your answer to 1 decimal place within this function
    S = sorted([v for v,f in zip(values,freqs) for _ in range(f)])
    L = len(S)
    Q1 = (S[(L//4)-1] + S[(L//4)]) /2 if L%4 == 0 else S[L//4]
    Q3 = (S[3*(L//4)-1] + S[3*(L//4)]) /2 if 3*L%4 == 0 else S[3*L//4]
    print( f"{Q3 - Q1:.1f}")
    
    
if __name__ == '__main__':
    n = int(input().strip())

    val = list(map(int, input().rstrip().split()))

    freq = list(map(int, input().rstrip().split()))

    interQuartile(val, freq)
