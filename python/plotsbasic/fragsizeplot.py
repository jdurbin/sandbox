#!/usr/bin/env python3

import pandas as pd
import sys
import matplotlib
import matplotlib.pyplot as plt
import numpy


df = pd.read_csv("fragsizes.txt",names=['Distance Between First and Last SNP'])

sizelist = df['Distance Between First and Last SNP'].tolist()
#x = np.sort(sizelist)
#y=np.arange(len(x))
#y = y/float(len(x))
#plt.plot(x,y)
#

data = numpy.array(sizelist)
print("N:", len(data))
print("Min:", numpy.min(data))
print("Max:", numpy.max(data))
print("Mean:", numpy.mean(data))
print("Median:", numpy.median(data))
print("STD:", numpy.std(data))
print("CV:", numpy.std(data) / numpy.mean(data))
print("Sum:", numpy.sum(data))

plt.title("Distibution of Fragment Sizes\nMax: 39,995,925 Mean: 694,622 Median: 61")
plt.ylabel("Log(count)")
plt.xlabel("Distance Between First and Last SNP In Fragment")
plt.yscale('log')
plt.hist(sizelist,bins=100)

plt.show()

