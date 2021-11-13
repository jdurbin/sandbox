#!/usr/bin/env python3

import sys
import pandas as pd
from ExtractAndClean import findEmail

#xlfile=sys.argv[1]
xlfile="excel1.xlsx"

dfs = pd.read_excel(xlfile, sheet_name=None)

# Find the email column for each sheet
sheet2mail=dict()
for sheetName,df in dfs.items():
    for colName in df.columns: 
        if "Email" in colName or "email" in colName:        
            sheet2mail[sheetName] = colName

print("sheet2mail: ",sheet2mail)

# Extract just the email address out of each row of the 
# email column, then remove leading/trailing spaces an d
# leading/trailing periods, and save it to a new column. 
for sheetName,colName in sheet2mail.items():
    sheet = dfs[sheetName]
    newColName = f"Clean{colName}"
    sheet[newColName] = sheet[colName].apply(findEmail)
    sheet[newColName] = sheet[newColName].str.strip(" ")
    sheet[newColName] = sheet[newColName].str.strip(".")
    
# Save the modified tables to a new file. 
writer = pd.ExcelWriter('excel1_clean.xlsx',engine='xlsxwriter')
for sheetName,df in dfs.items():
    df.to_excel(writer,sheet_name=sheetName,index=False)
writer.save()

