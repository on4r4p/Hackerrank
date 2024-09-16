from itertools import combinations
# Enter your code here. Read input from STDIN. Print output to STDOUT
ln = int(input())
letters = input().split(" ")
k =int(input())
ccnt = 0
acnt = 0
for c in combinations(letters,k):
    ccnt += 1
    if "a" in c: acnt += 1
    #print(c)
#print("ccnt:",ccnt)
#print("acnt:",acnt)
tot = acnt / ccnt
print(tot)
