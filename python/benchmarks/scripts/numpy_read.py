#!/usr/bin/env python

import numpy as np
import sys

filename = sys.argv[1]

# Method #1.  Works OK.  But what of my labels? 
f = open(filename)
ncols = len(f.readline().split('\t'))
data = np.loadtxt(f,delimiter="\t",skiprows=0,usecols=range(1,ncols)) 
print data.shape


# (11650, 5372)
# Durbinlib doubleTable:  8.8s 
# Pandas engine="c": 15s (1.7x)
# numpy 27.511s (3x)
# Pandas engine="python": 43s (4.8x)


# (11650, 8293)
# Durbinlib doubleTable 13s 
# Pandas engine="c": 30.2s (2.3x)
# numpy 46.716s (3.6x)
