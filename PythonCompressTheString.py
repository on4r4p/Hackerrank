from itertools import groupby
string = input()
#(1, 1) (3, 2) (1, 3) (2, 1)
output = " ".join(["(%s, %s)"%(len(list(g)),s) for s,g in groupby(string)])
print(output)
#for s,g in groupby(string):
#    print("(%s, %s)"%(s,len(list(g))))
