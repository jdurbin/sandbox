#!/usr/bin/env python3 

import plotly.graph_objs as go
import pandas as pd


# This is output to combined_coverage_v3.tsv
#print(f"chr6\t{loc}\t{loc}\t{loc2MinDepth[loc]}\t{loc2MaxDepth[loc]}\t{loc2DepthCounter[loc]}\t{sampleCount}\t{avgdepth}")
#chr     start       end         min     max     depthcount  samplecount avgdepth
#chr6	29944360	29944360	2176	7060	252951	62	4079.85
#
# The cursed output of pyranges.to_bed() is:  
# chr   start       end         n1  n2  n3  max     samples avgdepth    min depthcount
# chr6	29944360	29944360	.	.	.	7060	62	    4079.85	2176	252951
#
# What are they even doing?  So so cursed....

    

df = pd.read_csv("v3_HLA-B.bed",sep="\t",names=["Chromosome","Start","End","null1","null2","null3","max","samples","avgdepth","min","depthcount"])


fig = go.Figure([
    go.Scatter(
        name='Avg Depth',
        x=df['Start'],
        y=df['avgdepth'],
        mode='lines',
        line=dict(color='rgb(31, 119, 180)'),
    ),
    go.Scatter(
        name='Max Depth',
        x=df['Start'],
        y=df['max'],
        mode='lines',
        marker=dict(color="#444"),
        line=dict(width=0),
        showlegend=False
    ),
    go.Scatter(
        name='Min Depth',
        x=df['Start'],
        y=df['min'],
        marker=dict(color="#444"),
        line=dict(width=0),
        mode='lines',
        fillcolor='rgba(68, 68, 68, 0.3)',
        fill='tonexty',
        showlegend=False
    )
])
fig.update_layout(
    yaxis_title='Read Depth (bwa mem vs hg38)',
    title='HLA-B Coverage across samples',
    hovermode="x"
)
fig.show()