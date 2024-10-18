_,L=input(),list(map(int,input().split()))
print(all(n > 0 for n in L) and any(str(i) == str(i)[::-1] for i in L))
