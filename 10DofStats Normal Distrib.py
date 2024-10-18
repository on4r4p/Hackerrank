from math import erf,sqrt
mean,stdd = map(int,input().split(" "))
less_hour = float(input())
frm,to = map(float,input().split(" "))
probz = 0.5 * (1 + erf(((less_hour - mean) / stdd) / sqrt(2)))

P1 = 0.5 * (1 + erf(((frm - mean) /stdd) / sqrt(2)))

P2 = 0.5 * (1 + erf(((to - mean ) / stdd) / sqrt(2)))

probz2 = P2 - P1

#print("probz:",probz)
#print("P2:",probz2)
print(probz)
print(probz2)
