from collections import deque
def cmd(c,d):
    c = c.split(" ")
    methode = c[0];nbr = None
    if len(c) > 1:
       methode,nbr = c
        
    if nbr:
        if "left" in methode:
            d.appendleft(nbr)
        else:
            d.append(nbr)
    else:
        if "left" in methode:
            d.popleft()
        else:
            d.pop()
            
d = deque()
n = int(input())
for _ in range(n):
    cmd(input(),d)

print(" ".join(d))
