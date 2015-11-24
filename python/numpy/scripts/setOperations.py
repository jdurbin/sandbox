#!/usr/bin/env python 

import numpy as np

a = np.array([2,3,4,5.1,10,11,12,13,15,16,19])
b = np.array([4,5.2,7,10,12,24])

print "INTERSECTION:\n",np.intersect1d(a,b)  # 4,10,12
