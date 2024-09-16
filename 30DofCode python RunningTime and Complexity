def isprime(n):
    if n <= 1:return False
    if n <= 3:return True
    if n % 2 == 0 or n % 3 == 0:return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:return False
        i += 6
    return True
    
T = int(input())
nums = [int(input()) for t in range(T)]
for n in nums:
    if isprime(n):print("Prime")
    if not isprime(n):print("Not prime")
