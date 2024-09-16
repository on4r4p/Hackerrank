from math import erf,sqrt
# excpected output
#    15.87
#    84.13
#    15.87
def normd(n):
    return 0.5 * (1 + erf(n / sqrt(2)))

#mean,stdd = map(int,input().split(" ")) 
#X1 = int(input())
#X2 = int(input())

mean = 70
stdd = 10
X1 = 80
X2 = 60


NZ1 = round(normd(((X2 - mean) /stdd))*100,2)
NZ2 = round(normd(((X1 - mean) /stdd))*100,2)
NZ3 = round((normd(((X2 - mean) /stdd)))*100,2)

print("%s\n%s\n%s"%(NZ1,NZ2,NZ3))
