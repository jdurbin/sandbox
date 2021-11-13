#!/usr/bin/env python3

import numpy as np  
import pandas as pd  
import random
import matplotlib.pyplot as plt 
import sys
import copy


# Base	Mean	Median	LowerQuartile	UpperQuartile	TenthPercentile	NinetyPercentile
# 1	34.28725190918221	37.0	37.0	37.0	25.0	37.0
# 2	34.73897959624481	37.0	37.0	37.0	25.0	37.0

fin = "/Users/james/projects/arimasmack/explore/omni/70X/HG002.HiC_1_NovaSeq_1_S1_L002_R2_001_fastqc/seqqual.tsv"
df = pd.read_csv(fin,sep="\t")

stats=[]

for index,row in df.iterrows():
    if index%4 :
        label=""
    else:
        label=row.Base
    
    onestat = {
     "label": label,  # not required
     "mean":  row.Mean,  # not required
     "med": row.Median,
     "q1": row.LowerQuartile,
     "q3": row.UpperQuartile,
     # "cilo": 5.3 # not required
     # "cihi": 5.7 # not required
     "whislo": row.TenthPercentile,  # required
     "whishi": row.NinetyPercentile,  # required
     "fliers": []  # required if showfliers=True
    }
    stats.append(onestat)
   
 
fs = 10  # fontsize

fig, axes = plt.subplots(nrows=1, ncols=1, figsize=(6, 6), sharey=True)
axes.bxp(stats,patch_artist=True)
axes.set_title('Per base sequence quality', fontsize=fs)
plt.show()