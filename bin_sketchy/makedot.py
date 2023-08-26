#!/usr/bin/env python3
import sys,pysam
from collections import Counter

bamInName = sys.argv[1]
bamIn = pysam.AlignmentFile(bamInName)

pairCounts = Counter()
for a in bamIn:
    refname = a.reference_name
    nextrefname = a.next_reference_name

    # Skip low q reads
    if a.mapping_quality < 1: continue

    # Skip same chrom pairs
    if refname == nextrefname: continue
    
    pairname=f"{refname} {nextrefname}"
    pairCounts.update([pairname])

for key,value in pairCounts.items():
    print(f"{key} {value}")
    
  