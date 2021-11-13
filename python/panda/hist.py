#!/usr/bin/env python3

from pandas import DataFrame
import numpy as np
import matplotlib.pyplot as plt


x = ['A']*300 + ['B']*400 + ['C']*300
y = np.random.randn(1000)
df = DataFrame({'Letter':x, 'N':y})

print(df.head())
df['N'].hist()

plt.show()
#df['N'].hist(by=df['Letter'],bins=40)