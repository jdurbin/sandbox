#!/usr/bin/env python

import sys
from Bio import SeqIO

# chr16	21835086	21836107	chr16	21836107	21837222

if len(sys.argv) < 2:
    print("reverseComplement.py input.fa chr1 > output.fa")
    quit()

fasta_file = sys.argv[1]  # Input fasta file
chrom = sys.argv[2]

#print(f"Reading {fasta_file}...",end="")
seqdict = SeqIO.to_dict(SeqIO.parse(open(fasta_file),'fasta'))
#print("done.")

targetseq=seqdict[chrom]
outseq = targetseq.reverse_complement()

print(f">{chrom} reversecomplement")
print(outseq.seq)