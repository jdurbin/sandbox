#!/usr/bin/env python3

import pandas as pd
import sys
from tqdm import tqdm

# chr16	2547328	2549793	chr16	2652350	2654815	inv	107487
bedpeName = "chr16psv.bedpe"
#bedpe = pd.read_csv(bedpeName,sep="\t",names=('achr','astart','aend','bchr','bstart','bend','type','svsize'))
bedpe = pd.read_csv(bedpeName,sep="\t",)
print(bedpe)
#row1 = bedpe.loc[0]
#print(row1.achr,"\t",row1.bchr,"\t",row1.type)
#sys.exit(1)


#for index, row in bedpe.iterrows():
#     print("ITERROW:",row.achr,row.svsize)

def getParamString(row):
    return ','.join(map(str,row[7:]))

for row in bedpe.itertuples(index=True, name='Pandas'):
    print(row[1:7],"paramstr: ",getParamString(row))
 


    

# If don't pull out index, have to index into the tuple it returns
# first entry is the index, second entry is a series object. 
#for row in bedpe.iterrows():
#    print("CHECK2:",row[1].type,type(row),type(row[0]),type(row[1]))
    
