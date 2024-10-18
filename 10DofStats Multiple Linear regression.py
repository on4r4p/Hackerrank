def transpose(mat):
    return [list(row) for row in zip(*mat)]

def inverse(mat):
    size = len(mat)
    identity = [[1 if i == j else 0 for j in range(size)] for i in range(size)]
    augmented = [row[:] + identity_row for row, identity_row in zip(mat, identity)]
    for i in range(size):
        pivot = augmented[i][i]
        for j in range(size * 2):
            augmented[i][j] /= pivot
        for k in range(size):
            if k != i:
                factor = augmented[k][i]
                for j in range(size * 2):
                    augmented[k][j] -= factor * augmented[i][j]
    return [row[size:] for row in augmented]

def matrix(X, Y):
    return [[sum(x * y for x, y in zip(X_row, Y_col)) for Y_col in zip(*Y)] for X_row in X]

def linear_reg(X, Y):
    tx = transpose(X)
    xty = matrix(tx, Y)
    xtx = matrix(tx, X)
    inv_xtx = inverse(xtx)
    return [item for sublist in matrix(inv_xtx, xty) for item in sublist]

m, n = map(int, input().split(" "))
XY = [list(map(float, input().split(" "))) for _ in range(n)]
X = [[1] + x[:m] for x in XY]
Y = [[x[m]] for x in XY]
q = int(input())
qX = [list(map(float, input().split(" "))) for _ in range(q)]
NX = [[1] + x[:m] for x in qX]

b = linear_reg(X, Y)

for nx in NX:
    y = sum(bi * fi for bi, fi in zip(b, nx))
    print(f"{y:.2f}")
