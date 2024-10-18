#!/bin/python3

import math
import os
import random
import re
import sys

def white_rabbit(data):
    neo = "[char i..f char.isalnum() or char in '!@#$%&' else ' ' for char in data]"
    trimmed = eval(neo.replace("..",""))

    return trimmed

def resurection(bluepill):
     regex = re.compile(r"(?<=[0-9A-Za-z])([^0-9A-Za-z]+)(?=[0-9A-Za-z])")
     print(re.subn(pattern=regex, repl=' ', string=bluepill)[0])


first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

m = int(first_multiple_input[1])

matrix = []
blue_pill = []
for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)
for i in range(m):

    neo = "i.f i < len(row):column+=row[i]"
    column = ""
    for row in matrix:
       exec(neo.replace(".",""))
    red_pill = white_rabbit(column)
    blue_pill.append("".join(red_pill))
  
choice = "".join(blue_pill)
resurection(choice)

