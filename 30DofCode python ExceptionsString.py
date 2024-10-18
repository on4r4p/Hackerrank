#!/bin/python3

import math
import os
import random
import re
import sys

class BadString(Exception):
     def __init__(self,m):
       super().__init__(m)    
       self.m = m
        
S = input()
try:
        s = int(S)
        print(s)
except ValueError:
        print("Bad String")
