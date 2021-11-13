#!/usr/bin/env python3


fname = "chr21.fa"

with open(fname) as fin:
    for line in fin:
        if ">" in line: 
            print(line)
            
            