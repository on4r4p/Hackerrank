from collections import defaultdict
# Enter your code here. Read input from STDIN. Print output to STDOUT
a, b = map(int, input().split(" "))
#print("a:",a)
#print("b:",b)
d = defaultdict(list)

for i in range(a):
    d["GROUPEA"].append(input())
    
for i in range(b):
    d["GROUPEB"].append(input())

#print("d:",d)

for word_gb in d["GROUPEB"]:
    if not word_gb in d["GROUPEA"]:
        print(-1)
    else:
        id = []
        for i,word_ga in enumerate(d["GROUPEA"],start=1):
            if word_ga == word_gb:
                id.append(str(i))
        print(" ".join(id))
        
