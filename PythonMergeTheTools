def merge_the_tools(string, k):
    #print("K:",k)
    lns = len(string)
    cut_at = k#int(lns/k)
    #print("lns:",lns)
    #print("cut_at:",cut_at)
    splited = [string[i:i+cut_at] for i in range(0,lns,cut_at)]
    #print("splited:",splited)
    for s in splited:
        cnt = []
        for c in s:
            if c not in cnt:
                cnt.append(str(c))
        print("".join(cnt))
    

