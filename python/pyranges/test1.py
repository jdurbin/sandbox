#!/usr/bin/env python3

import pyranges as pr
import pandas as pd
import numpy as np

genesdf = pd.read_csv("final_gene_list.bed",sep="\t",names=["Chromosome","Start","End","Strand","id","Gene","required"])
genesranges = pr.PyRanges(genesdf)


depthdf1 = pd.read_csv("S1_capture_depth_q20.tsv",sep="\t",names=['Chromosome','Start','Depth'])
depthdf1['End'] = depthdf1['Start']
depthdf1=depthdf1.reindex(columns=['Chromosome','Start','End','Depth'])
print(depthdf1)


depthdf2 = pd.read_csv("S2_capture_depth_q20.tsv",sep="\t",names=['Chromosome','Start','Depth'])
depthdf2['End'] = depthdf2['Start']
depthdf2=depthdf2.reindex(columns=['Chromosome','Start','End','Depth'])
print(depthdf2)

combined = depthdf1.copy()
combined['dsum'] = combined['Depth']
print(combined)

combined['dsum'] = combined['dsum'] + depthdf2['Depth']
print(combined)


#depthranges1 = pr.PyRanges(depthdf1)
#depthranges2 = pr.PyRanges(depthdf2)
#print(type(depthranges1['chr6']))

#print(depthranges2['chr6',29941260:29945884])
#print(depthranges2['chr6',29941260:29945884])





# chr6    29941260        29945884        +       3105      HLA-A






#dr = depthranges['chr6',29941260:29945884]

#print(depthranges['chr6',29941260:29945884])
#for index,row in genesdf.iterrows():
#    print(f"{row['Gene']}\t{row['required']}")
#    print(depthranges[row['Chromosome'],row['Start']:row['End']])
    #print(depthranges['chr6',29941260:29945884])
    

