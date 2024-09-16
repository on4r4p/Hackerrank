from collections import Counter
n,m = map(int,input().split())
Happyness = 0
Life = Counter(list(map(int,input().split())))
A = set(map(int,input().split()))
B = set(map(int,input().split()))

for a,b in zip(A,B):
    if a in Life.keys():
       Happyness += Life[a]
    if b in Life.keys():
        Happyness -= Life[b]
print(Happyness)
