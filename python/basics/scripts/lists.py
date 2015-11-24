#!/usr/bin/env python

import numpy as np

a = [1,2,3,4]

print a

print a[2:5]

# omitted in a slice assumed to have extreme value
print a[:3]
# a[:] is just a, the entire list

print "a[:-1]",a[:-1]
print "a[:-2]",a[:-2]


#numpy matrix:
# Note that [,] are lists, but (,) are tuples. 
# Lists are mutable, tuples are not. 
# tuple is a hashtable so you can use it as a dictionary(??)
mat = np.zeros((3,3))

print "MAT:\n",mat

# slices are always views, not copies. 
mat2=np.array([[1,2,3],[4,5,6],[7,8,9]])
print "MAT2:\n",mat2

print "MAT2[0:2]\n",mat2[0:2]

print "MAT2[,0:2]\n",mat2[:,0:2]

print "MAT2[0:1,0:2]:\n",mat2[0:1,0:2]

print "mat sqrt:\n",np.sqrt(mat2)

mat3 = np.array([2,2,2])

print "mat2 dot mat3:\n",mat2.dot(mat3)