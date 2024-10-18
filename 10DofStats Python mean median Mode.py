# Enter your code here. Read input from STDIN. Print output to STDOUT
from statistics import mean,median,mode
from collections import Counter

N = input()
X = sorted(list(map(int,input().split(" "))))
print(mean(X))
print(median(X))
print(mode(X))
