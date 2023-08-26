#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from Bio import SeqIO

fasta_file = sys.argv[1]  # Input fasta file

seqCount = 0
totalLength = 0
fasta_sequences = SeqIO.parse(open(fasta_file),'fasta')
print("name\tsize")
for seq in fasta_sequences:
    seqCount +=1
    seqLen = len(seq)
    print(seq.name,"\t",seqLen)
    


# fasta_file:  data/Asm2m82206.scaffolds.fa
# Sequences:   31710
# Total size:  711,438,399.  (85.6% of wtdbg2 size)

# fasta_file:  data/wtdbg2_ont40x.fa
# Sequences:   3320
# Total size:  830,665,017

