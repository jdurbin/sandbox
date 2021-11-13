#!/usr/bin/env python3

import sys
from sklearn.model_selection import ParameterGrid

# Read the search parameters. 
with open("test_spec.txt") as fin:
    grid_spec = eval(fin.read())
    grid = ParameterGrid(grid_spec)
    
for peak_find_params in grid:
    vals = list(peak_find_params.values())    
    print(",".join(map(str, vals)))
