import numpy as np

A = np.arange(2, 14).reshape((3, 4))
# numpy can get minimize variable's index
# numpy can get maximize variable's index
print A
print np.argmin(A)
print np.argmax(A)
# numpy can get array's mean
# numpy can get array's median
print np.mean(A)
print np.median(A)

# numpy can get 
print np.cumsum(A)
print np.diff(A)

# numpy can get 
print np.nonzero(A)
print np.sort(A)
print np.transpose(A)
print A.T

# numpy can set max and min value, let variables not over this
print np.clip(A, 5, 9)
