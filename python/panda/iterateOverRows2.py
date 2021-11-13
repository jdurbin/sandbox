#!/usr/bin/env python3

import pandas as pd
import sys
from tqdm import tqdm

# chr16	2547328	2549793	chr16	2652350	2654815	inv	107487
bedpeName = "chr16psv.bedpe"
bedpeName = "gridsearch1_head.txt"
#bedpe = pd.read_csv(bedpeName,sep="\t",)
#for row in bedpe.itertuples(index=True, name='Pandas'):
#    print(row.achr,row.astart)

def gridParamStr(gridsv):
    print("GRIDSV:",gridsv)
    return f"{gridsv.svsize}"

for griddf in pd.read_csv(bedpeName,sep='\t', chunksize=10):
    print("CHUNK")
    for row in griddf.itertuples(): 
        print(row.achr,row.astart)

    
