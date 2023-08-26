#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from Bio import SeqIO

# chr16	21835086	21836107	chr16	21836107	21837222

if len(sys.argv) < 5:
    print("Usage: \n")
    print("faregion input.fa chr6 100 500 output.fa\n")
    sys.exit(1)

fasta_file = sys.argv[1]  # Input fasta file
chrom = sys.argv[2]
start = int(sys.argv[3])
end = int(sys.argv[4])
outfile = sys.argv[5]

print(f"Reading {fasta_file}...",end="")
seqdict = SeqIO.to_dict(SeqIO.parse(open(fasta_file),'fasta'))
print("done.")

targetseq=seqdict[chrom] # This is a SeqRecord

targetseq.description = f"{fasta_file}:{start}-{end}"

with open(outfile,"w") as fout:
    SeqIO.write(targetseq[start:end],fout,"fasta")
