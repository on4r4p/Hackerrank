import numpy

A = numpy.array([list(map(float,input().split())) for _ in range(int(input()))])
print(round(numpy.linalg.det(A),2))
