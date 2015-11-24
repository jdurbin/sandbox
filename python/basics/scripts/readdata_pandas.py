#!/usr/bin/env python

import numpy as np
import pandas as pd

# Pandas DataFrame is a bit like an R dataframe   
df = pd.read_csv("data/vijver2002.tab",delimiter="\t",header = 0,index_col=0)

rowNames = list(df.index)
print rowNames[0:3]
columnNames = list(df.columns.values)
print columnNames[0:3]

# Access by name
dataCol = df['VJV-14']
print dataCol

dataRow = df.loc['A1BG']
print dataRow
print dataRow.values

df = df._get_numeric_data() # wtf with the underscore?
numpy_array = df.as_matrix() # ready for scikit-learn
print numpy_array.shape





# http://pandas.pydata.org/pandas-docs/stable/dsintro.html



# Some other idioms
#print df.index.values[0:3]
#print df.columns.values[0:3]