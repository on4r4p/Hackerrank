n = input()
A = set(map(int,input().split()))
n = int(input())
[eval("A.%s(%s)"%(input().split()[0],list(map(int,input().split())))) for _ in range(n)]
print(sum(A))
