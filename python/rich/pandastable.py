#!/usr/bin/env python 

import seaborn as sns
from rich.console import Console
from rich.table import Table
from rich import print


colors=["turquoise4","indian_red","deep_sky_blue2","plum4","deep_pink4","orange4","cadet_blue","aquamarine3","dark_khaki"]

def printrich(df,table_title):
    table = Table(title=table_title)

    coloridx = 0
    for col in df.columns:
        table.add_column(col, style=colors[coloridx])
        coloridx+=1
        print(col)


    for index,row in df.iterrows():
        rlist = row.tolist()
        rlist = list(map(str,rlist))
        table.add_row(*rlist)

    console = Console()
    console.print(table, justify="center")




iris = sns.load_dataset('iris')
printrich(iris,"IRIS Dataset")
