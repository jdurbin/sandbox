#!/usr/bin/env python3 

import pandas as pd

df1 = pd.DataFrame(columns=['Chromosome', 'Start', 'End','Depth'])
df2 = pd.DataFrame(columns=['Chromosome', 'Start', 'End','Depth'])


# Suppose we have one counts file that we read into a data frame...
df1 = df1.append({'Chromosome':'chr6','Start':111,'End':111,'Depth':10},ignore_index=True)
df1 = df1.append({'Chromosome':'chr6','Start':112,'End':112,'Depth':20},ignore_index=True)
df1 = df1.append({'Chromosome':'chr6','Start':113,'End':113,'Depth':12},ignore_index=True)
df1 = df1.append({'Chromosome':'chr6','Start':114,'End':114,'Depth':22},ignore_index=True)
df1 = df1.append({'Chromosome':'chr6','Start':116,'End':116,'Depth':50},ignore_index=True)
df1 = df1.append({'Chromosome':'chr6','Start':117,'End':117,'Depth':60},ignore_index=True)
df1 = df1.append({'Chromosome':'chr6','Start':118,'End':118,'Depth':100},ignore_index=True)

print(df1)

# And a second counts file we load into a data frame...
df2 = df2.append({'Chromosome':'chr6','Start':111,'End':111,'Depth':100},ignore_index=True)
df2 = df2.append({'Chromosome':'chr6','Start':112,'End':112,'Depth':2},ignore_index=True)
df2 = df2.append({'Chromosome':'chr6','Start':113,'End':113,'Depth':22},ignore_index=True)
df2 = df2.append({'Chromosome':'chr6','Start':114,'End':114,'Depth':38},ignore_index=True)
df2 = df2.append({'Chromosome':'chr6','Start':115,'End':115,'Depth':21},ignore_index=True)
df2 = df2.append({'Chromosome':'chr6','Start':116,'End':116,'Depth':11},ignore_index=True)
df2 = df2.append({'Chromosome':'chr6','Start':117,'End':117,'Depth':26},ignore_index=True)
df2 = df2.append({'Chromosome':'chr6','Start':118,'End':118,'Depth':77},ignore_index=True)

print(df2)

# Want to create a new dataframe where DepthSum is the sum of the depths from the two input dataframes...
dfsum = pd.DataFrame(columns=['Chromosome', 'Start', 'End','Depth'])

dfsum = df1.copy()


dfsum['Depth']=dfsum['Depth']+df2['Depth']

print("DFSUM:")
print(dfsum)
