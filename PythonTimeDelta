#!/bin/python3

import math
import os
import random
import re
import sys
from datetime import datetime

# Complete the time_delta function below.
def time_delta(t1, t2):
    #print("t1:",t1)
    #print("t2:",t2)
    obj1 = datetime.strptime(t1, "%a %d %b %Y %H:%M:%S %z")
    obj2 = datetime.strptime(t2, "%a %d %b %Y %H:%M:%S %z")
    if obj1.timestamp() > obj2.timestamp():
     #   print("obj1>")
        delta =  obj1 - obj2
    else:
      #  print("obj2>")
        delta =  obj2 - obj1     
        
    return(str(int(delta.total_seconds())))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)

        fptr.write(delta + '\n')

    fptr.close()
