import math
max_w = int(input())
boxs = int(input())
mean = int(input())
stdd = int(input())

mean_T = boxs *  mean
stdd_T = math.sqrt(boxs) * stdd
print(round(0.5 * (1 + math.erf(  ((max_w - mean_T) /stdd_T)   / math.sqrt(2))),4))
