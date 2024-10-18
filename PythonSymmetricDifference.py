m,A,n,B = (set(input().split(" ")) for _ in range(4))
print("\n".join(map(str,sorted([int(a) for a in A.symmetric_difference(B)]))))
