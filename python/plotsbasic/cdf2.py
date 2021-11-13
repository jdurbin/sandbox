#!/usr/bin/env python3
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import sys

indelfile="alignedlengths3.txt"
indeldata = pd.read_csv(indelfile,names=['counts'])
x = np.sort(indeldata['counts'])
y = np.arange(len(x))
y = y/float(len(x))
plt.plot(x, y)
plt.title("Aligned Read Lengths CDF\nOmniC_3")
plt.show()
