import numpy as np

a = np.array([10, 20, 30, 40])
b = np.arange(4)

print a,b
c = a - b
print c
c = a + b
print c
c = a * b
print c
d = b ** 2
print d
c = np.sqrt(b)
print c
print "######################"

c = 10 * np.sin(a)
print c
c = 10 * np.cos(a)
print c
print "#######################"

print b
print b < 3
print b == 3
print "#######################"

a = np.array([[1,1],[0,1]])
b = np.arange(4).reshape((2,2))
# numpy have two matrix multiply
# * use to multiply for each item
# np.dot use ot matrix multiply 
print a
print b
c = a * b
print c
c = np.dot(a,b)
print c
c = a.dot(b)
print c
print "#######################"

a = np.random.random((2,4))

print a
print np.max(a)
print np.min(a)
print np.sum(a)
print np.max(a, axis = 1)
print np.min(a, axis = 0)



