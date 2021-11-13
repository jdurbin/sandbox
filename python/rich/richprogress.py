#!/usr/bin/env python

from rich.progress import track
from rich import print

filename="big.fa"

seqCount=0
num_lines = sum(1 for line in open(filename,'r'))
print("num_lines:",num_lines)
with open(filename) as f:
    for line in track(f,total=num_lines,description="Reading FASTA"):
        if ">" in line: 
            seqCount+=1
            print(line.strip(),seqCount)


