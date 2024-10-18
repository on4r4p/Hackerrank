
def get_ranks(nbrs):
    ranks = [0] * len(nbrs)
    i = 0
    while i < n:
        j = i
        while j < n - 1 and nbrs[j][0] == nbrs[j + 1][0]:
            j += 1
        avg_rank = (i + j + 2) / 2.0
        for k in range(i, j + 1):
            ranks[nbrs[k][1]] = avg_rank
        i = j + 1 
    return ranks
    
    
        
    

n = int(input())
X = tuple(map(float,input().strip().split(" ")))
Y = tuple(map(float,input().strip().split(" ")))
Xi = sorted((x, r) for r, x in enumerate(X))
Yi = sorted((y, r) for r, y in enumerate(Y))
#print("Xi:",Xi)
#print("Yi:",Yi)

Xr = get_ranks(Xi)
Yr = get_ranks(Yi)
#print("Xr:",Xr)
#print("Yr:",Yr)
sum2 = sum((Xr[i] - Yr[i]) ** 2 for i in range(n))

P = 1 - (6 * sum2) / (n * (n**2 - 1))
print(round(P,3))

