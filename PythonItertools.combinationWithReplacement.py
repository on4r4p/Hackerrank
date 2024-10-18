from itertools import combinations_with_replacement
string,nbr = input().split()
string = "".join(sorted(string))
for r in combinations_with_replacement(string,int(nbr)):
    print("".join(r))
