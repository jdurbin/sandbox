#!/usr/bin/env python3

import pandas as pd

print("WTF?  Seriously, WTF?")

data = {"Name": ["James", "Alice", "Phil", "James"],
		"Age": [24, 28, 40, 24],
		"Sex": ["Male", "Female", "Male", "Male"]}

df = pd.DataFrame(data)
print(df,"\n")

df2 = df.drop_duplicates(subset='Name', keep=False)

print(df2,"\n")

df3 = df.drop_duplicates(subset='Name', keep='first')

print(df3,"\n")


