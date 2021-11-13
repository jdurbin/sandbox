#!/usr/bin/env python
from tqdm import tqdm

filename="big.fa"


num_lines = sum(1 for line in open(filename,'r'))
print("num_lines:",num_lines)
with open(filename) as f:
    for line in tqdm(f,total=num_lines):
        if ">" in line: print(line)


