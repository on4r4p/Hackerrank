#n = 1 d = 3 k = 5 pxk = 0.868
n,d = map(float,input().split())
k = int(input())
p = n/d
#pxk = (1 - p)**k * p
#print(round(pxk,3))
print(round(sum((1 - p)**i * p for i in range(k)),3))
