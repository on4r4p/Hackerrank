cube = lambda x: x ** 3

def fibonacci(n,f1=0,f2=1):
     if n == 0:return []
     return [f1] + fibonacci(n-1,f2,f2+f1)
         

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))
