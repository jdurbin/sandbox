#!/usr/bin/env python

import numpy as np
import pandas as pd

from rich import print
from rich import pretty

print("""
for line in fin:
    line.replace('bob','mark')
""")

s = pd.Series([1, 3, 5, np.nan, 6, 8])

