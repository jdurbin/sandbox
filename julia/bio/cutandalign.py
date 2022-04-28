#!/usr/bin/env python
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
alignmentsA1 = pairwise2.align.localxs(hlaref.seq,hlaseq.seq,-5,-1)

# HLA-DQA1
# time cutandalign.py
# cutandalign.py  26.87s user 2.25s system 98% cpu 29.673 total
