import numpy as np
np.set_printoptions(legacy='1.13')
A = np.array(tuple(map(float,input().split())))
print("%s\n%s\n%s"%(np.floor(A),np.ceil(A),np.rint(A)))
