#!/usr/bin/env python

import numpy as np
import pandas as pd


# Method #1.  Works OK.  But what of my labels? 
f = open("data/vijver2002.tab")
ncols = len(f.readline().split('\t'))
print ncols
data = np.loadtxt(f,delimiter="\t",skiprows=0,usecols=range(1,ncols)) 
print type(data)
print data.shape
print data.dtype
print data
