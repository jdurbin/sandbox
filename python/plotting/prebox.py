#!/usr/bin/env python3 

import matplotlib.pyplot as plt
import random
import copy


stats = []

onestat = {
    "label": 'A',  # not required
    "mean":  5,  # not required
    "med": 5.5,
    "q1": 3.5,
    "q3": 7.5,
    # "cilo": 5.3 # not required
    # "cihi": 5.7 # not required
    "whislo": 2.0,  # required
    "whishi": 8.0,  # required
    "fliers": []  # required if showfliers=True
    }

for i in range(60):
    mystat = copy.deepcopy(onestat)
    mystat['med']=mystat['med']+random.uniform(-1,1)
    mystat['q1']=mystat['q1']+random.uniform(-1,1)
    mystat['q3']=mystat['q1']+random.uniform(-1,1)
    mystat['whislo']=mystat['whislo']+random.uniform(-1,1)
    mystat['whishi']=mystat['whishi']+random.uniform(-1,1)
    
    if i%4 :
        mystat['label']=""
    else:
        mystat['label']=i*20
    
    stats.append(mystat)


fs = 10  # fontsize

fig, axes = plt.subplots(nrows=1, ncols=1, figsize=(6, 6), sharey=True)
axes.bxp(stats,patch_artist=True)
axes.set_title('Boxplot for precalculated statistics', fontsize=fs)
plt.show()