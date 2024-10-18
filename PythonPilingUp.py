from collections import deque
def pilup(n,cubes):
    last_cube = max(cubes)
    for _ in range(n):
        if cubes[0] >= cubes[-1]:current = cubes.popleft()
        else:current = cubes.pop()
        if current > last_cube:return "No"
        last_cube = current
    return "Yes"
        
t= int(input())
for _ in range(t):
    n = int(input())
    blocks = deque(tuple(map(int,input().split(" "))))
    print(pilup(n-1,blocks))
