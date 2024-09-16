#!/bin/python3

import math
import os
import random
import re
import sys

from collections import Counter
#    o 12
#    m 11
#    n 11
def logo(s):
    cnt = Counter(s)
    if len({x[1] for x in cnt.most_common(3)}) == 1:
        for (c,v) in sorted(cnt.items(),key= lambda x:x[0])[:3]: print("%s %s"%(c,v))
    else:
        for (c,v) in sorted(cnt.items(),key= lambda x:(-x[1],x[0]))[:3]:
            print("%s %s"%(c,v))

        
if __name__ == '__main__':
    s = input()
    logo(s)
    

        
