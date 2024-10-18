from re import match
[print(bool(match(r'^[+-]?\d*\.\d*$',input().strip()))) for _ in range(int(input()))]
