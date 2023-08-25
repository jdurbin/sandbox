#!/usr/bin/env python3 

import plotly.graph_objs as go
import pandas as pd
import sys

colname = sys.argv[1]


df = pd.read_csv("v3_HLA-A.bed",sep="\t",names=["Chromosome","Start","End","null1","null2","null3","max","samples","avgdepth","min","depthcount"])

print(df[colname])
