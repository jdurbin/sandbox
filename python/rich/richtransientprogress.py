#!/usr/bin/env python
from rich.progress import track
from rich import print
from rich.progress import Progress

filename="big.fa"


num_lines = sum(1 for line in open(filename,'r'))
print("num_lines:",num_lines)
with Progress(transient=True) as progress:
    with open(filename) as f:
        for line in track(f,total=num_lines):
            if ">" in line: print(line)


