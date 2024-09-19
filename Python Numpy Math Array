import numpy as pn
N,M,L = (*map(int,input().split()),lambda a,b: ([a+b,a-b,a*b,a//b,a%b,a**b]))
A,B = [pn.array([list(map(int,input().split()))for _ in range(N)]) for i in range(2)]
[*map(print,L(A, B))]
