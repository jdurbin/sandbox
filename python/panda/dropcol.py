#!/usr/bin/env python3

import pandas as pd
import numpy as np


def changeCode(text):
    if "Male" in text: return("M")
    
    if "Female" in text: return("F")
    
    return("")
    
data = {"Name": ["James", "Alice", "Phil", "James","Mark"],
		"Age": [24, 28, 40, 24,48],
		"Sex": ["Male", "Female", "Male", "Male",""],
        "Charisma": [6,6,3,7,9]}

df = pd.DataFrame(data)
print(df,"\n\n")


df = df[['Age','Name']]

print(df)