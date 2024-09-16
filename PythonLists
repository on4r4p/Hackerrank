def retype(c):
    try:
        c = int(c)
        return int(c)
    except:
        return c
if __name__ == '__main__':
    N = int(input())
    res = []
    for i in range(N):
        l = input().split()
        cmd = l[0]
        if "insert" in cmd :
            idx = int(l[1])
            what =int(l[2])
            res.insert(idx,what)
        elif "append" in cmd:
             what = int(l[1])
             res.append(what)
        elif "print" in cmd:
            print(res)
        elif "remove" in cmd:
            what = int(l[1])
            res.remove(what)
        elif "sort" in cmd:
            res.sort()
        elif "pop" in cmd:
            res.pop()
        elif "reverse" in cmd:
            res.reverse()
        
