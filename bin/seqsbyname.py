#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from Bio import SeqIO


if len(sys.argv) < 3:
    print("seqsbyname fastaFile targetList seqout.fa")
    sys.exit(1)

fasta_file = sys.argv[1]  # Input fasta file
targetlist = sys.argv[2]
outfile = sys.argv[3]


print(f"Reading {fasta_file}...",end="")
seqdict = SeqIO.to_dict(SeqIO.parse(open(fasta_file),'fasta'))
print("done.")


# >HLA:HLA00001 A*01:01:01:01 3503 bp
# >HLA:HLA02169 A*01:01:01:02N 3291 bp
# >HLA:HLA14798 A*01:01:01:03 3503 bp
# >HLA:HLA15760 A*01:01:01:04 3087 bp
# >HLA:HLA16415 A*01:01:01:05 3321 bp
# >HLA:HLA16417 A*01:01:01:06 3097 bp
targets=[]
with open (targetlist) as tin:
    for line in tin:
        # strip > from name if it's there
        line = line.strip().replace(">","")
        # Get the name separate from the description. 
        name = line.split()[0]
        targets.append(name)

with open(outfile,"w") as fout:
    for target in targets:
        targetseq=seqdict[target] # This is a SeqRecord
        SeqIO.write(targetseq,fout,"fasta")
