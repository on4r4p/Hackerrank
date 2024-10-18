from math import comb
boy_ratio, girl_ratio = map(float, input().split(" "))
pb = boy_ratio / (boy_ratio + girl_ratio)
pf = 1 - pb
print(round(sum(comb(6, x) * (pb**x) * (pf**(6 - x)) for x in range(3, 7)),3))

