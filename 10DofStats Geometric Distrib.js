#n = 1 d = 3 k = 4
n,d = map(float,input().split())
k = int(input())-1
p = n/d
pxk = (1 - p)**k * p
print(round(pxk,3))
#print(sum((1 - p)**i * p for i in range(k)))
