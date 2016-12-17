import numpy as np

a = np.array([1,2,3])
print a

# numpy array can define type
b = np.array([[1,2,3],
				[4,5,6]],
					dtype = np.int)
d = np.array([2,4,6], dtype = np.float)
print b
print b.dtype
print d
print d.dtype

# numpy can define a all zero array
c = np.zeros((3,4))
print c

# numpy can define a all one array
e = np.ones((3,4))
print e

# numpy can define a empty array
f = np.empty((3,4))
print f

# numpy can define a sorted array
g = np.arange(2, 12, 2)
print g

h = np.arange(12).reshape((3,4))
print h

# numpy can define a line array
j = np.linspace(1, 10, 5)
print j
