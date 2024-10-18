if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    arr = list(dict.fromkeys(arr))

    if len(arr)>1:
        print(arr[-2])
