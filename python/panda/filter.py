#!/usr/bin/env python3

import pandas as pd
import numpy as np


def changeCode(text):
    if "Male" in text: return("M")
    
    if "Female" in text: return("F")
    
    return("")
    
data1 = {"Name": ["James", "Alice", "Phil", "Jim","Mark"],
		"Age": [24, 28, 40, 24,48],
		"Sex": ["Male", "Female", "Male", "Male",""]}
        
data2 = {"Name": ["Samuel", "Alice", "Thomas", "Jim","Mark"],
		"Age": [24, 27, 40, 24,49],
		"Sex": ["Male", "Female", "Male", "Male",""]}

df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)
print(df1,"\n\n")
print(df2,"\n\n")

df2notindf1 = df2[~df2['Name'].isin(df1['Name'])]
df1notindf2 = df1[~df1['Name'].isin(df2['Name'])]
print(df2notindf1,"\n\n")
print(df1notindf2,"\n\n")