#!/usr/bin/env python3

import pandas as pd
import numpy as np

data = {"Name": ["James", "Alice", "Phil", "James","Mark"],
		"Age": [24, 28, 40, 24,48],
		"Sex": ["Male", "Female", "Male", "Male",""]}

df = pd.DataFrame(data)
print(df,"\n")

column = "Sex"
df2 = df[df[column] != ""]
print(df2)