#!/bin/python3

import math
import os
import random
import re
import sys

class Swap():
    def __init__(self,liste):
        self.liste = liste
        self.SwapTotal = 0
        
    def sort(self):
        for i in range(len(self.liste)):
            numberOfSwaps = 0
            for j in range(0,len(self.liste)-1-i):
                if self.liste[j] > self.liste[j+1]:
                    self.liste[j],self.liste[j+1] = self.liste[j+1] ,self.liste[j]
                    numberOfSwaps += 1
            self.SwapTotal += numberOfSwaps
            if numberOfSwaps == 0:
                break
        
    def getfirst(self):
            return(self.liste[0])
    def getlast(self):
            return(self.liste[-1])
    def gettot(self):
            return(self.SwapTotal)
                    

if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    buble = Swap(a)
    buble.sort()
    
    print("Array is sorted in %s swaps."%buble.gettot())
    print("First Element: %s"%buble.getfirst())
    print("Last Element: %s"%buble.getlast())
                
