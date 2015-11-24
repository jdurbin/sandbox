#!/usr/bin/env python

import pandas as pd
import numpy as np
from pandas import DataFrame, Series


df = DataFrame({'int_col' : [1,2,6,8,-1], 'float_col' : [0.1, 0.2,0.2,10.1,None], 'str_col' : ['a','b',None,'c','a']})

print df

# Extract just the float_col and int_col
#print df.ix[:,['float_col','int_col']]

print df[['float_col','int_col']]

# test indexing

#print df[df['float_col'] > 0.15]

# Handy!
print df.describe()

# Covariance between 'suitable' columns:
print df.cov()

# Correlation between columns. 
print df.corr()

values = df.values[:,:-1]
print "VALUES:\n",values

print type(values) # numpy ndarray
print type(values[1,1]) # int

# convert them all to float32 (some were int)
print df.values[:,:-1].astype(np.float32)
