import math
max_w = 250
boxs = 100
mean = 2.4
stdd = 2.0

mean_T = boxs *  mean
stdd_T = math.sqrt(boxs) * stdd
print(round(0.5 * (1 + math.erf(  ((max_w - mean_T) /stdd_T)   / math.sqrt(2))),4))
