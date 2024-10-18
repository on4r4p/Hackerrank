from math import sqrt
def cov(n, x, x_, y, y_):
    cov_xy = 1 / n * sum((x[i] - x_) * (y[i] - y_) for i in range(n))
    return cov_xy
    
def barre(n, a):
    a_bar = 1 / n * sum(a[i] for i in range(n))
    return a_bar
    
def variance(n,a,a_):
    a_stdd = 1 / n * sum((a[i]-a_) ** 2 for i in range(n))
    return a_stdd
    
n = int(input())
X = tuple(map(float, input().strip().split(" ")))
Y = tuple(map(float, input().strip().split(" ")))

x_bar = barre(n, X)
y_bar = barre(n, Y)

#print("xbar:", x_bar)
#print("ybar:", y_bar)

v_x = variance(n,X,x_bar)
v_y = variance(n,Y,y_bar)

stdd_x = sqrt(v_x)
stdd_y = sqrt(v_y)

#print("stdd_x:",stdd_x)
#print("stdd_y:",stdd_y)

cov_xy = cov(n, X, x_bar, Y, y_bar)
#print("cov_xy:", cov_xy)
pearson = cov_xy / ( stdd_x * stdd_y)
print(round(pearson,3))

