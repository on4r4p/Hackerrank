# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(input())
for i in range(n):
    try:
        ab = input().split(" ")
        a = int(ab[0])
        b = int(ab[1])
        print(int(a/b))
    except ZeroDivisionError:
        print("Error Code: integer division or modulo by zero")
    except ValueError as e:
        print("Error Code: %s"%e)
    except Exception as e:
        print("Error Code: ",e)
