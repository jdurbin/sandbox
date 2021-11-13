#!/usr/bin/env python 

import seaborn as sns
from rich.console import Console
from rich.table import Table
from rich import print

from rich.color import ANSI_COLOR_NAMES

for color,index in ANSI_COLOR_NAMES.items():
    print(f"{index}\t[{color}]{color}\t\tIsn't this pretty.  1 2 3 4 5.678 [/{color}]")


