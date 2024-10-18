from collections import namedtuple;n= int(input());Students = namedtuple('Students',input())
print(round(sum(int(Students(*input().split()).MARKS) for _ in range(n)) /n,2))
