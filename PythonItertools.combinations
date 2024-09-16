# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations
string,nbr = input().split(" ")
string = "".join(sorted(string))
#comb = list(combinations(string,int(nbr)))
#print(comb)
for i in range(1,int(nbr)+1):
    for p in combinations(string,i):
        print("".join(p))
