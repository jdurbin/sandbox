#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from Bio import SeqIO
from Bio import pairwise2
from Bio.pairwise2 import format_alignment

# Read sequence dictionary for HLA
seqFile = "data/S2_callseqs.fa"
seqdict = SeqIO.to_dict(SeqIO.parse(open(seqFile),'fasta'))

target = "HLA:HLA00602" # >HLA:HLA00602 DQA1*01:02:01:01 6484 bp
chrStart=32628178 # DQA1
chrEnd=32637531

# target = "HLA:HLA00010" # >HLA:HLA00010 A*02:05:01:01 3517 bpa
#chrStart = 29941259
#chrEnd = 29945884

hlaseq = seqdict[target]
print("hla seq: ",len(hlaseq))

# Read chromosome 6
chr6Name= "data/chr6_hg38.fa"
chr6Dict = SeqIO.to_dict(SeqIO.parse(open(chr6Name),'fasta'))
chr6seq = chr6Dict['chr6']

# Pull out region of chromosome6 
hlaref = chr6seq[chrStart:chrEnd]
print("hlaref: ",len(hlaref))

# Align that region to big HLA sequence
for i in range(1,2000):
    alignmentsA1 = pairwise2.align.globalxs(hlaref,hlaseq,-5,-1)

#print(format_alignment(*alignmentsA1[0]))

# HLA-A
# ./cutandalign.py  1.09s user 0.28s system 86% cpu 1.583 total

# HLA-DQA1
# ./cutandalign.py  1.07s user 0.26s system 86% cpu 1.547 total

# HLA-DQA1 * 2000
# ./cutandalign.py  13.03s user 0.32s system 98% cpu 13.524 total