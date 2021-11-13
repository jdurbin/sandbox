#!/usr/bin/env python3

import pandas as pd
import sys
import matplotlib
import matplotlib.pyplot as plt
import numpy

# achr    astart  aend    svtype  svlen   refsize altsize biggersize
# 1       10403   10440   DEL     37      38      1       38
# 1       10415   10440   DEL     25      26      1       26

df = pd.read_csv(sys.argv[1],sep="\t")

sizelist = df['biggersize'].tolist()
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

plt.title("HG002_SVs_Tier1_v0.6.vcf Distribution of SV Sizes\nN=74012 min=21 Max=997k Mean=502 Median=38")
plt.ylabel("Log(count)")
plt.xlabel("SV Size (bp)")
plt.yscale('log')
plt.hist(sizelist,bins=100)

plt.show()

