import numpy as np

A = np.array([1, 1, 1])
B = np.array([2, 2, 2])

# vertical stack
C = np.vstack((A, B)) 
print A.shape, C.shape

# horization stack
D = np.hstack((A, B))
print A.shape, D.shape

# np.newaxis add new dimension 
print A[np.newaxis, :]
print A[np.newaxis, :].shape
print A[:, np.newaxis]
print A[:, np.newaxis].shape

#
A = np.array([1,1,1])[:, np.newaxis]
B = np.array([2,2,2])[:, np.newaxis]

C = np.concatenate((A,B), axis = 1)
print C
C = np.concatenate((A,B), axis = 0)
print C
