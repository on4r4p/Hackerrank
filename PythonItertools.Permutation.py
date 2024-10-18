# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import permutations
string,nbr = input().split(" ")
string = "".join(sorted(string))
for p in permutations(string,int(nbr)):
    print("".join(p))
