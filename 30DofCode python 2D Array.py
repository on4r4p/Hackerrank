#!/bin/python3

import math
import os
import random
import re
import sys

def hourglass(nlst,needle):

     up = nlst[needle]
     mid = nlst[needle+1]
     bottom = nlst[needle+2]
     sumup = [up[i:i + 3] for i in range(len(up) - 2)]
     sumid = [mid[i + 1] for i in range(len(mid) - 2)]
     sumbot = [bottom[i:i + 3] for i in range(len(bottom) - 2)]
     sumhourglass = []
     for n,(sand1,sand3) in enumerate(zip(sumup,sumbot)):
           s123 = sum(sand1) + sum(sand3) + sumid[n]
           sumhourglass.append(s123)
     return(sumhourglass)

if __name__ == '__main__':

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
    results = []
    for i in range(int(len(arr)/2)+1):
        results.append(hourglass(arr,i))
    maxsum = max([z for x in results for z in x])
    print(maxsum)
