from math import exp, factorial
lbda = float(input());k = int(input())
#print("lbda:",lbda)
#print("k:",k)
pkl = round(((lbda**k) * exp(-lbda)) / factorial(k),3)
print(pkl)
