#!/usr/bin/env python3
import pyranges as pr
import pandas as pd
import numpy as np

# Method 
def average(df):
    df = df.set_index(["Chromosome", "Start", "End", "Strand"])
    mean = df.mean(axis=1)
    mean.index = df.index
    mean.name = "Average"
    return mean.reset_index()

# Generate some random ranges. 
gr = pr.random(n=5)
print("GR: ")
print(gr)

# Generate some columns of random numbers
nums = pd.DataFrame(np.random.rand(len(gr), 3))
print("===== NUMS: ")
print(nums)

# Add the random numbers to the random ranges. 
gr2 = pr.PyRanges(pd.concat([gr.df, nums], axis=1))
print("GR2: ")
print(gr2)

print("GR2.apply() result:")
print(gr2.apply(average))

print("GR2 After Avg")
print(gr2)

