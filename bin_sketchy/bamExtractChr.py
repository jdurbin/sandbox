#!/usr/bin/env python3
import sys,pysam


bamInName = sys.argv[1]
target = sys.argv[2]
bamOutName = sys.argv[3]

bamIn = pysam.AlignmentFile(bamInName)
bamOut = pysam.AlignmentFile(bamOutName,"wb",template=bamIn)

i = 0
for a in bamIn:
    refname = a.reference_name
    nextrefname = a.next_reference_name
  
    if refname==target: 
        bamOut.write(a)

    if i % 500000 == 0:
        print(f'{i:,} alignments examined.')

    i+=1