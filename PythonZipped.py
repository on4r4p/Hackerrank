n,x = map(int,input().split())
[print(sum(s)/x)for s in zip(*[map(float,input().split()) for _ in range(x)])]

    
    
