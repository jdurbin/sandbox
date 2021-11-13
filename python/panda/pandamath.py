#!/usr/bin/env python3

import pandas as pd
import sys

# chr16	2547328	2549793	chr16	2652350	2654815	inv	107487
#bedpeName = "chr16psv.bedpe"
bedpeName = "small.bedpe"
bedpe = pd.read_csv(bedpeName,sep="\t",names=('achr','astart','aend','bchr','bstart','bend','type','svsize'))

bedpe['asize']=bedpe.aend-bedpe.astart
bedpe['bsize']=bedpe.bend-bedpe.bstart
bedpe['combinedSize']=bedpe.bend-bedpe.astart

print(bedpe)

gs1 = {"binsize": 32e3,"dil_size1": 3}
gs2 = {"binsize": 32e3,"dil_size1": 7}
gs3 = {"binsize": 32e3,"dil_size1": 11}
gs4 = {"binsize": 32e3,"dil_size1": 2}
params = dict()
params['id1'] = gs1
params['id2'] = gs1
params['id3'] = gs1
params['id4'] = gs1

firstkey = next(iter(params))
print(firstkey)
pkeys = params[firstkey].keys()
print(pkeys)

for pkey in pkeys:
    bedpe[pkey] = [params[id][pkey] for id in params.keys()]
    
print(bedpe)
