import numpy as n

NM =[*map(int, input().split()[:2])]
A,B=[n.array([list(map(int, input().split()))for _ in range(NM[i])]) for i in range(2)]
print(n.concatenate((A, B),axis=0))
