#!/usr/bin/env python3

import sys
import pandas as pd
#from ExtractAndClean import findEmail

#xlfile=sys.argv[1]
xlfile="mined.xlsx"

dfs = pd.read_excel(xlfile, sheet_name=None)

print(dfs)

# Find the email column for each sheet
sheet2mail=dict()
for sheetName,df in dfs.items():
    print(sheetName,dfs.columns)


# Save the modified tables to a new file. 
writer = pd.ExcelWriter('bob.xlsx',engine='xlsxwriter')
for sheetName,df in dfs.items():
    df.to_excel(writer,sheet_name=sheetName,index=False)
writer.save()

