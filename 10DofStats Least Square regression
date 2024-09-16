from math import sqrt

def std_dev(d):
    mean = sum(d) / len(d)
    variance = sum((v - mean) ** 2 for v in d) / len(d)
    return sqrt(variance)

def pearson(X, Y):
    mean_X = sum(X) / len(X)
    mean_Y = sum(Y) / len(Y)
    
    numerator = sum((X[i] - mean_X) * (Y[i] - mean_Y) for i in range(len(X)))
    denominator = sqrt(sum((X[i] - mean_X) ** 2 for i in range(len(X))) * sum((Y[i] - mean_Y) ** 2 for i in range(len(Y))))
    
    return numerator / denominator

n = 5
XY = tuple(tuple(map(int, input().strip().split(" "))) for _ in range(n))

X = tuple(x for x, y in XY)
Y = tuple(y for x, y in XY)

std_X = std_dev(X)
std_Y = std_dev(Y)

mean_X = sum(X) / len(X)
mean_Y = sum(Y) / len(Y)

r = pearson(X, Y)

b = r * (std_Y / std_X)
a = mean_Y - (b * mean_X)

x = 80
Regression_Line = a + (b * x)

print(round(Regression_Line, 3))
