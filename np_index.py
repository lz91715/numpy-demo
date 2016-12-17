import numpy as np

# numpy index
A = np.arange(3, 15).reshape((3, 4))
print A
print A[2]
print A[1][1]
print A[1,1]
print A[0,:]
print A[:, 0]
print A[:, 0:2]

# numpy row iter
for row in A:
	print row

# numpy column iter
for col in A.T:
	print col

# numpy item iter 
print A.flatten()
for item in A.flat:
	print item


